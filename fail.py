#!/usr/bin/python3
import unittest

from function import absolute_value

class TestCases(unittest.TestCase):
    def test_list_int(self):
        data = 20
        result = absolute_value(data)
        self.assertEqual(result, -20)

    def test_list_int1(self):
        data = -20
        result = absolute_value(data)
        self.assertEqual(result, -20)
if __name__ == '__main__':
    unittest.main()

