__author__ = 'Pavel.Malko'
from fractions import Fraction

METALS = ('gold', 'tin', 'iron', 'copper')


def checkio(alloys):
    import re
    def determinante(matrix):
        determinante = Fraction(0,1)
        dimension = len(matrix)
        for i in range(0,dimension):
            slash = Fraction(1,1)
            backslash = Fraction(1,1)
            slashArray, backslashArray = [], []
            for j in range(0,dimension):
                print('[',j,'],[',(i+j)%dimension,'] - [',j,'],[',(dimension - j + i - 1)%dimension,']')
                slashArray.append(matrix[j][(i+j)%dimension])
                backslashArray.append(matrix[j][(dimension - j + i - 1)%dimension])
                slash *= matrix[j][(i+j)%dimension]
                backslash *= matrix[j][(dimension - j + i - 1)%dimension]
            print('\ndeterimante: ', determinante, '\nslash: ',slash,'\nbackslash: ',backslash)
            print('slash: ', slashArray)
            print('backslash: ', backslashArray)
            determinante += (slash - backslash)
        return determinante
    matrix = [[Fraction(0,1) for i in range(0,5)] for j in range(0,4)]
    # parse matrix g, t, i, c, sum
    matrix[3] = [Fraction(1,1),Fraction(1,1),Fraction(1,1),Fraction(1,1),Fraction(1,1)]
    for phrase in range(0,len(alloys)):
        for metal in range(0,len(METALS)):
            if re.search(METALS[metal], list(alloys.keys())[phrase]): matrix[phrase][metal] = Fraction(1,1)
        matrix[phrase][4] = alloys[list(alloys.keys())[phrase]]
    main, gold = [],[]
    for i in range(0,4):
        main.append([])
        gold.append([])
        for j in range(0,4):
            main[i].append(matrix[i][j])
            if j == 0:
                gold[i].append(matrix[i][4])
            else:
                gold[i].append(matrix[i][j])
    for i in matrix: print(i)
    print()
    for i in main: print(i)
    print('\n',determinante(main),'\n')
    for i in gold: print(i)
    print('\n',determinante(gold),'\n')
    return determinante(gold) / determinante(main)

checkio({
        'gold-tin': Fraction(1, 2),
        'gold-iron': Fraction(1, 3),
        'gold-copper': Fraction(1, 4),
        })
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({
        'gold-tin': Fraction(1, 2),
        'gold-iron': Fraction(1, 3),
        'gold-copper': Fraction(1, 4),
        }) == Fraction(1, 24), "1/24 of gold"
    assert checkio({
        'tin-iron': Fraction(1, 2),
        'iron-copper': Fraction(1, 2),
        'copper-tin': Fraction(1, 2),
        }) == Fraction(1, 4), "quarter"
