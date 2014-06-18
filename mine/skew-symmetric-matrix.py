__author__ = 'Pavel.Malko'
def checkio(matrix):
    dimension = len(matrix)
    for i in range(0,dimension):
        if matrix[i][i] != 0: return False
        for j in range(i+1,dimension):
            if matrix[i][j] != -1 * matrix[j][i]: return False
    return True

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) == True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) == False, "3rd example"