#!/usr/bin/python3

fishies = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(9):
    fishies[i] = len([x for x in [int(x) for x in open("input").read().split(",")] if x == i])

for d in range(256):
    fishies = fishies[1:] + fishies[0:1]
    fishies[6] += fishies[-1]

print(sum(fishies))