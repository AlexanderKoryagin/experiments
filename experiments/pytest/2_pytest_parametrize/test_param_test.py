# http://docs.pytest.org/en/latest/parametrize.html

import pytest


@pytest.mark.parametrize('param', ['one', 'two', 'three', 'four'])
def test_something1(param):
    """Tests usage of PyTest for case parametrize"""
    print 'Test with value of "param" = "{0}"'.format(param)
    assert param != 'five'


param_strings = ['one', 'two']
param_ints = [1, 2]


@pytest.mark.parametrize('param1', param_strings)
@pytest.mark.parametrize('param2', param_ints)
def test_something2(param1, param2):
    """Tests usage of PyTest for case parametrize with several params"""
    print 'Test with value of "param1" = "{0}"'.format(param1)
    print 'Test with value of "param2" = "{0}"'.format(param2)
