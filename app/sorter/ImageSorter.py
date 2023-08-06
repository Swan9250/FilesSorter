import os
from app.views.Image import Image

home_dir = os.path.expanduser('~')
images_dir = home_dir + '/Изображения/'


class ImageSorter:

    def __init__(self, image: Image):
        self.image = image

    def run(self):
        pass


