# http://docs.pytest.org/en/latest/parametrize.html

import pytest


@pytest.mark.parametrize('param', ['one', 'two', 'three', 'four'])
def test_something1(param):
    """Tests usage of PyTest for case parametrize"""
    print '\nTest with value of "param" = "{0}"'.format(param)


@pytest.mark.parametrize('param1', ['one', 'two', 'three', 'four'])
@pytest.mark.parametrize('param2', [1, 2, 3, 4])
def test_something2(param1, param2):
    """Tests usage of PyTest for case parametrize"""
    print '\nTest with value of "param1" = "{0}"'.format(param1)
    print '\nTest with value of "param2" = "{0}"'.format(param2)
