__author__ = 'Pavel.Malko'
def checkio(text):
    dict = {}
    frequent = 0
    for char in text.lower():
        if char.isalpha():
            dict.setdefault(char,text.lower().count(char))
            frequent = max(frequent, dict[char])
    return sorted([key for (key, value) in dict.items() if value == frequent])[0]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
