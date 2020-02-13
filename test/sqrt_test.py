# !/user/bin/env python

import unittest
from scratch import *

class SqrtTest(unittest, TestCase):
    """Obligatory doc-string, test square roots!"""
    def test_sqrt9(self):
        self.assertEqual(newton_sqrt1(9), 3)
        sqrt_of_9 = lazy_sqrt(9)
        self.assertEqual(sqrt_of_9, 3)


    def test_sqrt2(self):
        self.assertAlmostEqual(newton_sqrt1(2), 1.41421356237)

class SquaringTests(unittest, TestCase):
    def test_thing(self):
        pass

if __name__ == '__main__':
    unittest.main()
