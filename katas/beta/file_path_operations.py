import os.path


class FileMaster(object):
    def __init__(self, file_path):
        self.dir_path = os.path.dirname(file_path) + '/'
        self.file_name, self.file_ext = os.path.basename(file_path).split('.')

    def dirpath(self):
        return self.dir_path

    def extension(self):
        return self.file_ext

    def filename(self):
        return self.file_name
