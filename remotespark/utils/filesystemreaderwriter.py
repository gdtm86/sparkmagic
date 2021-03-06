# Copyright (c) 2015  aggftw@gmail.com
# Distributed under the terms of the Modified BSD License.
import os


class FileSystemReaderWriter(object):

    def __init__(self, path):
        from remotespark.utils.utils import expand_path
        assert path is not None
        self.path = expand_path(path)

    def ensure_path_exists(self):
        try:
            os.makedirs(self.path)
        except OSError:
            if not os.path.isdir(self.path):
                raise

    def ensure_file_exists(self):
        if not os.path.exists(self.path):
            open(self.path, 'w').close()

    def read_lines(self):
        if os.path.isfile(self.path):
            with open(self.path, "r+") as f:
                return f.readlines()
        else:
            return ""

    def overwrite_with_line(self, line):
        with open(self.path, "w+") as f:
            f.writelines(line)
