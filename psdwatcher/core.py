#!/usr/bin/env python
#coding: utf-8

import os

from hashlib  import sha224
from datetime import datetime
from psdwatcher.util import Logger
from psdwatcher.git  import git

class ModificationWatcher(object):

    def __init__(self, watch_file):

        self.target = watch_file
        self.target_dir = os.path.dirname(self.target)

        self.target_modified_time = self.get_mtime(self.target)
        self.target_file_hash = self.get_sha224_hash(self.target)

    def watch(self, dev=False):

        Logger.info("Watch start.")

        if dev:
            Logger.debug("target: '{0}'".format(self.target))

        # 1. find modify

        # 1-1. get new modified time and hash
        new_modified_time = self.get_mtime(self.target)
        new_file_hash = self.get_sha224_hash(self.target)

        if dev:
            Logger.debug("1-1. Got a timestamp")
            Logger.debug("\tOld mtime: {0}".format(
                self.strmtime(self.target_modified_time)))
            Logger.debug("\tNew mtime: {0}".format(
                self.strmtime(new_modified_time)))
            Logger.debug("1-2. Got a file hash")
            Logger.debug("\tOld hash: {0}".format(new_file_hash[0:15]))
            Logger.debug("\tNew hash: {0}".format(self.target_file_hash[0:15]))

        # 1-2. compare

        raise Exception # under development

        # 2. when found modify, git operation start.

        if dev:
            Logger.info("Move target directory: '{0}'".format(self.target_dir))

        os.chdir(self.target_dir)

        if git.is_inside_work_tree() is not True:

            if dev:
                Logger.warn("This directory is not git work tree.")
                Logger.info("Execute 'git init .'")

            # git.init()

    def get_mtime(self, file):

        return os.stat(file).st_mtime

    def get_sha224_hash(self, file):

        with open(file,"rb") as fp:
            return sha224(fp.read()).hexdigest()

    def to_datetime(self, mtime):

        return datetime.fromtimestamp(mtime)

    def strmtime(self, mtime):

        dt = self.to_datetime(mtime)
        return dt.strftime("%Y-%m-%d %H:%M:%S")


