import unittest
from unittest import mock
from mod2 import func2

class func2Tests(unittest.TestCase):
    @mock.patch("mod1.func1")
    def test_odd(self, func1):
        func1.return_value = 33
        result = func2()
        self.assertEqual(result, "odd")

    @mock.patch("mod1.func1")
    def test_even(self, func1):
        func1.return_value = 24
        result = func2()
        self.assertEqual(result, "even")
