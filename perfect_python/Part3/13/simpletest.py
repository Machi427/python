import unittest

class SimpleTests(unittest.TestCase):
    def test_it(self):
        result = " ".join("abc")
        self.assertEqual(result, "a b c")
