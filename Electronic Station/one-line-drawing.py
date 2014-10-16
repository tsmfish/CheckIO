__author__ = 'Pavel.Malko'
def draw(segments):
    def printMatrix(matrix):
        """

        :param Dict: matrix:
        :return: None
        Print distance matrix.
        """
        print('\t'+'\t'.join(sorted(matrix.keys())))
        for pointY, cortege in sorted(matrix.items()):
            print(pointY+'\t'+'\t'.join([str(path[1]) for path in sorted(cortege.items())]))

    def hasLink(matrix):
        """

        :param matrix: distance matrix
        :return: True if one or more link available
        """
        for point1 in matrix:
            if [link for poin2, link in matrix[point1].items() if link == 1]:
                return True
        return False

    def dictCopy(source):
        """

        :param source: dictionary for copy
        :return: copy of source.
        """
        deststination = {}
        for key1, value1 in source.items():
            deststination[key1] = {}
            for key2, value2 in value1.items():
                deststination[key1][key2] = 1 if value2 else 0
        return deststination

    distanceMatrix = {}
    for x1, y1, x2, y2 in segments:
        distanceMatrix.setdefault('%d:%d'%(x1, y1), {})['%d:%d'%(x2, y2)] = 1
        distanceMatrix.setdefault('%d:%d'%(x2, y2), {})['%d:%d'%(x1, y1)] = 1
    points = distanceMatrix.keys()
    for point1 in points:
        for point2 in points:
            if point2 not in distanceMatrix[point1]: distanceMatrix[point1][point2] = 0
    # printMatrix(distanceMatrix)

    for point in points:
        solution = [{'point': point,
                     'distances': distanceMatrix,
                     'visited': [],
                     'unvisited': [p1 for p1 in distanceMatrix[point] if distanceMatrix[point][p1] == 1]}]
        # print('Start from: ' + point)
        while not (not solution[0]['unvisited'] and len(solution) == 1):
            # если есть пути в непосещённый вершины - идём в них
            if [p for p in solution[-1]['unvisited'] if solution[-1]['distances'][solution[-1]['point']][p]]:
                # выбираем непосещённую вершину
                step = solution[-1]['unvisited'].pop()
                # помечаем выбранную как посещённую
                solution[-1]['visited'].append(step)
                newDistances = dictCopy(solution[-1]['distances'])
                # в новой матрице связности удаляем пути от предыдущей до выбраной
                newDistances[step][solution[-1]['point']], newDistances[solution[-1]['point']][step] = 0, 0
                solution.append({'point': step,
                                 'distances': newDistances,
                                 'visited': [],
                                 'unvisited': [p1 for p1 in newDistances[step] if newDistances[step][p1] == 1]})
                # print('Step to: ' + step)
            else:
                # если путей из текущей вершины в другие - нет то:
                # проверим есть ли вообще пути в графе
                if hasLink(solution[-1]['distances']):
                    # пути есть - значит мы не нарисовали всю фигуру и пришли в тупик. Возвращаемся на предыдущий шаг
                    # print('Step back.')
                    solution.pop(-1)
                else:
                    # мы использовали все пути - а следовательно нарисовали фигурур. Составляем полученный маршрут и выдаём ответ
                    # print('Solution: '+'->'.join([repr(step['point'].split(':')) for step in solution]))
                    return [step['point'].split(':') for step in solution]
    return []

# print(draw([(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5)]))
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def checker(func, in_data, is_possible=True):
        user_result = func(in_data)
        if not is_possible:
            if user_result:
                print("How did you draw this?")
                return False
            else:
                return True
        if len(user_result) < 2:
            print("More points please.")
            return False
        data = list(in_data)
        for i in range(len(user_result) - 1):
            f, s = user_result[i], user_result[i + 1]
            if (f + s) in data:
                data.remove(f + s)
            elif (s + f) in data:
                data.remove(s + f)
            else:
                print("The wrong segment {}.".format(f + s))
                return False
        if data:
            print("You forgot about {}.".format(data[0]))
            return False
        return True

    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5)}), "Example 1"
    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7),
                    (4, 7, 7, 5), (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2)},
                   False), "Example 2"
    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5),
                    (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2), (1, 5, 7, 5)}), "Example 3"
