#!/usr/bin/env python
#coding: utf-8

import os

from hashlib  import sha224
from datetime import datetime
from psdwatcher.util import Logger
from psdwatcher.git  import git
from psdwatcher.config import DEFAULT_COMMIT_AUTHOR

class ModificationWatcher(object):

    def __init__(self, watch_file):

        self.target = watch_file
        self.target_dir = os.path.dirname(self.target)

        self.target_modified_time = self.get_mtime(self.target)
        self.target_file_hash = self.get_sha224_hash(self.target)

    def watch(self, dev=False):
        # comment rule:
        #   - Comment must write with index.
        #   - Append new line under and over comment.
        #   - Comment must finish with period.
        #   - First letter of comment is must upper.

        if dev:
            Logger.info("Watching '{0}'".format(self.target))

        # 1. Find the file modification.

        # 1-1. Get new mtime and hash.

        new_modified_time = self.get_mtime(self.target)
        new_file_hash = self.get_sha224_hash(self.target)

        if dev:
            Logger.debug("1. Got a file timestamp")
            Logger.debug("\tOld mtime: {0}".format(self.strmtime(self.target_modified_time)))
            Logger.debug("\tNew mtime: {0}".format(self.strmtime(new_modified_time)))

            Logger.debug("2. Got a file hash")
            Logger.debug("\tOld hash: {0}".format(new_file_hash[0:15]))
            Logger.debug("\tNew hash: {0}".format(self.target_file_hash[0:15]))

        # 1-2. Compare variables.

        if self.target_file_hash != new_file_hash \
            and self.target_modified_time != new_modified_time:

            Logger.info("Catch the file modify!")

        else:

            # 1-2-1: when not found modification, break func.

            if dev:
                Logger.info("PSDwatcher can't catch modify.")

            return

        # 2. when found modify, git operation start.

        # 2-1. Move current dir to target directory.

        os.chdir(self.target_dir)

        if dev:
            Logger.info("Move target directory: '{0}'".format(self.target_dir))

        # 2-2. Check the current dir is isnide git work tree.

        if git.is_inside_work_tree() is not True:

            if dev:
                Logger.warn("This directory is not git work tree.")
                Logger.info("Execute 'git init .'")

            # ==== UNDER DEVELOPEMNT ====
            # git.init()
            # ===========================

        # 2-3. Execute 'add' command

        # ==== UNDER DEVELOPEMNT ====
        # git.add(self.target)
        # ===========================

        if dev:
            Logger.info("Staged '{0}' to git.".format(self.target)

        # 2-4. Execute 'commit' command

        msg = "This commit was written by PSDwatcher\n\n" \
               "TARGET FILE: '{0}'\n".format(self.target) \
               "  FILE HASH: '{1}'\n".format(new_file_hash) \
               "MODIFIED AT: '{2}'\n".format(self.strmtime(new_modified_time))

        # ==== UNDER DEVELOPEMNT ====
        # git.commit(msg, author= \
        #       DEFAULT_COMMIT_AUTHOR)
        # ===========================

        # 3. Update file data from old to new.

        self.target_modified_time = new_modified_time
        self.target_file_hash = new_file_hash

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


