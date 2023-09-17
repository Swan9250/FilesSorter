import argparse

from app.views.Image import Image
from app.sorter.ImageSorter import ImageSorter
from app.api.ImageApiTranslator import ImageApiTranslator
from app.logger.Logger import Logger


class SortAction:
    OPERATION = 'SortOne'

    def __init__(self):
        self.translator = ImageApiTranslator()
        self.logger = Logger(__name__, 'DEBUG').get_logger()
        self.parser = self.create_parser()

    def run(self):
        namespace = self.parser.parse_args()
        self.translator.set_operation(self.OPERATION).match_api()  # типа имитация запроса по api для будущего меня
        image = Image(namespace.path_from)
        return ImageSorter(image, namespace.path_to).run()

    @staticmethod
    def create_parser():
        parser_obj = argparse.ArgumentParser()
        parser_obj.add_argument('-pf', '--path-from', action='store', required=True)
        parser_obj.add_argument('-pt', '--path-to', action='store', required=True)
        return parser_obj


if __name__ == '__main__':
    print(SortAction().run())
