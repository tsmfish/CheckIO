__author__ = 'Pavel.Malko'
VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    import re

    return len(['+' for w in re.compile(r'\b\w\w+\b', re.IGNORECASE).findall(text) if (
    not len(re.compile('[' + VOWELS + ']{2,}', re.IGNORECASE).findall(w)) and not len(
        re.compile('[' + CONSONANTS + ']{2,}', re.IGNORECASE).findall(w)))])

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
