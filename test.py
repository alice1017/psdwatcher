#!/usr/bin/env python
#coding: utf-8

import os

from unittest import loader, TextTestRunner

test_path = os.path.join(os.path.dirname(__file__), 'tests')
test_loader = loader.TestLoader()

if __name__ == "__main__":

    runner = TextTestRunner(verbosity=2)
    runner.run(test_loader.discover(test_path))
