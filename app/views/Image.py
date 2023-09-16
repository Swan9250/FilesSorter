from app.views.BaseFile import BaseFile


class Image(BaseFile):
    TYPE = 'image'

    def __init__(self, name: str):
        super().__init__(name=name)
        self.file_type = self.TYPE
