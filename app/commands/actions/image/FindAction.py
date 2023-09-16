import argparse

from typing import Optional

from app.api.ImageApiTranslator import ImageApiTranslator
from app.logger.Logger import Logger
from app.finder.ImageFinder import ImageFinder
from app.views.Image import Image


class FindAction:
    OPERATION = 'FindOne'

    def __init__(self):
        self.translator = ImageApiTranslator()
        self.logger = Logger(__name__, 'DEBUG').get_logger()
        self.parser = self.create_parser()

    def run(self) -> Optional[tuple]:
        namespace = self.parser.parse_args()
        self.translator.set_operation(self.OPERATION).match_api()  # типа имитация запроса по api
        self.translator.request['name'] = namespace.name
        image_object = Image(self.translator.request['name'])
        return ImageFinder().run(image_object)

    @staticmethod
    def create_parser():
        parser_obj = argparse.ArgumentParser()
        parser_obj.add_argument('--name', action='store', required=True)
        return parser_obj


if __name__ == "__main__":
    print(FindAction().run())
