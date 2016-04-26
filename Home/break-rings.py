__author__ = 'Pavel.Malko'

def break_rings(rings):
    def get_assiciocion_list (rings):
        associationList = {}
        for left, rigth in rings:
            associationList.setdefault(left, []).append(rigth)
            associationList.setdefault(rigth, []).append(left)
        return associationList

    def destroy_ring(list, ring):
        new_list, destroy_query = {name: value[:] for name, value in list.items() if name != ring}, []
        for rings in new_list.values():
            if ring in rings: rings.remove(ring)

        return {name: value for name, value in new_list.items() if value}

    def destroer(associoacionList, destroyed):
        if not associoacionList: return destroyed
        ring_count = len(associoacionList)
        ratingRings = {ring:ring_count - len(destroy_ring(associoacionList, ring)) for ring in associoacionList}

        return destroer(destroy_ring(associoacionList, max(ratingRings.items(), key=lambda key:key[1])[0]), destroyed+1)

    return destroer(get_assiciocion_list(rings), 0)

print(break_rings(({1,9},{1,2},{8,5},{4,6},{5,6},{8,1},{3,4},{2,6},{9,6},{8,4},{8,3},{5,7},{9,7},{2,3},{1,7},)))
print(break_rings(({3,4},{5,6},{2,7},{1,5},{2,6},{8,4},{1,7},{4,5},{9,5},{2,3},{8,2},{2,4},{9,6},{5,7},{3,6},{1,3},)))
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 5}, {3, 6})) == 2, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
    assert break_rings(({1,9},{1,2},{8,5},{4,6},{5,6},{8,1},{3,4},{2,6},{9,6},{8,4},{8,3},{5,7},{9,7},{2,3},{1,7})) == 5, "Extra test 4/4"
