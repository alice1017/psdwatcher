#!/usr/bin/env python
#coding: utf-8

import sys

from psdwatcher.cli    import parser
from psdwatcher.util   import Logger
from psdwatcher.config import FileContainer

def program(args):

    #dev:
    if args.dev:
        container = FileContainer("psdwatcher-dev.rc")
    else:
        container = FileContainer()

    if args.command == "add":

        container.add_file(args.file)
        Logger.info("Add '{0}' to watching list.".format(args.file))
        sys.exit(0)

    #elif args.command == "run":

    #    #dev:
    #    from psdwatcher.core import ModificationWathcer

    #    psdfiles = container.release()
    #    watchers = []
    #    
    #    for psdfile in psdfiles:
    #        watchers.append(ModificationWathcer(psdfile))

    #    try:
    #        while True:
    #            for watcher in watchers:
    #                watcher.watch()

    #    except KeyboardInterrupt:
    #        Logger.info("KeyboardInterrupt: PSDwatcher terminated.")
    #        sys.exit(0)
    #        



def main():

    if len(sys.argv) == 1:
        parser.parse_args(["-h"])

    args = parser.parse_args()
    print args

    try:
        program(args)

    except Exception as e:

        if args.traceback is True:
            print "{:-^30}".format(" TRACEBACK ")
            Logger.exception(e)

        else:
            Logger.error(e.message)

        sys.exit(1)

    
if __name__ == "__main__":

    main()
    
