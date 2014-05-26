import math

__author__ = 'Pavel.Malko'
def checkio(n, m):
    return [str(((n & (1 << i)) ^ (m & (1 << i)))>>i) for i in range(0,math.ceil(math.log2(max(n,m)))+1)].count('1')

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
