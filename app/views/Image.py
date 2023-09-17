from app.views.BaseFile import BaseFile


class Image(BaseFile):
    TYPE = 'image'

    def __init__(self, path: str):
        super().__init__(path)
        self.file_type = self.TYPE
