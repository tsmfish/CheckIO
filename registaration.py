__author__ = 'Pavel.Malko'
def checkio(els):
    sum=0
    for add in els[0:3]: sum+=add
    return sum

if checkio([1, 2, 3, 4, 5, 6]) == 6:
    print('Done!')
