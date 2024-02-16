from pathlib import Path

ROOT = Path(__file__, "..", "..", "..", "..").resolve()

# Folders
FOLDER_SECRETS = Path(ROOT, "config", "secrets")

# Files
FILE_METADATA_AI_CORE_KEY = Path(
    FOLDER_SECRETS, "my_metadata_ai_core_key.json"
).resolve()

FILE_ENV = Path(FOLDER_SECRETS, ".env").resolve()
