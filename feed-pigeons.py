__author__ = 'Pavel.Malko'
def checkio(number):
    feed = number
    pigeons = 0
    flyPigeons = 1

    while feed >= pigeons + flyPigeons:
        pigeons += flyPigeons
        feed -= pigeons
        flyPigeons += 1
    if feed > pigeons:
        return feed
    else:
        return pigeons

print(checkio(1) )
print(checkio(2) )
print(checkio(3) )
print(checkio(5) )
print(checkio(10))
exit()
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"