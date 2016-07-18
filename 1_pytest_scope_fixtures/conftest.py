import pytest
from random import randint


@pytest.yield_fixture(scope='function')
def function_scope():
    numb = randint(0, 1000)
    print '~ FUNCTION_start: Start of FUNCTION scope fixture #%d' % numb
    yield
    print '~~ FUNCTION_end: End of FUNCTION scope fixture #%d' % numb


@pytest.yield_fixture(scope='class')
def class_scope():
    numb = randint(0, 1000)
    print '^ CLASS_start: Start of CLASS scope fixture #%d' % numb
    yield
    print '^^ CLASS_end: End of CLASS scope fixture #%d' % numb


@pytest.yield_fixture(scope='module')
def module_scope():
    numb = randint(0, 1000)
    print '* MODULE_start: Start of MODULE scope fixture #%d' % numb
    yield
    print '** MODULE_end: End of MODULE scope fixture #%d' % numb


@pytest.yield_fixture(scope='session')
def session_scope():
    numb = randint(0, 1000)
    print '> SESSION_start: Start of SESSION scope fixture #%d' % numb
    yield
    print '>> SESSION_end: End of SESSION scope fixture #%d' % numb
