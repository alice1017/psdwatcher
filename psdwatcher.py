#!/usr/bin/env python
#coding: utf-8

import os
import sys
import time
import stat
import termcolor
import cPickle as pickle

from argparse   import ArgumentParser
from subprocess import Popen

WATCH_LIST_FILE = os.environ["HOME"]+"/.psdwatcher.rc"

parser = ArgumentParser(
    prog="psdwatcher",
    version="1.0b",
    description="You can watch the change log of psd file using git.")

subparsers = parser.add_subparsers(dest="subcmd")

cmd_add = subparsers.add_parser("add", help="Add PSD file at watch list.")
cmd_add.add_argument("psd_file", action="store", help="The PSD file name.")

cmd_watch = subparsers.add_parser("run", help="Start watching.")
cmd_watch.add_argument("--dev", action="store_true", dest="dev", help="Write out development log")

cmd_list = subparsers.add_parser("list", help="Show the files that was contained watch-list")

def is_exist_listfile():
    return os.access(WATCH_LIST_FILE, os.F_OK)

def get_watch_list():
    return pickle.load(open(WATCH_LIST_FILE))

def update_list(obj):
    pickle.dump(obj, open(WATCH_LIST_FILE,"w"))
    return

def is_in_gitrepo():
    cmd = "git rev-parse --is-inside-work-tree".split()
    proc = Popen(cmd, stdout=-1, stderr=-1, stdin=-1)
    boolean = proc.communicate()[0][:-1]
    if boolean == "true":
        return True
    else:
        return False


def add_file(namespace):
    file_name = namespace.psd_file.split("/")[-1]
    file_ext = file_name.split(".")[-1]
    file_path = os.path.abspath(os.path.join(os.getcwd(), namespace.psd_file))
    file_dir = os.path.dirname(file_path)

    if not os.access(file_path, os.F_OK):
        raise IOError("%s file does not found." % file_path)

    if file_ext != "psd":
        raise IOError("fatal: '%s' this file is not PSD file!!" % file_name)

    if is_exist_listfile():
        watch_list = get_watch_list()
    else:
        watch_list = []

    if file_name not in [n for n,d,p in watch_list]:
        watch_list.append( (file_name, file_dir, file_path) )
        update_list(watch_list)

    else:
        raise KeyError("'%s' file is already added." % file_name)


def start_watch(namespace):
    if is_exist_listfile():
        watch_list = get_watch_list()
    else:
        raise IOError("%s file does not found." % WATCH_LIST_FILE)

    counter = 0
    timestamp_register = {}
    binary_content = {}
    watch_list_files_length = len(watch_list)

    print "Start watching........"
    while True:
        for file_name, file_dir, file_path in watch_list:
            if namespace.dev:
                print "="*80
                print "Now watching file : %s" % termcolor.colored(file_name, "red")
            
            # move dir
            if namespace.dev: print "Moving Directory to %s" % termcolor.colored(file_dir, "blue")

            os.chdir(file_dir)


            # check whether there is git repository
            if namespace.dev:
                print "Checking wheter there is git repository... ",

            if not is_in_gitrepo():
                if namespace.dev: print termcolor.colored("git repository does not found", "yellow")
                raise IOError("fatal: Not a git repository (or any of the parent directories): .git")

            if namespace.dev: print termcolor.colored("git repository does found", "blue")


            # register original timestamp
            if counter <= watch_list_files_length:
                if namespace.dev: print "Registring file's original timestamp: %s" % os.stat(file_path)[stat.ST_MTIME]
                timestamp_register[file_name] = os.stat(file_path)[stat.ST_MTIME]

                if namespace.dev: print "Registering psd file's binary content"
                binary_content[file_name] = open(file_name).read()

                counter += 1
                continue

            # take a timestamp
            old_timestamp = timestamp_register[file_name]
            now_timestamp = os.stat(file_path)[stat.ST_MTIME]
            if namespace.dev:
                print "Taking a timestamp:"
                print "\told: %s" % timestamp_register[file_name]
                print "\tnew: %s" % os.stat(file_path)[stat.ST_MTIME]

            # get the binary content
            old_bincontent = binary_content[file_name]
            now_bincontent = open(file_name).read()
            if namespace.dev: print "Getting the psd file's binary content"

            if old_timestamp != now_timestamp and old_bincontent != now_bincontent:
                # the file was overwritten

                # write log
                print termcolor.colored("Catch the '%s' file's change!" % file_name, "yellow")
                print "timestamp : %s -> %s" % (old_timestamp, now_timestamp)
                return

            else:
                # file not changed 
                continue

            counter += 1

    
def show_watch_list(namespace):
    if is_exist_listfile():
        watch_list = get_watch_list()

        for file_name, file_dir, file_path in watch_list:
            print file_path

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        parser.parse_args(["-h"])

    args = parser.parse_args()

    fn_register = {
        "add": add_file,
        "run": start_watch,
        "list": show_watch_list}

    for key in fn_register.keys():
        if args.subcmd == key:
            fn_register[key](args)
