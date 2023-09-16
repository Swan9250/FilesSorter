import json
from types import SimpleNamespace
from typing import Optional
from app.views.BaseFile import BaseFile


class BaseApiTranslator:
    TYPE_JSON = 'json'
    TYPE_HTTP = 'http'
    TYPE_GRPC = 'grpc'

    def __init__(self):
        self.operation = None
        self.request = None
        self.response = None

    def match_type(self, api_type: str):
        match api_type:
            case self.TYPE_JSON:
                pass

    def set_operation(self, operation: str):
        self.operation = operation
        return self

    @staticmethod
    def convert_from_json(request: json) -> Optional[BaseFile]:
        info = json.loads(request)
        if 'id' in info.keys() and info.get('id') != 0:
            file = BaseFile(file_id=info.get('id'))
        elif 'name' in info.keys() and info.get('name') != "":
            file = BaseFile(name=info.get('name'))
        else:
            return
        return file

    @staticmethod
    def convert_to_json(file: BaseFile) -> json:
        return json.dumps(file, default=lambda o: o.__dict__)
