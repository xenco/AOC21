#!/usr/bin/python3

def get_lines():
    lines = []

    for line in open("input").readlines():
        s, e = line.split("->")
        s = [int(x) for x in s.strip().split(",")]
        e = [int(x) for x in e.strip().split(",")]

        if s[0] == e[0] or s[1] == e[1]:
            lines.append({"x1": s[0], "y1": s[1], "x2": e[0], "y2": e[1]})

    return lines


def get_field_size(lines):
    max_x = 0
    max_y = 0
    for l in lines:
        if l["x1"] > max_x: max_x = l["x1"]
        if l["x2"] > max_x: max_x = l["x2"]
        if l["y1"] > max_y: max_y = l["y1"]
        if l["y2"] > max_y: max_y = l["y2"]
    return max_x, max_y


def draw_line(field, x1, y1, x2, y2):
    dx = abs(x2 - x1)
    sx = 1 if x1 < x2 else -1
    dy = -abs(y2 - y1)
    sy = 1 if y1 < y2 else -1
    err = dx + dy
    while True:
        field[y1][x1] += 1

        if x1 == x2 and y1 == y2: break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x1 += sx
        if e2 <= dx:
            err += dx
            y1 += sy

    return field


def print_field(field, max_x, max_y):
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print("." if field[y][x] == 0 else field[y][x], end=' ')
        print()


lines = get_lines()
max_x, max_y = get_field_size(lines)
field = [[0 for x in range(max_x + 1)] for y in range(max_y + 1)]

for line in lines:
    field = draw_line(field, line["x1"], line["y1"], line["x2"], line["y2"])

print(sum([1 if field[y][x] > 1 else 0 for x in range(max_x + 1) for y in range(max_y + 1)]))
