__author__ = 'Pavel.Malko'
def flat_list(a):
    r = []
    def f(a):
        for i in a:
          r.append(i) if type(i) == int else f(i)
    f(a)
    return r

print(flat_list([1, 2, 3]))
print(flat_list([1, [2, 2, 2], 4]))
print(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]))
print(flat_list([-1, [1, [-2], 1], -1]))