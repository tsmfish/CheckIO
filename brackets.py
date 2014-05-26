__author__ = 'Pavel.Malko'
def checkio(expression):
    bracketAdapter = {')':'(',']':'[','}':'{'}

    bracketStack = []
    for symbol in expression:
        if symbol in ('[', '{', '('):
            bracketStack.append(symbol)
        if symbol in (']', '}', ')') and \
                     (len(bracketStack) == 0 or bracketAdapter[symbol] != bracketStack.pop()):
            return False
    return len(bracketStack) == 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
