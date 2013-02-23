# Copyright (c) 2009-2012 testtools developers. See LICENSE for details.

"""Test result objects."""

__all__ = [
    'CopyStreamResult',
    'ExtendedToOriginalDecorator',
    'ExtendedToStreamDecorator',
    'IncompleteTestDetector',
    'MultiTestResult',
    'StreamFailFast',
    'StreamResult',
    'StreamResultRouter',
    'StreamSummary',
    'StreamToDict',
    'StreamToExtendedDecorator',
    'Tagger',
    'TestByTestResult',
    'TestControl',
    'TestResult',
    'TestResultDecorator',
    'TextTestResult',
    'ThreadsafeForwardingResult',
    'ThreadsafeStreamResult',
    'TimestampingStreamResult',
    ]

from testtools.testresult.real import (
    CopyStreamResult,
    ExtendedToOriginalDecorator,
    ExtendedToStreamDecorator,
    IncompleteTestDetector,
    MultiTestResult,
    StreamFailFast,
    StreamResult,
    StreamResultRouter,
    StreamSummary,
    StreamToDict,
    StreamToExtendedDecorator,
    Tagger,
    TestByTestResult,
    TestControl,
    TestResult,
    TestResultDecorator,
    TextTestResult,
    ThreadsafeForwardingResult,
    ThreadsafeStreamResult,
    TimestampingStreamResult,
    )
