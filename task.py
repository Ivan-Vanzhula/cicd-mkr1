import re


def load_text(path="input.txt"):
    """Return text from the file"""
    file = open(path)
    return file.read()


def parse_words(text):
    """Split text to words"""
    words = re.split(r'[.,?!:;\s]+', text)

    # remove all empty strings
    words = list(filter(None, words))
    print(words)
    return len(words)


def parse_strings(text):
    """Split text to strings"""
    strings = re.split(r'[.?!]+', text)
    strings = list(filter(None, strings))
    print(strings)
    return len(strings)


if __name__ == "__main__":
    text = load_text()
    print(parse_words(text))
    print(parse_strings(text))
