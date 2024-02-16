from dataclasses import dataclass
from library.model.aicore import AiCoreMetadata as AiCoreMetadataDefinition
import os
import logging
import json
import time
import requests
import base64
import sys
from library.constants.timings import RETRY_TIME_IN_SECONDS_AICORE_DEPLOYMENT_URL

log = logging.getLogger(__name__)


@dataclass
class AiCoreMetadata(AiCoreMetadataDefinition):
    def __init__(self):
        self.authUrl = os.environ.get("AICORE_LLM_AUTH_URL")
        self.clientId = os.environ.get("AICORE_LLM_CLIENT_ID")
        self.clientSecret = os.environ.get("AICORE_LLM_CLIENT_SECRET")
        self.resourceGroup = os.environ.get("AICORE_LLM_RESOURCE_GROUP")
        self.apiBase = os.environ.get("AICORE_LLM_API_BASE")
        self.targetAiCoreModel = json.loads(os.environ.get("TARGET_AI_CORE_MODEL"))
        self.apiAccessToken = get_api_access_token(self)
        self.availableModels = get_available_ai_models(self)
        self.configurationIds = create_configuration(self)
        self.deployment = create_deployments(self)


# Retrieve the access token from the AI Core system
def get_api_access_token(aiCoreMetadata: AiCoreMetadataDefinition) -> str:
    token = None
    clientId = aiCoreMetadata.clientId
    clientSecret = aiCoreMetadata.clientSecret
    authUrl = aiCoreMetadata.authUrl

    # Create the authorization string
    authorizationString = f"{clientId}:{clientSecret}"
    # Encode the authorization string
    byte_data = authorizationString.encode("utf-8")
    # Base64 encode the byte data
    clientSecretBase64 = base64.b64encode(byte_data).decode("utf-8")

    # Create the URL to retrieve the access token
    aiCoreLocation = f"{authUrl}/oauth/token?grant_type=client_credentials"
    # Create the headers for the request
    headers = {"Authorization": f"Basic {clientSecretBase64}"}

    # Retrieve the access token from the AI Core system
    try:
        # Send the request to retrieve the access token
        r = requests.post(url=aiCoreLocation, headers=headers)
        # Retrieve the access token from the response
        if r.ok is True:
            token = r.json()["access_token"]
            return token
        else:
            log.info(f"Response status code: {r.status_code} ({r.reason}): {r.text}")
            log.error("Could not retrieve access token from AI Core system! Exiting...")
            sys.exit(1)
    except requests.exceptions.RequestException:
        log.error("Could not retrieve access token from AI Core system! Exiting...")
        sys.exit(1)


# Retrieve the available AI models from the AI Core system
def get_available_ai_models(aiCoreMetadata: AiCoreMetadataDefinition) -> str:
    token = aiCoreMetadata.apiAccessToken
    apiBase = aiCoreMetadata.apiBase

    # Create the URL to retrieve the available AI models
    aiCoreLocation = f"{apiBase}/v2/lm/scenarios/foundation-models/executables"
    # Create the headers for the request
    headers = {
        "AI-Resource-Group": aiCoreMetadata.resourceGroup,
        "Authorization": f"Bearer {token}",
    }

    # Retrieve the available AI models from the AI Core system
    try:
        # Send the request to retrieve the available AI models
        log.info("Retrieving available AI models from AI Core system...")
        r = requests.get(url=aiCoreLocation, headers=headers)
        if r.ok is True:
            # Retrieve the available AI models from the response
            models = r.json()
            return models
        else:
            log.info(f"Response status code: {r.status_code} ({r.reason}): {r.text}")
            log.error(
                "Could not retrieve available AI models from AI Core system! Exiting..."
            )
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        log.warning(str(e))
        log.error(f"No resources found with available models. {str(e)}. Exiting...")
        sys.exit(1)


# Create the configurations for the AI models in the AI Core system
def create_configuration(aiCoreMetadata: AiCoreMetadataDefinition) -> str:
    apiBase = aiCoreMetadata.apiBase
    token = aiCoreMetadata.apiAccessToken
    resourceGroup = aiCoreMetadata.resourceGroup

    configurationIDs = []

    # Create the URL to create the configuration
    aiCoreLocation = f"{apiBase}/v2/lm/configurations"
    # Create the headers for the request
    headers = {}
    headers["AI-Resource-Group"] = resourceGroup
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    if (
        aiCoreMetadata.availableModels is None
        or aiCoreMetadata.availableModels.get("resources") is None
        or len(aiCoreMetadata.availableModels["resources"]) == 0
    ):
        log.error("No available resources found! with available models. Exiting...")
        exit(1)

    # Loop through the available models and find the one that matches the target model
    for model in aiCoreMetadata.availableModels["resources"]:
        for parameter in model["parameters"]:
            supportedModels = get_supported_models(parameter)
            for targetAiCoreModel in aiCoreMetadata.targetAiCoreModel:
                if targetAiCoreModel in supportedModels:
                    data = {}
                    data["name"] = targetAiCoreModel + "-config"
                    data["executableId"] = model["id"]
                    data["scenarioId"] = model["scenarioId"]
                    data["versionId"] = model["versionId"]
                    data["parameterBindings"] = []
                    data["parameterBindings"].append(
                        {"key": "modelName", "value": targetAiCoreModel}
                    )

                    # Create the configuration in the AI Core system
                    try:
                        # Send the request to create the configuration
                        log.info(f"Creating configuration for '{targetAiCoreModel}'...")
                        r = requests.post(
                            url=aiCoreLocation, headers=headers, data=json.dumps(data)
                        )
                        if r.ok is True:
                            # Retrieve the configuration from the response
                            configuration = r.json()
                            configurationIDs.append(configuration["id"])
                        else:
                            log.info(
                                f"Response status code: {r.status_code} ({r.reason}): {r.text}"
                            )
                            log.error(
                                f"Could not create configuration for '{targetAiCoreModel}'! Exiting..."
                            )
                            sys.exit(1)
                    except requests.exceptions.RequestException as e:
                        log.warning(str(e))

    return configurationIDs


