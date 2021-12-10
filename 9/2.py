#!/usr/bin/python3

field = [[int(x) for x in y.strip()] for y in open("input").readlines()]


def find_low_points():
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
                lp.append((x, y))
    return lp


def print_field(field, basins):
    for y in range(len(field)):
        for x in range(len(field[y])):
            p = False
            for b in basins:
                if (x, y) in b:
                    if (x, y) in lp:
                        print(f"\033[1m\033[92m%s\033[0m" % field[y][x], end=' ')
                    else:
                        print(f"\033[1m\033[93m%s\033[0m" % field[y][x], end=' ')
                    p = True
                    break
            if not p:
                print(field[y][x], end=' ')
        print()


def mark_basins(field, lp):
    basins = [[p] for p in lp]

    for (i, basin) in enumerate(basins):
        queue = []
        queue_visited = []
        for b in basin:
            queue.append(b)

        while len(queue) > 0:
            cur = queue.pop(0)

            if not cur in basins[i]:
                basins[i].append(cur)

            for dir in [
                (1, 0),  # right
                (-1, 0),  # left
                (0, -1),  # up
                (0, 1),  # down
            ]:
                cx, cy = cur
                while True:
                    cx += dir[0]
                    cy += dir[1]

                    if cy < 0 or cy > len(field) - 1: break
                    if cx < 0 or cx > len(field[cy]) - 1: break

                    p = field[cy][cx]
                    if p == 9: break

                    if not (cx, cy)in basins[i]:
                        basins[i].append((cx, cy))

                    if not (cx, cy) in queue_visited:
                        queue.append((cx, cy))

            queue_visited.append(cur)

    return basins


lp = find_low_points()
basins = mark_basins(field, lp)
print_field(field, basins)

res = 1
for x in sorted(basins, key=len, reverse=True)[:3]:
    res *= len(x)
print(res)