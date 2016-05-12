#!/usr/bin/env python
#coding: utf-8

import os

from unittest import TextTestRunner

try:
    from unittest import loader
except ImportError:
    from unittest2 import loader

test_path = os.path.join(os.path.dirname(__file__), 'tests')
test_loader = loader.TestLoader()

TextTestRunner(verbosity=2).run(test_loader.discover(test_path))
