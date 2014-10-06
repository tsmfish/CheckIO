__author__ = 'Pavel.Malko'
def golf(holes):
    import math

    distance = lambda a,b : math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    comparator = lambda a: a if a else 65536

    points = [(0, 0)] + (list(holes))
    rang, lowerLimit, path = len(points), 0, []
    distanceMatrix = [[None for i in range(0, rang)] for j in range(0, rang)]
    # generate distance matrix
    for i, point1 in enumerate(points):
        for j, point2 in enumerate(points[i+1:]):
            distanceMatrix[i+j+1][i] = distanceMatrix[i][i+j+1] = distance(point1, point2)

    print(points)
    # for string in distanceMatrix: print(string)

    for step in range(0,rang-2):
        for i in range(0,rang):
            minInRow = min(distanceMatrix[i],key=comparator)
            minInColumn = min(distanceMatrix[:][i],key=comparator)

            lowerLimit += minInRow if minInRow else 0
            lowerLimit += minInColumn if minInColumn else 0

            for j in range(0,rang):
                distanceMatrix[i][j] = distanceMatrix[i][j] - minInRow if distanceMatrix[i][j] and minInColumn else None
                distanceMatrix[j][i] = distanceMatrix[j][i] - minInColumn if distanceMatrix[j][i] and minInRow else None
        # zeroWeidthSet = [(i,j) for i in range(0,rang) for j in range(0,rang) if distanceMatrix[i][j] == 0]
        Gij = {}
        for point in [(i,j) for i in range(0,rang) for j in range(0,rang) if distanceMatrix[i][j] == 0]:
            distanceMatrix[point[0]][point[1]] = None
            Gij[point] = min(distanceMatrix[point[0]],key=comparator) + min(distanceMatrix[:][point[1]],key=comparator)
            distanceMatrix[point[0]][point[1]] = 0
        maxGij = max(Gij,key=lambda key: Gij[key])

        for i in range(0,rang):
            distanceMatrix[maxGij[0]][i] = distanceMatrix[i][maxGij[1]] = None

        distanceMatrix[maxGij[0]][maxGij[1]] = None
        for str in distanceMatrix: print(str)
        print('#'*255)
    print(round(lowerLimit,2))
    return 0.0

print(golf({(2, 2), (2, 8), (8, 8), (8, 2), (5, 5)}) == 23.31)
print(golf({(2, 2), (4, 4), (6, 6), (8, 8), (9, 9)}) == 12.73)