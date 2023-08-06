import json
from ApiBuilder import ApiBuilder


class GetOneRequest(ApiBuilder):
    REQUEST = 'GetOneRequest'

    def __init_(self):
        super().__init__()

        self.id = None
        self.name = None
        self.file_type = None
        self.path = None
        self.size = None
        self.created = None
        self.last_modified = None

    def convert_to_attributes(self):
        with open('Api.json', 'r') as api_file:
            api: dict
            api = json.loads(api_file.read())
            operation = api.get(self.operation)
            request = operation.get(self.REQUEST)

            if 'id' in request.keys() and request.get('id') != 0:
                self.id = request.get('id')
            if 'name' in request.keys() and request.get('name') != "":
                self.name = request.get('name')
        return self

    def convert_to_json(self):
        pass
