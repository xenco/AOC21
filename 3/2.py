#!/usr/bin/python3

def countAtPosition(nu, pos, sig):
    h, l = sum([1 for n in nu if int(n[pos])]), sum([1 for n in nu if not int(n[pos])])
    return sig if h == l else int(h > l) if sig else int(not h > l)


no = nc = [x for x in open("input").read().split()]
for pos in range(len(no[0])):
    if len(no) > 1: no = [n for n in no if int(n[pos]) == countAtPosition(no, pos, 1)]
    if len(nc) > 1: nc = [n for n in nc if int(n[pos]) == countAtPosition(nc, pos, 0)]

print(int(no[0], 2) * int(nc[0], 2))
