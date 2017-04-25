import pytest

pytestmark = pytest.mark.usefixtures(
    'function_scope', 'class_scope', 'module_scope', 'session_scope')


class TestClass1(object):

    def test_1(self):
        print 'TEST 1 (test_py_1.py: TestClass1:test_1)'

    def test_2(self):
        print 'TEST 2 (test_py_1.py: TestClass1:test_2)'


class TestClass2(object):

    def test_3(self):
        print 'TEST 3 (test_py_1.py: TestClass2:test_1)'

    def test_4(self):
        print 'TEST 4 (test_py_1.py: TestClass2:test_1)'
