__author__ = 'Pavel.Malko'
def safe_pawns(pawns):
    safePawns = 0
    a2i = {value: index for index, value in enumerate("abcdefgh")}
    i2a = {index: value for index, value in enumerate("abcdefgh")}

    for pawn in pawns:
        row, col = a2i[pawn[0]], int(pawn[1])-1
        if col in range(8) and \
            (row-1 in i2a and i2a[row-1]+str(col) in pawns) or \
            (row+1 in i2a and i2a[row+1]+str(col) in pawns):
            safePawns += 1
    return safePawns

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1


