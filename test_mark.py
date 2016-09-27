import pytest
import sys

from .code import increment, show_all_smaller_odd_positive_numbers


@pytest.mark.parametrize(
    'number, plusoned',
    [(1, 2), (11, 12), (-1, 0), (0.5, 1.5), (float('inf'), float('inf'))],
)
def test_multiple_increment(number, plusoned):
    assert increment(number) == plusoned


@pytest.mark.skip
def test_this_really_fails():
    assert increment(1) == 3, "Ya ain't gonna see this"


@pytest.mark.skipif(
    sys.version_info > (3,0), reason="works only on python2"
)
def test_if_range_works_the_good_ole_way():
    assert range(5) == [0, 1, 2, 3, 4]


@pytest.mark.xfail
def test_this_one_is_too_obvious():
    assert 0 == 1


# Name your own markers and run them with $ pytest -m MARKNAME
@pytest.mark.silly
def test_that_are_supposed_to_be_silly():
    assert 2 + 2 == 4

