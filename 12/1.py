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
        elif v.isupper() or v not in path:
            path.append(v)
            paths(v, dst, path)
            path.pop()


paths('start', 'end', ['start'])
print(len(valid_paths))
