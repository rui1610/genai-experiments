from dataclasses import dataclass
from json import JSONEncoder


class HanaCloudMetadataJsonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


@dataclass
class HanaCloudMetadata:
    address: str
    port: str
    user: str
    password: str

    def __getitem__(self, item):
        return getattr(self, item)
