__author__ = 'Pavel.Malko'
FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    ansver = ''
    parse = number

    if parse > 99:
        ansver += FIRST_TEN[parse // 100 - 1] + " " + HUNDRED
        parse -= (parse // 100) * 100
        if parse != 0: ansver += " "
    if parse > 19:
        ansver += OTHER_TENS[parse // 10 - 2]
        parse -= (parse // 10) * 10
        if parse != 0: ansver += " "
    if parse > 10:
        ansver += SECOND_TEN[parse % 20 - 10]
        parse = 0
    if parse > 0:
        ansver += FIRST_TEN[parse % 20 - 1]
    return ansver

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"