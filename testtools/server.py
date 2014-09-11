# Copyright (c) 2014 testtools developers. See LICENSE for details.

"""Small server to give an API for driving tests."""

from functools import partial
import os.path
import unittest
import sys


class Server:
    """A test server.

    The server starts up as normal via testools.run but then allows the loaded
    tests to be listed, run, or a run to be interacted with. In order to have
    minimal impact on code under test or utilities like pdb which may attempt
    to read from stdin, the global file descriptors 0, 1 and 2 are replaced
    with socketpairs, and the server runs as a select loop across them plus
    the original stdin.

    See serve() for the specific usage API.
    """

    def __init__(self, run_argv):
        """Construct a server.

        :param run_argv: The command line arguments to use when loading the
            test suite.
        """

    def serve(self):
        """Serve on stdin.

        Requests are read from stdin, and acted on. When EOF is detected the
        server exits.
        """
        return 0
