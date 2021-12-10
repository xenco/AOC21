h = v = a = 0

with open("input") as f:
    dirs = [x.strip().split() for x in f.readlines()]

for d, x in dirs:
    y = int(x)
    if d == "forward": h += y;v += y * a
    if d == "up": a -= y
    if d == "down": a += y

print(h * v)
