from random import random

__author__ = 'Pavel.Malko'


def checkio(data):
    number = data
    ansver = ''

    signs = {'1000': {'one': 'M', 'five': '' },
             '100' : {'one': 'C', 'five': 'D'},
             '10'  : {'one': 'X', 'five': 'L'},
             '1'   : {'one': 'I', 'five': 'V'}}
    for exponent in reversed(range(0, 4)):
        power = 10 ** exponent
        mantisa = number // power
        if mantisa == 9:
            ansver += signs[str(power)]['one']+signs[str(power*10)]['one']
            number -= mantisa * power
        elif mantisa == 4:
                ansver += signs[str(power)]['one']+signs[str(power)]['five']
                number -= mantisa * power
        else:
            if mantisa >= 5:
                ansver += signs[str(power)]['five']
                number -= 5 * power
                mantisa -= 5
            if mantisa > 0:
                ansver += signs[str(power)]['one']*mantisa
                number -= mantisa * power

    return ansver


[checkio(int(99 * random())) for n in range(0, 20)]
# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'