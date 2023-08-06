from app.views.BaseFile import BaseFile


class Image(BaseFile):
    TYPE = 'image'

    def __init__(self, file_id: int, name: str):
        super().__init__(file_id, name)
        self.file_type = self.TYPE
