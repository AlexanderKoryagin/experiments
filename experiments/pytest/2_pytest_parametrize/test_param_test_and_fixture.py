import pytest


@pytest.fixture
def some_fixt(request):
    param = getattr(request, 'param', 'nothing provided')
    return param


@pytest.mark.parametrize('some_fixt', ['one', 'two', 'three'], indirect=True)
@pytest.mark.parametrize('param', [1, 2, 3])
def test_something(some_fixt, param):
    """Tests fixture parametrize"""
    print '\nTest where value from fixture = "{0}"'.format(some_fixt)
    print 'Test where value from param   = "{0}"'.format(param)