# Create the deployments for the AI models in the AI Core system
def create_deployments(aiCoreMetadata: AiCoreMetadataDefinition) -> list:
    final_deployments = []

    apiBase = aiCoreMetadata.apiBase
    token = aiCoreMetadata.apiAccessToken
    resourceGroup = aiCoreMetadata.resourceGroup

    # Create the URL to create the configuration
    aiCoreLocation = f"{apiBase}/v2/lm/deployments"
    # Create the headers for the request
    headers = {}
    headers["AI-Resource-Group"] = resourceGroup
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    deploymentIds = []

    for configurationId in aiCoreMetadata.configurationIds:
        data = {}

        data["configurationId"] = configurationId

        try:
            # Send the request to create the deployment
            log.info(f"Creating deployment for configuration '{configurationId}'...")
            r = requests.post(
                url=aiCoreLocation, headers=headers, data=json.dumps(data)
            )
            if r.ok is True:
                # Retrieve the configuration from the response
                deployment = r.json()
                deploymentIds.append(deployment["id"])
            else:
                log.info(
                    f"Response status code: {r.status_code} ({r.reason}): {r.text}"
                )
                log.error(
                    f"Could not create deployment for configuration '{configurationId}'! Exiting..."
                )
                sys.exit(1)
        except requests.exceptions.RequestException as e:
            log.warning(str(e))

    for deploymenId in deploymentIds:
        deploymentDetails = get_deployment_details(aiCoreMetadata, deploymenId)
        final_deployments.append(deploymentDetails)

    return final_deployments


# Retrieve the deployment details from the AI Core system metadata
def get_deployment_details(aiCoreMetadata: AiCoreMetadataDefinition, deploymenId: str):
    apiBase = aiCoreMetadata.apiBase
    token = aiCoreMetadata.apiAccessToken
    resourceGroup = aiCoreMetadata.resourceGroup

    # Create the URL to create the configuration
    aiCoreLocation = f"{apiBase}/v2/lm/deployments/{deploymenId}"
    # Create the headers for the request
    headers = {}
    headers["AI-Resource-Group"] = resourceGroup
    headers["Authorization"] = f"Bearer {token}"
    deploymentUrl = ""
    deploymentDetails = None

    while deploymentUrl == "":
        try:
            # Send the request to create the deployment
            log.info(f"Retrieving deployment details for id '{deploymenId}'...")
            r = requests.get(url=aiCoreLocation, headers=headers)
            if r.ok is True:
                # Retrieve the configuration from the response
                deploymentDetails = r.json()
                log.info(
                    f"waiting to get AI Core endpoint setup for '{deploymenId}' (trying every {str(RETRY_TIME_IN_SECONDS_AICORE_DEPLOYMENT_URL)} seconds) ..."
                )
                # print(f"waiting to get AI Core endpoint setup for '{deploymenId}' (trying every {str(RETRY_TIME_IN_SECONDS_AICORE_DEPLOYMENT_URL)} seconds) ...")
                time.sleep(RETRY_TIME_IN_SECONDS_AICORE_DEPLOYMENT_URL)
                deploymentUrl = deploymentDetails["deploymentUrl"]
            else:
                log.info(
                    f"Response status code: {r.status_code} ({r.reason}): {r.text}"
                )
                log.error(
                    f"Could not retrieve deployment details for id '{deploymenId}'! Exiting..."
                )
                sys.exit(1)

        except requests.exceptions.RequestException as e:
            log.warning(str(e))
            return None
    log.success(f"AI Core deployment id '{deploymenId}' is now accessible!")
    return deploymentDetails


# Extract the supported models from the parameters description
def get_supported_models(parameters: dict) -> list[str]:
    result = []

    if parameters.get("description") is not None:
        split = parameters["description"].split("supportedModels: ")
        if len(split) > 1:
            result = split[1].split(", ")

    return result
