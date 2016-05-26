#!/usr/bin/env python
# coding: utf-8

import argparse

from psdwatcher import __version__

parser = argparse.ArgumentParser(
    prog="psdwatcher",
    version=__version__,
    description="PSDwatcher - watching psd, and commit automatically."
)

parser.add_argument(
    "--traceback",
    action="store_true",
    dest="traceback",
    help="When PSDwatcher raises error, "
         "print only error message. "
         "But use this argument, "
         "you can show traceback of error."
)

parser.add_argument(
    "--dev",
    action="store_true",
    dest="dev",
    help="Chnage development mode"
)

subparser = parser.add_subparsers(
    title="commands",
    dest="command"
)

parser_add_help = \
    "PSDwatcher registers a new PSD file to watch list."

parser_add = subparser.add_parser(
    "add",
    description=parser_add_help,
    help=parser_add_help
)

parser_add.add_argument(
    "file",
    action="store",
    metavar="PSDFILE",
    help="A PSD file name or path."
)

parser_run_help = \
    "PSDwatcher runs the file modification watcher, " \
    "and automatically exec 'git-add' and 'git-commit'. " \

parser_run = subparser.add_parser(
    "run",
    description=parser_run_help,
    help=parser_run_help
)

parser_run.add_argument(
    "--quiet",
    action="store_true",
    dest="is_quiet",
    help="PSDwatcher doesn't print log."
)

parser_run.add_argument(
    "--verbose",
    action="store_true",
    dest="is_verbose",
    help="PSDwatcher print verbose log."
)

parser_list_help = \
    "PSDwatcher shows the list of all " \
    "registered PSD file."

parser_list = subparser.add_parser(
    "list",
    description=parser_list_help,
    help=parser_list_help
)
