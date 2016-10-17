import pytest

pytest_plugins = 'fixt_1'


@pytest.fixture
def basic_fixture():
    print '\nBasic fixture'
