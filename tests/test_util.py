#!/usr/bin/env python
#coding: utf-8

import sys
import logging
import unittest

from StringIO        import StringIO
from psdwatcher.util import Logger

class LoggerTester(unittest.TestCase):

    def setUp(self):

        self.logger = Logger
        self.stream = StringIO()

        self.handler = logging.StreamHandler(self.stream)

        self.logger.removeHandler(logging.StreamHandler())
        self.logger.addHandler(self.handler)

        self.header = "[ {:^7} ] "

    def tearDown(self):

        pass

    def test_debug(self):
        
        name = "debug"
        self.logger.debug(name)

        self.assertEqual(
            self.stream.getvalue().strip(),
            self.header.format(name.upper())+name
        )

    def test_info(self):

        name = "info"
        self.logger.info(name)

        self.assertEqual(
            self.stream.getvalue().strip(),
            self.header.format(name.upper())+name
        )

    def test_warning(self):

        name = "warning"
        self.logger.warning(name)

        self.assertEqual(
            self.stream.getvalue().strip(),
            self.header.format(name.upper())+name
        )

    def test_error(self):

        name = "error"
        self.logger.error(name)

        self.assertEqual(
            self.stream.getvalue().strip(),
            self.header.format(name.upper())+name
        )

    def test_critical(self):

        name = "critical"
        self.logger.critical(name)

        self.assertEqual(
            self.stream.getvalue().strip(),
            self.header.format(name.upper())+name
        )


