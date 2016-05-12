#!/usr/bin/env python
#coding: utf-8

import os
import unittest
import tempfile
import cPickle as pickle

from psdwatcher.config import FileContainer


class ContainerTester(unittest.TestCase):

    def setUp(self):

        self.container_file = os.path.join(tempfile.mkdtemp(), "psdwatcher.rc.tmp")

    def _make_tmp_psdfile(self, file_name="tmp.psd", counterfeit=False):
        #counterfeit -> 偽造する

        tmpdir = tempfile.mkdtemp()
        tmpfile_path = os.path.abspath(os.path.join(tmpdir,file_name))

        if counterfeit is False:

            with open(tmpfile_path,"w") as fp:
                fp.write("8BPS")

        else:
            
            with open(tmpfile_path,"w") as fp:
                fp.write("")

        return tmpfile_path

    def test_make_tmp_psdfile(self):

        # 1. check file name
        tmp_psdfile1 = self._make_tmp_psdfile()
        self.assertEqual(
            tmp_psdfile1.split("/")[-1], "tmp.psd")

        tmp_psdfile2 = self._make_tmp_psdfile(file_name="tmp")
        self.assertEqual(
            tmp_psdfile2.split("/")[-1], "tmp")


        # 2. check file content
        tmp_psdfile3 = self._make_tmp_psdfile()
        with open(tmp_psdfile3, "r") as fp:
            self.assertEqual(
                fp.read(), "8BPS")

        tmp_psdfile4 = self._make_tmp_psdfile(counterfeit=True)
        with open(tmp_psdfile4, "r") as fp:
            self.assertEqual(
                fp.read(), "")

    def test_is_psd(self):

        # 1. all right
        tmp_psdfile1 = self._make_tmp_psdfile()
        container1 = FileContainer(container_file=self.container_file)
        self.assertTrue(
            container1._is_psd(tmp_psdfile1))

        # 2. wrong file name
        tmp_psdfile2 = self._make_tmp_psdfile(file_name="tmp")
        container2 = FileContainer(container_file=self.container_file)
        self.assertFalse(
            container2._is_psd(tmp_psdfile2))

        # 3. wrong file content
        tmp_psdfile3 = self._make_tmp_psdfile(counterfeit=True)
        container3 = FileContainer(container_file=self.container_file)
        self.assertFalse(
            container3._is_psd(tmp_psdfile3))

        # 4. all wrong
        tmp_psdfile4 = self._make_tmp_psdfile(file_name="tmp",
                                                counterfeit=True)
        container4 = FileContainer(container_file=self.container_file)
        self.assertFalse(
            container4._is_psd(tmp_psdfile4))

    def test_add_file(self):

        tmp_psdfile = self._make_tmp_psdfile()
        container = FileContainer(container_file=self.container_file)
        self.assertTrue(
            container.add_file(tmp_psdfile))

    def test_get_container(self):

        tmp_psdfile = self._make_tmp_psdfile()
        container = FileContainer(container_file=self.container_file)
        container.add_file(tmp_psdfile)
        loaded_container = container._get_container()
        self.assertEqual(
            loaded_container,
            [tmp_psdfile]
        )

