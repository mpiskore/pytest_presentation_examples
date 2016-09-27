import unittest

from .code import increment, show_all_smaller_odd_positive_numbers


class TestLetMeShowHowDullThisIs(unittest.TestCase):

    def test_increment(self):
        self.assertEqual(increment(5), 6)

    def test_failed_increment(self):
        # The error message in this case is far less impressive than in py.test
        self.assertEqual(increment(5), 7)


if __name__ == '__main__':
    unittest.main()
