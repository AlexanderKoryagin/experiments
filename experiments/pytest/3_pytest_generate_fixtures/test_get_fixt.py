import pytest


def words_factory(word):

    @pytest.yield_fixture
    def words():
        phrase = (
            "\nSay '{word}' again. Say '{word}' again, I dare you, "
            "I double dare you motherf....r, say '{word}' one more "
            "Goddamn time!").format(word=word)
        yield phrase

    return words


say_hello = words_factory('hello')
say_what = words_factory('what')
say_banana = words_factory('banana')


def test_phrase(say_hello, say_what, say_banana):
    print say_hello
    print say_what
    print say_banana
