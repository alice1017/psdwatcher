#!/usr/bin/env python
#coding: utf-8

import logging


class Logger(logging.Logger):

    HEADER = "[ {:^7} ] "

    def debug(self, msg, *args, **kwargs):
        
        header = self.HEADER.format("DEBUG")

        if self.isEnabledFor(logging.DEBUG):
            self._log(logging.DEBUG, header+msg, args, **kwargs)

    def info(self, msg, *args, **kwargs):

        header = self.HEADER.format("INFO")

        if self.isEnabledFor(logging.INFO):
            self._log(logging.INFO, header+msg, args, **kwargs)

    def warning(self, msg, *args, **kwargs):

        header = self.HEADER.format("WARNING")

        if self.isEnabledFor(logging.WARNING):
            self._log(logging.WARNING, header+msg, args, **kwargs)

    warn = warning

    def error(self, msg, *args, **kwargs):

        header = self.HEADER.format("ERROR")

        if self.isEnabledFor(logging.ERROR):
            self._log(logging.ERROR, header+msg, args, **kwargs)

    def exception(self, msg, *args, **kwargs):

        kwargs['exc_info'] = 1
        if self.isEnabledFor(logging.ERROR):
            self._log(logging.ERROR, msg, args, **kwargs)

    def critical(self, msg, *args, **kwargs):

        header = self.HEADER.format("CRITICAL")

        if self.isEnabledFor(logging.CRITICAL):
            self._log(logging.CRITICAL, header+msg, args, **kwargs)

    fatal = critical

Logger = Logger("psdwatcher")
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
Logger.setLevel(logging.DEBUG)
Logger.addHandler(handler)
