__author__ = 'Pavel.Malko'

def break_rings(rings):
    vector = {}
    for left, rigth in rings:
        vector.setdefault(left, []).append(rigth)
        vector.setdefault(rigth, []).append(left)
    braked = []

    while vector:
        maximumConnected = 0
        for connected in vector.values():
            if len(connected) > maximumConnected: maximumConnected = len(connected)
        desigonsList = {key: {'connected':len(connected), 'free':0} for key, connected in vector.items() if len(connected) == maximumConnected}
        for key, desigon in desigonsList.items():
            # copy connection tree
            newVector = {item: connections[:] for item, connections in vector.items()}
            newVector.pop(key)
            for ring, connectedRing in newVector.items():
                if key in connectedRing:
                    connectedRing.remove(key)
                    if not connectedRing:
                        desigonsList[key]['free'] += 1

        toBreak = max(desigonsList.items(), key=lambda key:key[1]['free'])[0]
        vector.pop(toBreak)
        toRemove = []
        for key, connections in vector.items():
            if toBreak in connections:
                connections.remove(toBreak)
                if not connections:
                    toRemove.append(key)
        for key in toRemove:
            vector.pop(key)

        braked.append(toBreak)

    print(braked)
    return len(braked)

print(break_rings(({1,9},{1,2},{8,5},{4,6},{5,6},{8,1},{3,4},{2,6},{9,6},{8,4},{8,3},{5,7},{9,7},{2,3},{1,7},)))
print(break_rings(({3,4},{5,6},{2,7},{1,5},{2,6},{8,4},{1,7},{4,5},{9,5},{2,3},{8,2},{2,4},{9,6},{5,7},{3,6},{1,3},)))
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 5}, {3, 6})) == 2, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
    assert break_rings(({1,9},{1,2},{8,5},{4,6},{5,6},{8,1},{3,4},{2,6},{9,6},{8,4},{8,3},{5,7},{9,7},{2,3},{1,7})) == 5, "Extra test 4/4"
