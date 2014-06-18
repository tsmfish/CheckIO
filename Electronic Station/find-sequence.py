def checkio(matrix):
    sequence = 4
    dimension = len(matrix)

    for c in matrix:
        print('\t'.join([str(s) for s in c]))

    for i in range(0,dimension):
        for j in range(0,dimension):
            row, column, slash, backslash = True, True, True, True
            print('position [%d : %d]'%(i,j))
            for k in range(1,sequence):
                print('k: %d'%k)
                if column:
                    if dimension > i + k:
                        column = matrix[i+k-1][j] == matrix[i+k][j]
                        print('column: %s'%str(column))
                    else: column = False
                if row:
                    if dimension > j + k:
                        row = matrix[i][j+k-1] == matrix[i][j+k]
                        print('row: %s'%str(row))
                    else: row = False
                if slash:
                    if dimension > i + k and \
                       dimension > j + k:
                        slash = matrix[i+k-1][j+k-1] == matrix[i+k][j+k]
                        print('slash: %s'%str(slash))
                    else: slash = False
                if backslash:
                    if dimension > i + k and \
                       j - k > -1:
                        backslash = matrix[i+k-1][j-k+1] == matrix[i+k][j-k]
                        print('backslash: %s'%str(backslash))
                    else: backslash = False
                if not (row or column or slash or backslash) : break
            print('row = %s, column = %s, slash = %s, backslash: %s'%(row,column,slash,backslash))
            if row or column or slash or backslash:
                print('Return True\n\n')
                return True
    print('Return False\n\n')
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
