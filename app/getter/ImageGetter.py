import os
import random
import posix

from app.views.Image import Image
from app.api.BaseApiTranslator import BaseApiTranslator
from app.logger.Logger import Logger
from app.base.db.mysql.Database import Mysql

home_dir = os.path.expanduser('~')
images_dir = home_dir + '/Изображения'
image_types = ('.jpg', '.jpeg', '.gif', '.png', '.tiff', '.bmp', '.svg', '.ico', '.webp', '.eps')


class ImageGetter:

    def __init__(self, recursive=False, max_depth=0):
        self.images = []
        self.recursive = recursive
        self.max_depth = max_depth
        self.logger = Logger(__name__, "DEBUG").get_logger()

    def run(self):
        image_list = self.search()
        if len(image_list) > 1:
            for ima in image_list:
                print(ima.path)
            your = image_list[random.randrange(0, len(image_list), 1)]  # Функция randrange(start, stop, width) не
            # включает параметр конца при генерации случайного целого числа. Параметр stop является эксклюзивным и не
            # генерируется случайным числом.
        elif len(image_list) == 1:
            your = image_list[0]
        else:
            your = None
        your_json = BaseApiTranslator().convert_to_json(your)
        # print(your.path)
        return your_json

    def search(self):
        os.chdir(home_dir)
        self.logger.info(f"Меняем директорию: {os.getcwd()}")
        current_dir = home_dir
        if self.recursive:
            self.logger.info('recursive mod')
        else:
            self.logger.info('default mode')
        image_files = self.search_recursion([current_dir])
        return self.make_image_objects(image_files)

    def search_recursion(self, dirs_list=None, find_images=None):
        new_dirs_list = []
        if find_images is None:
            find_images = []
        for new_dir in dirs_list:
            if images_dir == new_dir:
                continue
            if isinstance(new_dir, posix.DirEntry):
                if images_dir == new_dir.path:
                    continue
            new_dirs_list.extend([directory for directory in os.scandir(new_dir) if directory.is_dir()])
            find_images.extend([file for file in os.scandir(new_dir) if file.path.endswith(image_types)])
        for image in find_images:
            if self.already_in_db(image):
                find_images.pop(find_images.index(image))
        if self.max_depth == 0:
            return find_images
        else:
            self.max_depth -= 1
        return self.search_recursion(new_dirs_list, find_images)

    def make_image_objects(self, image_files: list):
        for file in image_files:
            image = Image(file.path)
            self.images.append(image)
        for img in self.images:
            self.logger.info(img.path)
        return self.images

    def already_in_db(self, image: posix.DirEntry) -> bool:
        file_in_base = Mysql().find_one(image.path)
        if file_in_base:
            return True
        else:
            self.logger.info(
                f"File {image.path} not found in database"
            )
        return False


if __name__ == '__main__':
    ImageGetter(True, 5).run()
