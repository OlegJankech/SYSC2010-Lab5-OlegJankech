import unittest
from Lab5_Classes import Numbers, ECG

class TestNumbers(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

    def setUp(self):
        self.num = Numbers()
