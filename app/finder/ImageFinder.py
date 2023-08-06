import argparse
import os
from app.views.Image import Image
from app.logger.Logger import Logger

home_dir = os.path.expanduser('~')

image_types = ('.jpg', '.jpeg', '.gif', '.png')


class ImageFinder:

    def __init__(self):
        self.images = []
        self.logger = Logger(__name__, 'DEBUG').get_logger()
        self.command_line_args = None

    def run(self):
        os.chdir(home_dir)
        self.logger.info(f"Меняем директорию: {os.getcwd()}")
        parser = self.create_parser()
        namespace = parser.parse_args(self.command_line_args)
        current_dir = home_dir
        if namespace.recursive:
            self.logger.info('recursive mod')
            image_files = self.search_recursion(namespace.max_depth, [current_dir])
        else:
            self.logger.info('default mode')
            image_files = self.search_recursion(0, [current_dir])
        return self.make_image_objects(image_files)

    def create_parser(self):
        parser_obj = argparse.ArgumentParser()
        parser_obj.add_argument('-r', '--recursive', action='store_true')
        known, others = parser_obj.parse_known_args(self.command_line_args)

        if known.recursive is True:
            parser_obj.add_argument('--max-depth', action='store', required=True, type=int)
        return parser_obj

    def search_recursion(self, max_depth=0, dirs_list=None, find_images=None):
        new_dirs_list = []
        if find_images is None:
            find_images = []
        for new_dir in dirs_list:
            new_dirs_list.extend([directory for directory in os.scandir(new_dir) if directory.is_dir()])
            find_images.extend([file for file in os.scandir(new_dir) if file.path.endswith(image_types)])
        if max_depth == 0:
            return find_images
        else:
            max_depth -= 1
        return self.search_recursion(max_depth, new_dirs_list, find_images)

    def make_image_objects(self, image_files: list):
        for file in image_files:
            image = Image(0, file.name).set_path(file.path)
            self.images.append(image)
        for img in self.images:
            self.logger.info(img.path)
        return self.images


if __name__ == '__main__':
    ImageFinder().run()

