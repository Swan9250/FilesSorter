import os
from app.views.Image import Image
from app.base.db.mysql.Database import Mysql
from app.api.ImageApiTranslator import ImageApiTranslator

home_dir = os.path.expanduser('~')
images_dir = home_dir + '/Изображения/'


class ImageSorter:
    DEFAULT_COMMENT = 'moved by sorter'

    def __init__(self, image: Image, path_to):
        self.translator = ImageApiTranslator()
        self.image = image
        self.path_to = path_to

    def run(self):
        absolute_path_to = images_dir + self.path_to + self.image.name
        try:
            if os.path.exists(absolute_path_to):
                return "File already exists"
            else:
                os.replace(self.image.path, absolute_path_to)
        except FileNotFoundError as e:
            os.makedirs(images_dir + self.path_to)
            os.replace(self.image.path, absolute_path_to)

        self.image.set_path(absolute_path_to)
        Mysql().add_image(self.image, self.DEFAULT_COMMENT)
        return self.translator.convert_to_json(self.image)
