# test_calculator.py

import unittest
from calculator import add, subtract, divide


class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        """Test addition of positive and negative numbers"""
        self.assertEqual(add(2, 3), 5)  # Typical case
        self.assertEqual(add(-1, -1), -2)  # Negative numbers
        self.assertEqual(add(-1, 2), 1)  # Mixed signs

    def test_subtract(self):
        """Test subtraction of various cases"""
        self.assertEqual(subtract(5, 3), 2)  # Typical case
        self.assertEqual(subtract(-1, -1), 0)  # Negative numbers
        self.assertEqual(subtract(2, 5), -3)  # Result is negative

    def test_divide(self):
        """Test division including zero division handling"""
        self.assertEqual(divide(10, 2), 5)  # Typical case
        self.assertEqual(divide(-6, 2), -3)  # Negative numerator
        self.assertAlmostEqual(divide(7, 3), 2.3333333, places=5)  # Decimal result
        with self.assertRaises(ValueError):  # Division by zero
            divide(5, 0)


if __name__ == '__main__':
    unittest.main()
