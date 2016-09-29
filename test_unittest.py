import unittest

from code import increment, show_all_smaller_odd_positive_numbers


class TestLetMeShowHowDullThisIs(unittest.TestCase):

    def test_increment(self):
        self.assertEqual(increment(5), 6)

    def test_failed_increment(self):
        # The error message in this case is far less impressive than in py.test
        self.assertEqual(increment(5), 7)

    def test_the_other_method(self):
        # this error message is pretty similar to pytest one
        self.assertEqual(
            show_all_smaller_odd_positive_numbers(20),
            [1, 3, 5, 7, 9, 11, 13, 14, 15, 17, 19, 21]
        )


if __name__ == '__main__':
    unittest.main()
