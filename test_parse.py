import pytest
import task


# Parameters for testing the parse_words function
@pytest.mark.parametrize("text,words", [
    ("Hello, world!", 2),
    ("This is a test", 4),
    ("", 0),
    ("One", 1),
])
def test_word_parsing(text, words):
    assert task.parse_words(text) == words


# Parameters for testing the parse_strings function
@pytest.mark.parametrize("text,strings", [
    ("Hello, world!", 1),
    ("Hello. World!", 2),
    ("", 0),
    ("""This is a test sentence. It contains several words;
    Another sentence ends with a question mark?
    And finally, a third sentence ends with an exclamation mark!""", 3), ])
def test_string_parsing(text, strings):
    assert task.parse_strings(text) == strings
