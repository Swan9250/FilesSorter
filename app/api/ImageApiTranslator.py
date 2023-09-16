import json

from app.api.BaseApiTranslator import BaseApiTranslator
from app.views.Image import Image


class ImageApiTranslator(BaseApiTranslator):

    def __init__(self):
        super().__init__()

    def match_api(self):
        with open('/root/projects/FilesSorter/app/api/ImageApi.json', 'r') as api_template:
            api = json.loads(api_template.read())
            match self.operation:
                case 'FindOne':
                    self.request = api.get('FindOne').get('FindOneRequest')
                    self.response = api.get('FindOne').get('FindOneResponse')
                case 'GetOne':
                    self.request = api.get('GetOne').get('GetOneRequest')
                    self.response = api.get('GetOne').get('GetOneResponse')
                case 'SortOne':
                    self.request = api.get('SortOne').get('SortOneRequest')
                    self.response = api.get('SortOne').get('SortOneResponse')
                case _:
                    self.request = {}
                    self.response = {}

