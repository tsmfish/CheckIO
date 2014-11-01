__author__ = 'Pavel.Malko'

def checkio(chips):
    def nextStep():
        global solution, ansver
        if len(chips)

    ansver = 0

    chipsNumber = len(chips)
    angelsNumber = len(chips[0])

    for startChip in range(chipsNumber):
        for startAngel in range(angelsNumber):
            solution = [{'chip': startChip,
                         'angel': startAngel,
                         'visited': [],
                         'unvisited': [chip for chip in range(chipsNumber) if chips[startChip][startAngel] in chips[chip]],
                         'chips': [chips]}]
            while len(solution) != 1 or solution[0]['unvisited']:
                nextStep()
    return ansver

print (checkio(
        [[1, 4, 20], [3, 1, 5], [50, 2, 3], [5, 2, 7], [7, 5, 20], [4, 7, 50]]))
# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(
        [[1, 4, 20], [3, 1, 5], [50, 2, 3], [5, 2, 7], [7, 5, 20], [4, 7, 50]]) == 152, "First"
    assert checkio(
        [[1, 10, 2], [2, 20, 3], [3, 30, 4], [4, 40, 5], [5, 50, 6], [6, 60, 1]]) == 210, "Second"
    assert checkio(
        [[1, 2, 3], [2, 1, 3], [4, 5, 6], [6, 5, 4], [5, 1, 2], [6, 4, 3]]) == 21, "Third"
    assert checkio(
        [[5, 9, 5], [9, 6, 9], [6, 7, 6], [7, 8, 7], [8, 1, 8], [1, 2, 1]]) == 0, "Fourth"
