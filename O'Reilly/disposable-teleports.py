__author__ = 'Pavel.Malko'
def checkio(teleports_string):

    def getAdjacencyMatrix(teleports):
        dict = {}
        for link in teleports.split(','):
            p1, p2 = int(link[0])-1, int(link[1])-1
            dict.setdefault(p1, []).append(p2)
            dict.setdefault(p2, []).append(p1)
        return sorted(dict.keys()), [item[1] for item in sorted(dict.items(), key=lambda item:item[0])]

    def copyAdjacency(src):
        dest = []
        for neighborhood in src:
            dest.append(neighborhood[:])
        return dest

    nodes, adjacency = getAdjacencyMatrix(teleports_string)
    solution = [{
        'node': 0,
        'visited': [],
        'unvisited': list(adjacency[0]),
        'path': [0],
        'adjacency': adjacency
    }]

    while (len(solution) != 1) or solution[0]['unvisited']:
        if set(nodes) == set (solution[-1]['path']):
            if solution[0]['node'] in solution[-1]['adjacency'][solution[-1]['node']]:
                # print(''.join([str(node+1) for node in solution[-1]['path']]) + '1')
                return ''.join([str(node+1) for node in solution[-1]['path']]) + '1'
            else:
                solution.pop(-1)
        else:
            if solution[-1]['unvisited']:
                # step front
                newNode = solution[-1]['unvisited'].pop(0)
                solution[-1]['visited'].append(newNode)
                newPath = list(solution[-1]['path'][:])
                newPath.append(newNode) # TODO
                newAdjacency = copyAdjacency(solution[-1]['adjacency'])
                newAdjacency[solution[-1]['node']].remove(newNode)
                newAdjacency[newNode].remove(solution[-1]['node'])
                solution.append({
                    'node': newNode,
                    'visited': [],
                    'unvisited': list(newAdjacency[newNode]),
                    'path': newPath,
                    'adjacency': newAdjacency
                })
            else:
                # step back
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

    print(checkio("12,23,34,45,56,67,78,81"))
    print(checkio("12,28,87,71,13,14,34,35,45,46,63,65"))
    print(checkio("12,15,16,23,24,28,83,85,86,87,71,74,56"))
    print(checkio("13,14,23,25,34,35,47,56,58,76,68"))

    assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
    assert check_solution(checkio, "12,28,87,71,13,14,34,35,45,46,63,65"), "Second"
    assert check_solution(checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"), "Third"
    assert check_solution(checkio, "13,14,23,25,34,35,47,56,58,76,68"), "Fourth"