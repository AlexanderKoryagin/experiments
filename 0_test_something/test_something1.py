import pytest
import random


def add_function(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise ValueError("'a' or 'b' is not int")


@pytest.mark.parametrize('values', [[1, 2, 3], [4, 5, 9], [-2, 4, 2]])
def test_add_function(values):

    a, b, c = values
    assert c == add_function(a, b)

    for i in xrange(0, 100):
        a = random.randint(0, 100000)
        b = random.randint(0, 100000)
        assert a + b == add_function(a, b)

    with pytest.raises(ValueError):
        add_function('a', 2)
