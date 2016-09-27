import pytest


@pytest.fixture(scope="module")
def the_answer():
    return '42'
