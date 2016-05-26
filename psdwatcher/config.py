#!/usr/bin/env python
# coding: utf-8

import os

import cPickle as pickle

DEFAULT_CONTAINER_FILE = str(os.environ.get(
    'PSDWATCHER_CONTAINER_FILE',
    os.path.expanduser('~/.psdwatcher')
))

DEFAULT_COMMIT_AUTHOR = str(os.environ.get(
    'PSDWATCHER_COMMIT_AUTHOR',
    'psdwatcher <https://github.com/alice1017/psdwatcher/>'
))


class FileContainer(object):

    def __init__(self, container_file=DEFAULT_CONTAINER_FILE):

        self.container_file = container_file
        self.container = self._get_container()

    def add_file(self, file_name):

        file_path = os.path.abspath(os.path.join(
            os.getcwd(),
            file_name
        ))

        is_psd = self._is_psd(file_name)

        if is_psd is not True:
            raise IOError(
                "'{0}' is not PSD.".format(file_name)
            )

        if file_path not in self.container:
            self.container.append(file_path)

        else:
            raise IOError(
                "'{0}' is duplicated.".format(file_name)
            )

        self.save()

        return True

    def release(self):

        if len(self.container) == 0:
            raise IndexError(
                "PSDwatcher doesn't have a PSD file. "
                "Please use 'add' command at first."
            )

        return self.container

    def save(self):

        pickle.dump(self.container, open(self.container_file, "w"))

    def load(self):

        return pickle.load(open(self.container_file, "r"))

    def _is_exist_container_file(self):

        if os.access(self.container_file, os.F_OK) is True:
            return True
        else:
            return False

    def _get_container(self):

        if self._is_exist_container_file() is True:
            return self.load()
        else:
            return []

    def _get_ext(self, file_name):

        return os.path.splitext(file_name)[-1]

    def _is_psd(self, file_name):

        if os.access(file_name, os.F_OK) is True:

            raw_bin = open(file_name, "r").read()

            if self._get_ext(file_name) == ".psd" \
               and raw_bin[0:4] == "8BPS":

                return True
            else:

                return False

        else:
            raise IOError(
                "'{0}' file doesn't found.".format(file_name)
            )
