#!/usr/bin/python3
nu = [x for x in open("input").read().split()]


def countAtPosition(pos, sig):
    h, l = sum([1 for n in nu if int(n[pos])]), sum([1 for n in nu if not int(n[pos])])
    return str(int(h > l)) if sig else str(int(not h > l))


g = e = ''
for pos in range(len(nu[0])):
    g += countAtPosition(pos, 1)
    e += countAtPosition(pos, 0)

print(int(g, 2) * int(e, 2))
