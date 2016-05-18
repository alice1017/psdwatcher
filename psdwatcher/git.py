#!/usr/bin/env python
#coding: utf-8

from subprocess import Popen


class GitError(BaseException):

    pass

class Git(object):

    def _exec(self, cmd, *args, **kwargs):

        if len(args) == 0:
            command = ("git", cmd)

        elif isinstance(args[0], tuple):
            # Avoid duplicate tuple
            # ex. self.rev_parse("--show-toplevel")
            #   ->('git', 'rev-parse', ('--show-toplevel',))
            command = ("git", cmd) + tuple([arg for arg in args[0]])

        else:
            command = ("git", cmd) + args

        stdin  = int(kwargs["stdin"])  if "stdin"  in kwargs else -1
        stdout = int(kwargs["stdout"]) if "stdout" in kwargs else -1
        stderr = int(kwargs["stderr"]) if "stderr" in kwargs else -1

        proc = Popen(
            command,
            stdin=stdin, stdout=stdout, stderr=stderr
        )

        out, err = proc.communicate()

        if len(err) == 0:
            return out.strip()

        else:
            raise GitError(err.strip())

    def add(self, path):

        self._exec("add", path)

    def commit(self, commit_msg, **kwargs):

        arg_fmt = "--{0}"
        command_args = ["-m", commit_msg]

        if kwargs:
            for key, val in kwargs.iteritems():
                command_args.append(arg_fmt.format(key))
                command_args.append(val)

        return self._exec("commit", *command_args)

    def init(self):

        self._exec("init")

    def rev_parse(self, *args):

        return self._exec("rev-parse", args)

    def is_inside_work_tree(self):
        
        try:
            boolean = self.rev_parse("--is-inside-work-tree")

        except GitError:
            return False

        if boolean == "true":
            return True

git = Git()
