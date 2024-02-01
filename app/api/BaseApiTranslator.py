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

    # def match_type(self, api_type: str):
    #     match api_type:
    #         case self.TYPE_JSON:
    #             return self.convert_from_json()

    def set_operation(self, operation: str):
        self.operation = operation
        return self

    @staticmethod
    def convert_from_json(request: json) -> Optional[BaseFile]:
        info = json.loads(request)
        if 'path' in info.keys() and info.get('path') != "":
            file = BaseFile(path=info.get('path'))
        else:
            return info
        return file

    @staticmethod
    def convert_to_json(file: BaseFile) -> json:
        return json.dumps(file, default=lambda o: o.__dict__)

