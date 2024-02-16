from library.util.io import write_file
from library.constants.folders import FILE_METADATA_AI_CORE_KEY

from library.model.aicore import AiCoreMetadataJsonEncoder
from library.fetch.aicore import AiCoreMetadata
from library.util.logging import initLogger
from pathlib import Path
import logging
import json
from dotenv import load_dotenv

log = logging.getLogger(__name__)
initLogger()


# Main function
def main():
    log.header("Preparing the environment for the AI Core and HANA Cloud system.")

    load_dotenv()

    # Extract the metadata for the AI Core system from the terraform state file
    ai_core_metadata = AiCoreMetadata()
    write_file(
        Path(FILE_METADATA_AI_CORE_KEY),
        json.dumps(ai_core_metadata, indent=2, cls=AiCoreMetadataJsonEncoder),
    )


if __name__ == "__main__":
    main()
