#!/usr/bin/python3
import os

field = [[int(x) for x in y.strip()] for y in open("input").readlines()]

flashes = 0
step = 0

max_y = len(field)
max_x = len(field[0])


def print_field(field, flashed):
    for y in range(max_y):
        for x in range(max_x):
            if (x, y) in flashed:
                print(f"\033[1m\033[92m%s\033[0m" % field[y][x], end=' ')
            else:
                print(field[y][x], end=' ')
        print()


while True:
    step += 1

    flashed = []

    for y in range(max_y):
        for x in range(max_x):
            field[y][x] += 1

    for y in range(max_y):
        for x in range(max_x):
            queue = [(x, y)]

            while len(queue):
                cur_x, cur_y = queue.pop(0)

                if field[cur_y][cur_x] > 9 and (cur_x, cur_y) not in flashed:
                    flashed.append((cur_x, cur_y))
                    flashes += 1

                    for (dx, dy) in [
                        (-1, -1),  # top-left
                        (0, -1),  # top
                        (1, -1),  # top-right
                        (-1, 0),  # left
                        (1, 0),  # right
                        (-1, 1),  # bottom-left
                        (0, 1),  # bottom
                        (1, 1),  # bottom-right
                    ]:
                        if 0 <= cur_x + dx <= max_x - 1 and 0 <= cur_y + dy <= max_y - 1:
                            n = (cur_x + dx, cur_y + dy)
                            field[cur_y + dy][cur_x + dx] += 1
                            queue.append(n)

    for fx, fy in flashed:
        field[fy][fx] = 0

    os.system('clear')
    print("AFTER STEP: %s - Flashes: %s" % (step, flashes))
    print_field(field, flashed)

    if step == 100: break
