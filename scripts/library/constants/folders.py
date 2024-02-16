from pathlib import Path

ROOT = Path(__file__, "..", "..", "..").resolve()

# Folders
FOLDER_SECRETS = Path(ROOT, "config", "secrets")

# Files
FILE_METADATA_AI_CORE_KEY = Path(
    FOLDER_SECRETS, "my_metadata_ai_core_key.json"
).resolve()

FILE_METADATA_HANA_CLOUD = Path(FOLDER_SECRETS, "metadata_hana_cloud.json").resolve()

FILE_AI_CODE_CREDENTIALS = Path(FOLDER_SECRETS, "metadata_ai_core_key.json").resolve()

FILE_ENV_VARIABLES_USE = Path(ROOT, "scripts" ".env").resolve()
