#!/usr/bin/python3
import unittest

"""Module to find the max integer in a list
"""

def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

class SimpleTest(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([]), None)  # Edge case for empty list

if __name__ == "__main__":
    unittest.main(verbosity=2)
