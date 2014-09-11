# Copyright (c) 2014 testtools developers. See LICENSE for details.

"""Tests for the test server."""

import os
from unittest import TestSuite
import sys
from textwrap import dedent

from extras import try_import
fixtures = try_import('fixtures')
testresources = try_import('testresources')

import testtools
from testtools import TestCase, run, skipUnless, server
from testtools.compat import (
    _b,
    _u,
    StringIO,
    )
from testtools.matchers import (
    Contains,
    MatchesRegex,
    )


if fixtures:
    class SampleServerFixture(fixtures.Fixture):
        """Creates testtools.runexample temporarily."""

        def __init__(self):
            """Create a SampleServerFixture.

            :param broken: If True, the sample file will not be importable.
            """
            init_contents = _b("""\
from testtools import TestCase

class TestFoo(TestCase):
    def test_bar(self):
        import pdb;pdb.set_trace()
    def test_quux(self):
        import pdb;pdb.set_trace()
""")
            self.package = fixtures.PythonPackage(
            'runexample', [('__init__.py', init_contents)])

        def setUp(self):
            super(SampleServerFixture, self).setUp()
            self.useFixture(self.package)
            testtools.__path__.append(self.package.base)
            self.addCleanup(testtools.__path__.remove, self.package.base)
            self.addCleanup(sys.modules.pop, 'testtools.runexample', None)


@skipUnless(fixtures, "fixtures not present")
class TestServer(TestCase):

    def test_make_server(self):
        self.useFixture(SampleServerFixture())
        test_server = server.Server(['testtools.runexample'])

    def test_serve(self):
        self.useFixture(SampleServerFixture())
        test_server = server.Server(['testtools.runexample'])
        stdin_r, stdin_w = os.pipe()
        # EOF - enough to trigger server exit.
        os.close(stdin_w)
        patch = fixtures.MonkeyPatch('sys.stdin', os.fdopen(stdin_r, 'rt'))
        patch.setUp()
        try:
            self.assertEqual(0, test_server.serve())
        finally:
            patch.cleanUp()
        

def test_suite():
    from unittest import TestLoader
    return TestLoader().loadTestsFromName(__name__)
