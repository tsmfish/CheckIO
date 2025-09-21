def follow_ghost_legs(n: int, legs: list[tuple[int, int]]) -> list[int]:
    result = list(range(1, n+1))

    for ia,ib in legs:
        result[ib-1], result[ia-1] = result[ia-1], result[ib-1]

    return result


print("Example:")
print(follow_ghost_legs(3, [(1, 2), (2, 3), (1, 2)]))

# These "asserts" are used for self-checking
assert follow_ghost_legs(3, [(1, 2), (2, 3), (1, 2)]) == [3, 2, 1]
assert follow_ghost_legs(4, [(2, 3), (1, 2), (2, 3), (3, 4)]) == [3, 2, 4, 1]
assert follow_ghost_legs(5, [(3, 4), (4, 5), (3, 4), (2, 3), (3, 4)]) == [1, 5, 4, 2, 3]
assert follow_ghost_legs(6, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]) == [
    2,
    3,
    4,
    5,
    6,
    1,
]

print("The mission is done! Click 'Check Solution' to earn rewards!")
