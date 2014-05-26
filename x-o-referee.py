__author__ = 'Pavel.Malko'
def checkio(game_result):
    for sign in ("X","O"):
        win = [sign for i in range(0,3)]

        if [game_result[n][n] for n in range(0,3)] == win: return str(sign)
        if [game_result[len(game_result)-n-1][n] for n in range(0,3)] == win: return str(sign)
        for i in range(0,3):
            if [game_result[i][n] for n in range(0,3)] == win: return str(sign)
            if [game_result[n][i] for n in range(0,3)] == win: return str(sign)
    return "D"

print(checkio([
        "X.O",
        "XX.",
        "XOO"]))
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

