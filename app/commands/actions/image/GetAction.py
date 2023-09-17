import argparse
import json

from app.api.ImageApiTranslator import ImageApiTranslator
from app.getter.ImageGetter import ImageGetter
from app.logger.Logger import Logger


class GetAction:
    OPERATION = 'GetOne'

    def __init__(self):
        self.translator = ImageApiTranslator()
        self.logger = Logger(__name__, 'DEBUG').get_logger()
        self.parser = self.create_parser()

    def run(self):
        namespace = self.parser.parse_args()
        self.translator.set_operation(self.OPERATION).match_api()  # типа имитация запроса по api для будущего меня
        if namespace.recursive:
            return ImageGetter(namespace.recursive, namespace.max_depth).run()
        else:
            return ImageGetter().run()

    @staticmethod
    def create_parser():
        parser_obj = argparse.ArgumentParser()
        parser_obj.add_argument('-r', '--recursive', action='store_true')
        known, others = parser_obj.parse_known_args()
        if known.recursive is True:
            parser_obj.add_argument('--max-depth', action='store', required=True, type=int)
        return parser_obj


if __name__ == "__main__":
    print(json.loads(GetAction().run()).get('name'))
