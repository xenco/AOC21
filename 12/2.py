#!/usr/bin/python3

graph = {}
for (k, v) in [x.strip().split("-") for x in open("input").readlines()]:
    if k not in graph: graph[k] = []
    if v not in graph[k]: graph[k].append(v)
    if v not in graph: graph[v] = [k]
    if k not in graph[v]: graph[v].append(k)

valid_paths = []


def paths(src, dst, path):
    for v in graph[src]:
        if v == dst:
            valid_paths.append(path + [dst])
        else:
            if v != 'start' and (v not in path or (v in path and (v.isupper() or (
                    len([x for x in path if x == v]) < 2 and len(
                    [x for x in path if x.islower() and x not in [v, 'start', 'end'] and path.count(x) > 1]) == 0)))):
                path.append(v)
                paths(v, dst, path)
                path.pop()


paths('start', 'end', ['start'])
print(len(valid_paths))
