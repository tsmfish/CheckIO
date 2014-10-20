__author__ = 'Pavel.Malko'
def checkio(teleports_string):

    def getDistances(teleports):
    #     create distance matrix
        matrix = [[0 for j in range(8)] for i in range(8)]
        for teleport in teleports.split(','):
            src, dst = int(teleport[0])-1, int(teleport[1])-1
            matrix[src][dst] = 1
            matrix[dst][src] = 1

        return matrix

    def copyDict(src):
        copy = [[] for i in range(len(src))]
        for p1 in range(len(src)):
            copy[p1] = [[] for i in range(len(src))]
            for p2 in range(len(src)):
                copy[p1][p2] = 1 if src[p1][p2] else 0
        return copy

    distances = getDistances(teleports_string)
    rang = len(distances)

    solution = []
    fullVisited = [i for i in range(rang)]

    for startPoint in range(len(distances)):
        solution.append({'point': startPoint,
                         'visited':[startPoint],
                         'tray': [],
                         'untray': [p1 for p1 in range(rang) if distances[startPoint][p1] == 1],
                         'distances': copyDict(distances),
                         'path': [startPoint]})
        while solution:
            # if oll teleports visited, then path equal ansver
            if sorted(solution[-1]['visited']) == fullVisited:
                print(''.join([str(i+1) for i in solution[-1]['path']]))
                return ''.join([str(i+1) for i in solution[-1]['path']])
            # check is wae have teleport from this ?
            if solution[-1]['untray']:
                # tray next step
                newStep = solution[-1]['untray'].pop()
                newDistances = copyDict(solution[-1]['distances'])
                newDistances[solution[-1]['point']][newStep], newDistances[newStep][solution[-1]['point']] = 0,0
                newVisited = solution[-1]['visited'][:]
                if newStep not in newVisited:
                    newVisited.append(newStep)
                newPath = solution[-1]['path']
                newPath.append(newStep)
                solution[-1]['tray'].append(newStep)
                solution.append({
                    'point': newStep,
                    'visited': newVisited,
                    'tray': [],
                    'untray': [p1 for p1 in range(rang) if solution[-1]['distances'][newStep][p1] == 1],
                    'distances': newDistances,
                    'path': newPath
                })
            else:
                solution.pop(-1)
    return ""

#This part is using only for self-testing
if __name__ == "__main__":
    def check_solution(func, teleports_str):
        route = func(teleports_str)
        teleports_map = [tuple(sorted([int(x), int(y)])) for x, y in teleports_str.split(",")]
        if route[0] != '1' or route[-1] != '1':
            print("The path must start and end at 1")
            return False
        ch_route = route[0]
        for i in range(len(route) - 1):
            teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
            if not teleport in teleports_map:
                print("No way from {0} to {1}".format(route[i], route[i + 1]))
                return False
            teleports_map.remove(teleport)
            ch_route += route[i + 1]
        for s in range(1, 9):
            if not str(s) in ch_route:
                print("You forgot about {0}".format(s))
                return False
        return True

    assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
    assert check_solution(checkio, "12,28,87,71,13,14,34,35,45,46,63,65"), "Second"
    assert check_solution(checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"), "Third"
    assert check_solution(checkio, "13,14,23,25,34,35,47,56,58,76,68"), "Fourth"