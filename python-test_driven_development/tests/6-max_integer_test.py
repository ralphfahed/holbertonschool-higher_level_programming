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
        # Test empty list
        self.assertIsNone(max_integer([]))

        # Test single element
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-5]), -5)

        # Test positive numbers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([10, 5, 8, 9]), 10)

        # Test negative numbers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([-10, -5, -8, -9]), -5)

        # Test mixed positive and negative numbers
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([-10, 5, -8, 9]), 9)

        # Test duplicate numbers
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([1, 2, 2, 1]), 2)

        # Test float numbers
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)
        self.assertEqual(max_integer([1.1, 3.3, 4.4, 2.2]), 4.4)
        self.assertEqual(max_integer([-1.5, -2.5, -3.5, -4.5]), -1.5)

        # Test mixed integer and float numbers
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)
        self.assertEqual(max_integer([-1, -2.5, -3, -4.5]), -1)

        # Test large numbers
        self.assertEqual(max_integer([1000000, 2000000, 3000000]), 3000000)
        self.assertEqual(max_integer([-1000000, -2000000, -3000000]), -1000000)

        # Test zero
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([-1, 0, 1]), 1)
        self.assertEqual(max_integer([-1, 0, -2]), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
