__author__ = 'Pavel.Malko'
def checkio(matrix):
    matrixLength = len(matrix)
    ranges = range(0,matrixLength)
    dsd = [[] for i in ranges]
    for i in ranges:
        dsd[i] = [str(i * matrixLength + j) for j in ranges]
    frequently = {'count':0,'value':None}
    def replaceInDsd(_from, _to):
        for i in ranges:
            for j in ranges:
                if dsd[i][j] == _from: dsd[i][j] = _to
    # draw dsd structure
    for i in ranges:
        for j in ranges:
            if j != 0 and  matrix[i][j-1] and matrix[i][j-1] == matrix[i][j]:
                dsd[i][j] = dsd[i][j-1]
            if i != 0 and matrix[i-1][j] and matrix[i-1][j] == matrix[i][j]:
                dsd[i][j] = dsd[i-1][j]
            if i + 1 < matrixLength and matrix[i+1][j] == matrix[i][j]:
                replaceInDsd(dsd[i][j],dsd[i+1][j])
                dsd[i][j] = dsd[i+1][j]
            if j + 1 < matrixLength and matrix[i][j+1] == matrix[i][j]:
                replaceInDsd(dsd[i][j],dsd[i][j+1])
                dsd[i][j] = dsd[i][j+1]
    # find in dsd frequently usage value
    counter, value = 1, ''
    for i in ranges:
        for j in ranges:
            if frequently.get(dsd[i][j]):
                frequently[dsd[i][j]]['counter'] += 1
                if frequently[dsd[i][j]]['counter'] > counter:
                    counter += 1
                    value = frequently[dsd[i][j]]['value']
            else:
                frequently[dsd[i][j]] = {'counter': 1, 'value': matrix[i][j]}
    # for list in matrix: print(list)
    # print('-'*15)
    # for list in dsd: print(list)

    return [counter,value]


print(checkio([
        [1, 2, 3, 4, 5],
        [1, 1, 1, 2, 3],
        [1, 1, 1, 2, 2],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ]))
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [1, 2, 3, 4, 5],
        [1, 1, 1, 2, 3],
        [1, 1, 1, 2, 2],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ]) == [14, 1], "14 of 1"

    assert checkio([
        [2, 1, 2, 2, 2, 4],
        [2, 5, 2, 2, 2, 2],
        [2, 5, 4, 2, 2, 2],
        [2, 5, 2, 2, 4, 2],
        [2, 4, 2, 2, 2, 2],
        [2, 2, 4, 4, 2, 2]
    ]) == [19, 2], '19 of 2'