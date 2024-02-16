from constants.folders import (
    FILE_METADATA_AI_CORE_KEY,
    FILE_METADATA_HANA_CLOUD,
    FILE_ENV_VARIABLES_USE,
)
from pathlib import Path
import logging
import json

log = logging.getLogger(__name__)


# Read file and return content
def read_file(file_path: Path):
    try:
        with open(file_path, "r") as file:
            filedata = file.read()
        return filedata
    except IOError:
        log.warning("Can't open file >" + str(file_path) + "<")
        return None


# Get json file content
def read_json_file(file_path):
    try:
        # Opening JSON file
        f = open(file_path)
        # returns JSON object as a dictionary
        data = json.load(f)
        return data
    except IOError:
        log.warning("Can't open json file >" + str(file_path) + "<")
        return None


# Write variable content to file
def write_file(file_path, content):
    try:
        # create any folder recirsively if not exists
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)

        # Writing to file
        f = open(file_path, "w")
        f.write(content)
        f.close()
        log.info("File written >" + str(file_path) + "<")
    except IOError:
        log.warning("Can't write to file >" + str(file_path) + "<")
        return None


# function to fetch all files in a folder with a glob pattern recursively
def get_files_in_folder(folder, glob_pattern):
    files = []
    for path in Path(folder).rglob(glob_pattern):
        files.append(path)
    return files


#  Store the AI Core and HANA Cloud metadata into an env file
def write_parameters_to_env_file():
    # Store the AI Core credentials into the environment

    ai_core_metadata = read_json_file(FILE_METADATA_AI_CORE_KEY)
    hana_cloud_metadata = read_json_file(FILE_METADATA_HANA_CLOUD)

    environmentString = ""

    # Store the AI Core credentials into the environment
    if ai_core_metadata is None or len(ai_core_metadata) == 0:
        log.error(
            "Missing metadata for AI Core service. Issue during infrastructure setup?"
        )
    else:
        environmentString += f"AICORE_LLM_AUTH_URL={ai_core_metadata['authUrl']}\n"
        environmentString += f"AICORE_LLM_CLIENT_ID={ai_core_metadata['clientId']}\n"
        environmentString += (
            f"AICORE_LLM_CLIENT_SECRET={ai_core_metadata['clientSecret']}\n"
        )
        environmentString += (
            f"AICORE_LLM_RESOURCE_GROUP={ai_core_metadata['resourceGroup']}\n"
        )
        environmentString += f"AICORE_LLM_API_BASE={ai_core_metadata['apiBase']}\n"
        write_file(str(FILE_ENV_VARIABLES_USE), environmentString)

    # Store the HANA Cloud credentials into the environment
    if hana_cloud_metadata is None or len(hana_cloud_metadata) == 0:
        log.error(
            "Missing metadata for HANA Cloud service. Issue during infrastructure setup?"
        )
    else:
        environmentString += f"HANA_DB_ADDRESS={hana_cloud_metadata['address']}\n"
        environmentString += f"HANA_DB_PORT={hana_cloud_metadata['port']}\n"
        environmentString += f"HANA_DB_USER={hana_cloud_metadata['user']}\n"
        environmentString += f"HANA_DB_PASSWORD={hana_cloud_metadata['password']}\n"
        write_file(str(FILE_ENV_VARIABLES_USE), environmentString)
