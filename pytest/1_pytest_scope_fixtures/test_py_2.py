import pytest

pytestmark = pytest.mark.usefixtures(
    'function_scope', 'class_scope', 'module_scope', 'session_scope')


class TestClass3(object):

    def test_5(self):
        print 'TEST 5 (test_py_2.py: TestClass3:test_5)'

    def test_6(self):
        print 'TEST 6 (test_py_2.py: TestClass3:test_6)'


class TestClass4(object):

    def test_7(self):
        print 'TEST 7 (test_py_2.py: TestClass4:test_7)'

    def test_8(self):
        print 'TEST 8 (test_py_2.py: TestClass4:test_8)'
