#!/usr/bin/python3
import unittest
from max_integer_6 import max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_list_is_empty(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))

    def test_list_with_one_element(self):
        """Test list with one element"""
        self.assertEqual(max_integer([98]), 98)

    def max_at_the_end(self):
        """Test max at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_the_beginning(self):
        """Test max at the beginning"""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_max_in_the_middle(self):
        """Test max in the middle"""
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_one_negative_number_in_the_list(self):
        """Test one negative number in the list"""
        self.assertEqual(max_integer([1, -1, 2, 3]), 3)

    def test_only_negative_numbers_in_the_list(self):
        """Test only negative numbers in the list"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_list_with_identical_values(self):
        """Test list with identical values"""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_list_with_one_float(self):
        """Test list with one float"""
        self.assertEqual(max_integer([1, 2, 3.5, 2]), 3.5)

if __name__ == "__main__":
    unittest.main(verbosity=2)

