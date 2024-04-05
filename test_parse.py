import pytest
import task


@pytest.mark.parametrize("text,words", [("Hello, world!", 2)])
def test_word_parsing(text, words):
    assert task.parse_words(text) == words


@pytest.mark.parametrize("text,strings", [("Hello, world!", 1)])
def test_string_parsing(text, strings):
    assert task.parse_strings(text) == strings
