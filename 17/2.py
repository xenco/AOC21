#!/usr/bin/python3
import copy
import re

xmin, xmax, ymin, ymax = [int(a) for a in re \
    .compile(r"target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)") \
    .findall(open("input").read().strip())[0]]

results = []
for v_x in list(range(1000)):
    for v_y in list(range(-1000, 1000)):
        probe_x, probe_y = 0, 0
        step_vx, step_vy = copy.deepcopy(v_x), copy.deepcopy(v_y)

        while probe_x <= xmax and probe_y >= ymax:
            probe_x += step_vx
            probe_y += step_vy

            if xmin <= probe_x <= xmax and ymin <= probe_y <= ymax:
                results += [(v_x, v_y)]

            if step_vx > 0:
                step_vx -= 1
            else:
                step_vx += 1

            step_vy -= 1

print(len(results))
