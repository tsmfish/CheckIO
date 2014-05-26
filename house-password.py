import re

__author__ = 'Pavel.Malko'
def checkio(data):

    rules = (re.compile("[a-zA-Z0-9]{10,}"),re.compile("[a-z]"),re.compile("[A-Z]"),re.compile("[0-9]"))
    for rule in rules:
        if not rule.search(data): return False
    return True

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"

