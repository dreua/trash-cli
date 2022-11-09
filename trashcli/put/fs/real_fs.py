import os
import stat

from trashcli import fs
from trashcli.fs import write_file
from trashcli.put.fs.dir_scanner import DirScanner
from trashcli.put.fs.fs import Fs
from six.moves import map as imap

class RealFs(Fs):

    def atomic_write(self, path, content):
        fs.atomic_write(path, content)

    def chmod(self, path, mode):
        os.chmod(path, mode)

    def isdir(self, path):
        return os.path.isdir(path)

    def isfile(self, path):
        return os.path.isfile(path)

    def getsize(self, path):
        return os.path.getsize(path)

    def get_size_recursive(self, path):
        if os.path.isfile(path):
            return os.path.getsize(path)

        files = DirScanner().list_all_files(path)
        files_sizes = imap(os.path.getsize, files)
        return sum(files_sizes, 0)

    def exists(self, path):
        return os.path.exists(path)

    def makedirs(self, path, mode):
        os.makedirs(path, mode)

    def move(self, path, dest):
        return fs.move(path, dest)

    def remove_file(self, path):
        fs.remove_file(path)

    def islink(self, path):
        return os.path.islink(path)

    def has_sticky_bit(self, path):
        return (os.stat(path).st_mode & stat.S_ISVTX) == stat.S_ISVTX

    def realpath(self, path):
        return os.path.realpath(path)

    def is_accessible(self, path):
        return os.access(path, os.F_OK)

    def make_file(self, path, content):
        write_file(path, content)

    def get_mod(self, path):
        return stat.S_IMODE(os.lstat(path).st_mode)
