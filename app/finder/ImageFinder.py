import os

from typing import Optional

from app.base.db.mysql import Database
from app.views.Image import Image

image_types = ('.jpg', '.jpeg', '.gif', '.png', '.tiff', '.bmp', '.svg', '.ico', '.webp', '.eps')


class ImageFinder:

    def __init__(self):
        self.db = Database.Mysql()

    def run(self, image: Image) -> Optional[tuple]:
        return self.db.find_one(image.name)

