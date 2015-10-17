# -*- coding: utf-8 -*-
"""
Unit Test Template
"""
from __future__ import absolute_import, division, print_function

import sys
import datetime
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

import os

from ioflo.aid.sixing import *
from ioflo.aid.odicting import odict
from ioflo.test import testing
from ioflo.aid.consoling import getConsole
console = getConsole()

from ioflo.aid import timing


def setUpModule():
    console.reinit(verbosity=console.Wordage.concise)

def tearDownModule():
    pass


class BasicTestCase(unittest.TestCase):
    """
    Example TestCase
    """

    def setUp(self):
        """
        Call super if override so House Framer and Frame are setup correctly
        """
        super(BasicTestCase, self).setUp()

    def tearDown(self):
        """
        Call super if override so House Framer and Frame are torn down correctly
        """
        super(BasicTestCase, self).tearDown()

    def testTuuid(self):
        """
        Test TUUID generation
        """
        console.terse("{0}\n".format(self.testTuuid.__doc__))
        console.reinit(verbosity=console.Wordage.profuse)

        tuid = timing.tuuid()
        self.assertEqual(len(tuid), 24)
        stamp, sep, randomized = tuid.rpartition('_')
        self.assertEqual(sep, '_')
        self.assertEqual(len(stamp), 16)
        self.assertEqual(len(randomized), 7)

        tuid =  timing.tuuid(9)
        self.assertEqual(len(tuid), 24)
        stamp, sep, randomized = tuid.rpartition('_')
        self.assertEqual(sep, '_')
        self.assertEqual(len(stamp), 16)
        self.assertEqual(len(randomized), 7)
        self.assertEqual(stamp[:16], '0000000000895440' )

        console.reinit(verbosity=console.Wordage.concise)


def runOne(test):
    '''
    Unittest Runner
    '''
    test = BasicTestCase(test)
    suite = unittest.TestSuite([test])
    unittest.TextTestRunner(verbosity=2).run(suite)

def runSome():
    """ Unittest runner """
    tests =  []
    names = [
             'testTuuid',
            ]
    tests.extend(map(BasicTestCase, names))
    suite = unittest.TestSuite(tests)
    unittest.TextTestRunner(verbosity=2).run(suite)

def runAll():
    """ Unittest runner """
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(BasicTestCase))
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__' and __package__ is None:

    #console.reinit(verbosity=console.Wordage.concise)

    #runAll() #run all unittests

    runSome()#only run some

    #runOne('testBasic')


