from .code import increment, show_all_smaller_odd_positive_numbers


def test_increment():
    assert increment(5) == 6


def test_failed_increment():
    assert increment(5) == 7, 'this test failed on purpose'


def test_the_other_function():
    assert show_all_smaller_odd_positive_numbers(8) == [1, 3, 5, 7]


def test_the_other_function_but_failed():
    assert show_all_smaller_odd_positive_numbers(11) == [1, 3, 5, 7, 9, 11]
