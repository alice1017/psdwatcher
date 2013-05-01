#!/usr/bin/env python
#coding: utf-8

import os
from distutils.core import setup

def makebin():
    # make dir
    if not os.path.isdir("bin"):
        os.system("mkdir bin")

    # copy file
    os.system("cp psdwatcher.py bin/psdwatcher")

    # add permission
    os.system("chmod +x bin/psdwatcher")

makebin()

setup(
	name="psdwatcher",
	author="Alice1017",
	version="1.0b",
	license=open("LICENSE").read(),
    url="https://github.com/alice1017/psdwatcher",
	description="You can watch the change log of psd file using git",
    long_description=open("README.rst").read(),
	packages=['termcolor'],
	scripts=['bin/psdwatcher']
)

