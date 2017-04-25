import itertools

import pytest


numbers = [1, 2, 3, 4, 5]
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['x', 'y', 'z']


@pytest.mark.parametrize(
    'number, vowel, consonant',
    itertools.product(numbers, vowels, consonants)
)
def test1(number, vowel, consonant):
    print 'First test: {0}, {1}, {2}'.format(number, vowel, consonant)


@pytest.fixture(params=numbers)
def number(request):
    return request.param


@pytest.fixture(params=vowels)
def vowel(request):
    return request.param


@pytest.fixture(params=consonants)
def consonant(request):
    return request.param


def test2(number, vowel, consonant):
    print 'Second test: {0}, {1}, {2}'.format(number, vowel, consonant)
