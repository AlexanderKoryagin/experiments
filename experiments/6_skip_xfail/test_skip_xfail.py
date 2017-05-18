import pytest
import sys


xfail = pytest.mark.xfail(strict=True)
not_implemented = pytest.mark.skip(reason="Feature is not implemented.")
need_windows = pytest.mark.skipif(
    sys.platform != 'win32', reason="Requires Windows."
)


def func_for_test(int1, int2):
    print '{0} + {1}'.format(int1, int2)
    return int1 + int2


@pytest.mark.parametrize(
    'int1, int2, result',
    [
        (1, 1, 2),
        (2, 2, 4),
        xfail(('a', 1, 2)),
        xfail(('b', 4, 5), raises=TypeError),
        xfail(('c', 6, 7), reason='I want so'),
    ]
)
def test_something1(int1, int2, result):
    assert func_for_test(int1, int2) == result


@not_implemented
def test_something3():
    assert False


@need_windows
def test_something2():
    assert False
