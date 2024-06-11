import unittest
# import pytest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42),-42,'should be abs')
    def test_abs2(self):
        self.assertEqual(abs(-42),42,'should be abs')


if __name__ == "__main__":
    unittest.main()

        




