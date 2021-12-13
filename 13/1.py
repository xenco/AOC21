#!/usr/bin/python3

points, instructions = open("input").read().split("\n\n")
points = [[int(point.strip().split(",")[0]), int(point.strip().split(",")[1])] for point in points.split()]
instructions = [[instruction.split("=")[0], int(instruction.split("=")[1])] for instruction in
                instructions.strip().replace("fold along ", "").split()]

max_x = max([p[0] for p in points]) + 1
max_y = max([p[1] for p in points]) + 1


def build_field():
    field = [['.'] * max_x for _ in range(max_y)]
    for p in points:
        field[p[1]][p[0]] = '#'
    return field


def print_field(field):
    for y in range(len(field)):
        for x in range(len(field[y])):
            print(field[y][x], end='')
        print()


def fold_field(f, dir, pos):
    if dir == 'y':
        for y in range(pos + 1, len(f)):
            for x in range(len(f[y])):
                new_y = 2 * pos - y
                if f[new_y][x] == '.':
                    f[new_y][x] = f[y][x]
        f = f[:pos]
    elif dir == 'x':
        for y in range(len(f)):
            for x in range(pos + 1, len(f[y])):
                new_x = 2 * pos - x
                if f[y][new_x] == '.':
                    f[y][new_x] = f[y][x]
            f[y] = f[y][:pos]
    return f


field = build_field()

for [dir, pos] in instructions:
    field = fold_field(field, dir, pos)
    break

s = 0
for y in range(len(field)):
    for x in range(len(field[y])):
        s += 1 if field[y][x] == '#' else 0

print(s)