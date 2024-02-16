from dataclasses import dataclass
from library.model.aicore import AiCoreMetadata as AiCoreMetadataDefinition
from library.util.aicore import (
    get_api_access_token,
    get_available_ai_models,
    create_configuration,
    create_deployments,
)
import logging
import os

log = logging.getLogger(__name__)


@dataclass
class AiCoreMetadata(AiCoreMetadataDefinition):
    def __init__(self):
        self.authUrl = os.environ.get("AICORE_LLM_AUTH_URL")
        self.clientId = os.environ.get("AICORE_LLM_CLIENT_ID")
        self.clientSecret = os.environ.get("AICORE_LLM_CLIENT_SECRET")
        self.resourceGroup = os.environ.get("AICORE_LLM_RESOURCE_GROUP")
        self.apiBase = os.environ.get("AICORE_LLM_API_BASE")
        self.targetAiCoreModel = ["gpt-35-turbo", "text-embedding-ada-002"]

        self.apiAccessToken = get_api_access_token(self)
        self.availableModels = get_available_ai_models(self)

        self.configurationIds = create_configuration(self)
        self.deployment = create_deployments(self)
