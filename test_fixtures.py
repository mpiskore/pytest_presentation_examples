import pytest

from .code import increment, show_all_smaller_odd_positive_numbers


@pytest.fixture
def odd_numbers():
    return [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


def test_odds_with_fixture(odd_numbers):
    assert show_all_smaller_odd_positive_numbers(20) == odd_numbers


@pytest.fixture(scope="session")
# this fixture will be prepared once for whole session of tests
def more_fancy_fixture():
    # Do some complicated, heavy operations here
    # Run factories, connect to the database, prepare bulk of instances
    pass


def test_fancy_fixture(more_fancy_fixture):
    with pytest.raises(AttributeError):
        assert more_fancy_fixture.subinstances == 33


def test_fixture_from_conftest(the_answer):
    assert the_answer == '42'


# Built-in fixtures (stolen from Florian Bruhin's presentation on SPS16)

def test_tmpdir(tmpdir):
    assert not tmpdir.listdir()


def test_monkeypatch(monkeypatch):
    import os
    monkeypatch.setenv('FOO', 'test')
    assert 'FOO' in os.environ
