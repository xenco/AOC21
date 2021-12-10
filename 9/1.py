#!/usr/bin/python3

field = [[int(x) for x in y.strip()] for y in open("input").readlines()]

lp = []

for y in range(len(field)):
    for x in range(len(field[y])):
        cur = field[y][x]
        top = field[y - 1][x] if y - 1 >= 0 else None
        bottom = field[y + 1][x] if y + 1 <= len(field) - 1 else None
        left = field[y][x - 1] if x - 1 >= 0 else None
        right = field[y][x + 1] if x + 1 <= len(field[y]) - 1 else None

        top_larger = (top is None or top > cur)
        left_larger = (left is None or left > cur)
        bottom_larger = (bottom is None or bottom > cur)
        right_larger = (right is None or right > cur)

        if top_larger and left_larger and right_larger and bottom_larger:
            lp.append(cur)
            print(f"\033[1m\033[92m%s\033[0m" % cur, end=' ')
        else:
            print(cur, end=' ')
    print()

print(sum([l + 1 for l in lp]))