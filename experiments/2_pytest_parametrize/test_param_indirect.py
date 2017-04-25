import pytest


@pytest.fixture
def x(request):
    print "fixture 'x', param = '%s'" % request.param
    return request.param + "_fixt_adding"


@pytest.fixture
def y(request):
    print "fixture 'y', param = '%s'" % request.param
    return request.param + '_fixt_adding'


@pytest.mark.parametrize('x, y', [('a', 'b')], indirect=['x'])
# @pytest.mark.parametrize('x, y', [('a', 'b')], indirect=['x', 'y'])
# @pytest.mark.parametrize('x, y', [('a', 'b')], indirect=True)
# @pytest.mark.parametrize('x, y', [('a', 'b')], indirect=False)
def test_indirect(x, y):
    print '\nx = {0}'.format(x)
    print 'y = {0}'.format(y)
