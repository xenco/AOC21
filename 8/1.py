#!/usr/bin/python3
print(sum([len([y for y in x.split("|")[1].split() if len(y) in [2, 3, 4, 7]]) for x in open("input").readlines()]))
