import pytest


@pytest.fixture
def some_fixt(request):
    param = getattr(request, 'param', 'nothing provided')
    return param + '_fixtadd'


@pytest.mark.parametrize('some_fixt', ['one', 'two', 'three'], indirect=True)
def test_something(some_fixt):
    """Tests fixture parametrize"""
    print '\nTest where value from fixture = "{0}"'.format(some_fixt)
