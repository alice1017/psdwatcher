#!/usr/bin/env python
#coding: utf-8

import sys

from psdwatcher.cli    import parser
from psdwatcher.util   import Logger
from psdwatcher.config import FileContainer

def program(args):

    #dev:
    container = FileContainer("psdwatcher.rc")

    if args.command == "add":

        container.add_file(args.file)
        print "Add '{0}' to watching list.".format(args.file)
        sys.exit(0)


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
            Logger.error(
                "Error: {0}\n".format(e.message)
            )

        sys.exit(1)

    
if __name__ == "__main__":

    main()
    
