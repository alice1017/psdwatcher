#!/usr/bin/env python
#coding: utf-8

import os
import sys

from unittest import loader, TextTestRunner

test_path = os.path.join(os.path.dirname(__file__), 'tests')
test_loader = loader.TestLoader()

if __name__ == "__main__":

    runner = TextTestRunner(verbosity=2)
    test_result = runner.run(test_loader.discover(test_path)).wasSuccessful()

    if test_result == False:
        sys.exit(1)
    else:
        sys.exit(0)

