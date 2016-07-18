import pytest


# def gen_fixt(words):
#     @pytest.fixture
#     def some_fixt(request):
#         words = getattr(request, 'words', 'nothing provided')
#         return words
#
# hello_word = gen_fixt('hello')
# bye_word = gen_fixt('bye')
#
#
# def test_1(hello_word, bye_word):
#     print hello_word
#     print bye_word
