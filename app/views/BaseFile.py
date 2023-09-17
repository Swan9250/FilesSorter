import os
from datetime import datetime


class BaseFile:

    def __init__(self, path):
        self.id = None
        self.file_type = None
        self.path = path
        if self.path != "" and self.path is not None and os.path.exists(self.path):
            self.name = self.path.rpartition('/')[2]
            self.size = self.size_format(os.path.getsize(self.path))
            self.created = datetime.fromtimestamp(os.path.getctime(self.path)).strftime('%Y-%m-%d %H:%M:%S')
            self.last_modified = datetime.fromtimestamp(os.path.getmtime(self.path)).strftime('%Y-%m-%d %H:%M:%S')
        else:
            self.name = None
            self.size = None
            self.created = None
            self.last_modified = None

    def set_id(self, file_id):
        self.id = file_id

    def set_path(self, path: str):
        self.path = path
        return self

    def set_type(self, file_type: str):
        self.file_type = file_type
        return self

    def set_size(self, file_size: str):
        self.size = file_size
        return self

    def set_created(self, file_created: str):
        self.created = file_created
        return self

    def set_last_modified(self, file_last_modified: str):
        self.last_modified = file_last_modified
        return self

    @staticmethod
    def size_format(size: int):
        if size is not None:
            if size >= 1024 * 1024 * 1024:
                size = f"{size / 1024 / 1024 / 1024} GB"
                return size
            elif size >= 1024 * 1024:
                size = f"{size / 1024 / 1024} MB"
                return size
            elif size >= 1024:
                size = f"{size / 1024} KB"
                return size
            else:
                return f"{size} B"
        else:
            return "Size is None"





