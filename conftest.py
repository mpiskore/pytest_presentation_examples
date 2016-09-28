import pytest


@pytest.fixture(scope="module")
def the_answer():
    return '42'


def pytest_addoption(parser):
    parser.addoption(
        "--backend", choices=("webkit", "webengine"), default="webkit"
    )
