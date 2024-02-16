from dataclasses import dataclass
from library.model.hanacloud import HanaCloudMetadata as HanaCloudMetadataDefinition
import json
from library.constants.folders import FILE_METADATA_HANA_CLOUD
from util.io import read_json_file
import logging

log = logging.getLogger(__name__)


@dataclass
class HanaCloudMetadata(HanaCloudMetadataDefinition):
    def __init__(self, raw):
        # get the content from the file FILE_METADATA_HANA_CLOUD
        file = read_json_file(FILE_METADATA_HANA_CLOUD)

        # decode the json from the terraform state file
        raw_json = json.loads(raw)
        if (
            raw_json.get("outputs") is None
            or raw_json["outputs"].get("HANA_DB_ADDRESS") is None
            or raw_json["outputs"]["HANA_DB_ADDRESS"].get("value") is None
            or raw_json["outputs"].get("HANA_DB_PORT") is None
            or raw_json["outputs"]["HANA_DB_PORT"].get("value") is None
            or raw_json["outputs"].get("HANA_DB_USER") is None
            or raw_json["outputs"]["HANA_DB_USER"].get("value") is None
            or raw_json["outputs"].get("HANA_DB_PASSWORD") is None
            or raw_json["outputs"]["HANA_DB_PASSWORD"].get("value") is None
        ):
            log.error(
                "Terraform state file does not contain the HANA Cloud metadata. Exiting."
            )
            return None
        output = raw_json["outputs"]

        try:
            self.address = set_env_var(file, output, "address", "HANA_DB_ADDRESS")
            self.port = set_env_var(file, output, "port", "HANA_DB_PORT")
            self.user = set_env_var(file, output, "user", "HANA_DB_USER")
            self.password = set_env_var(file, output, "password", "HANA_DB_PASSWORD")
        except Exception as e:
            log.warning(
                "Error while setting the HANA Cloud metadata. All metadata will be set to None. Error: "
                + str(e)
            )
            self.address = None
            self.port = None
            self.user = None
            self.password = None


def set_env_var(file: str, output: str, attribute_name: str, env_name: str) -> str:
    result = None

    # If the attribute_name is already set in the env file, use the attribute_name from the env file
    if file is not None:
        field = file.get(attribute_name)
        if field is not None and field != "":
            env_name = field
            log.debug(
                f"{attribute_name} is already set in the env file. Using the apiBase from the env file."
            )
            return

    result = output[env_name]["value"]

    return result
