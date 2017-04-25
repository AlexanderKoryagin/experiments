import pytest


@pytest.yield_fixture
def callable_fixt():
    values = []

    def _values_multiply(int_val):
        values.append(int_val)
        multiply = int_val * 2
        return multiply

    yield _values_multiply

    print '\nValues before cleanup = %s>' % values  # [1, 2, 3]
    values = []


def test_callable_fixt(callable_fixt):
    a = callable_fixt(1)
    b = callable_fixt(2)
    c = callable_fixt(3)

    print ''
    print 'a = %d' % a
    print 'b = %d' % b
    print 'c = %d' % c
