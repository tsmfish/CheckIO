__author__ = 'Pavel.Malko'
def checkio(number):
    multiple = 1
    for sign in str(number):
        if int(sign): multiple *= int(sign)
    return multiple

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
