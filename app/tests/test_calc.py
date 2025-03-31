"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc

class CalcTests (SimpleTestCase):
    """Test the calc module"""

    def test_add(self):
        res = calc.add(1, 2)

        self.assertEqual(res, 3)

    def test_subtract(self):
        res = calc.subtract(3, 1)

        self.assertEqual(res, 2)