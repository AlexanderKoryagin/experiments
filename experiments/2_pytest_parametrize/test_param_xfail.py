import pytest


@pytest.mark.parametrize(
    'values',
    [
        (1, 2, 3),
        (2, 4, 6),
        (3, 4, 7),
        pytest.mark.xfail(
            (1, 1, 3), strict=True),
        pytest.mark.xfail(
            ('x', 1, 3), strict=True, raises=TypeError)
    ]
)
def test_xfail(values):
    """Tests parametrize with xfail."""
    a, b, c = values
    assert a + b == c
