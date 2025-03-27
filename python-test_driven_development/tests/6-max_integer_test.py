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

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_max_integer(self):
        """Test all cases for max_integer function"""
        # Test empty list
        self.assertIsNone(max_integer([]))

        # Test list with one element
        self.assertEqual(max_integer([98]), 98)

        # Test max at the end
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        # Test max at the beginning
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

        # Test max in the middle
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

        # Test one negative number in the list
        self.assertEqual(max_integer([1, -1, 2, 3]), 3)

        # Test only negative numbers in the list
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        # Test list with identical values
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

        # Test list with one float
        self.assertEqual(max_integer([1, 2, 3.5, 2]), 3.5)

if __name__ == "__main__":
    unittest.main(verbosity=2)
