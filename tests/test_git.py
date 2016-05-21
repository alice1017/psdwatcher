#!/usr/bin/env python
#coding: utf-8

import os
import sys
import tempfile
import unittest

from StringIO import StringIO
from psdwatcher.git    import git, GitError
from psdwatcher.config import DEFAULT_COMMIT_AUTHOR

class GitOperatorTester(unittest.TestCase):

    def setUp(self):

        sys.stdout = StringIO()
        self.cwd = os.getcwd()
        self.tmpdir = tempfile.mkdtemp()
        os.chdir(self.tmpdir)

    def tearDown(self):

        sys.stdout = sys.__stdout__
        os.chdir(self.cwd)

    def test_exec(self):

        # 1. normal
        out = git._exec("init")
        msg = "Initialized empty Git " \
              "repository in {0}".format(
                  os.path.abspath(os.path.join(self.tmpdir, ".git")
                  ).replace("var/","private/var/") + "/"
                )
        self.assertEqual( out, msg )

        # 2. raise ValueError
        with self.assertRaises(ValueError):
            git._exec("init",stdout="a")
        with self.assertRaises(ValueError):
            git._exec("init",stdin="a")
        with self.assertRaises(ValueError):
            git._exec("init",stderr="a")
        with self.assertRaises(GitError):
            print git._exec("chekcout", "branch")

    def test_add_and_commit(self):

        tmpfile = open("tmpfile","w")

        git._exec("init")
        git.add("tmpfile")
        result = git._exec("status", "-s")

        self.assertEqual(result, "A  tmpfile")

        msg = "test commit"
        result = git.commit(msg, author=DEFAULT_COMMIT_AUTHOR)
        self.assertTrue(
            result.split("\n")[0].endswith(msg)
        )

    def test_is_inside_work_tree(self):

        git._exec("init")
        self.assertTrue(
            git.is_inside_work_tree()
        )
