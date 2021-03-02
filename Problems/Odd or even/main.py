# tests for the is_even() function
import unittest


class TestIsEven(unittest.TestCase):

    def test_when_output_true(self):
        # write your tests here
        self.assertTrue(is_even(2))

    def test_when_output_false(self):
        # write your tests here
        self.assertFalse(is_even(1))


if __name__ == '__main__':
    unittest.main()