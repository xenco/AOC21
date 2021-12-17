#!/usr/bin/python3

import copy
from heapq import heappush, heappop

MAX_X = None
MAX_Y = None


class Node:
    def __init__(self, position, weight, parent=None):
        self.position = position
        self.parent = parent
        self.g = weight
        self.h = 0
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.position[0] == other.position[0] and self.position[1] == other.position[1]

    def __hash__(self):
        return int(str(self.position[0] + self.position[1]))

    def __lt__(self, other):
        return self.f < other.f

    def __cmp__(self, other):
        return self.f < other.f

    def get_path(self):
        path = []
        cur = self
        while cur.parent is not None:
            path.append(cur)
            cur = cur.parent
        return path


def astar(field, start, end):
    openlist = []
    closedlist = set([])

    heappush(openlist, start)

    while len(openlist):
        current_node = heappop(openlist)
        closedlist.add(current_node)

        if current_node == end:
            return current_node

        neighbors = []
        (x, y) = current_node.position
        for (nx, ny) in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
            if (0 <= ny <= MAX_Y) and (0 <= nx <= MAX_X):
                neighbors.append(Node((nx, ny), current_node.g + field[ny][nx], current_node))

        for neighbor in neighbors:
            neighbor_next_cost = neighbor.g

            if neighbor not in openlist and neighbor not in closedlist:
                heappush(openlist, neighbor)
            elif neighbor in openlist and current_node.g <= neighbor_next_cost:
                neighbor.h = abs(neighbor.position[0] - end.position[0]) + abs(neighbor.position[1] - end.position[1])
                closedlist.add(current_node)
            elif neighbor in closedlist and neighbor.g < neighbor_next_cost:
                closedlist.remove(neighbor)
                heappush(openlist, neighbor)

            neighbor.g = neighbor_next_cost
            neighbor.f = neighbor.g + neighbor.h

            neighbor.parent = current_node


def print_field(field):
    for y in range(MAX_Y + 1):
        for x in range(MAX_X + 1):
            print(field[y][x], end=('\t' if x > 0 and x % 10 == 0 else ''))
        print()
        if y > 0 and y % 10 == 0: print()


if __name__ == "__main__":
    base_field = [[int(x) for x in y.strip()] for y in open("input").readlines()]
    field = copy.deepcopy(base_field)

    copy_field = copy.deepcopy(field)
    for k in range(4):
        for row in copy_field:
            new_row = []
            for x in row:
                n = x + k + 1
                while n > 9: n -= 9
                new_row.append(n)
            field.append(new_row)

    for (i, row) in enumerate(field):
        for k in range(4):
            n_col = []
            for x in field[i][:100]:
                n = x + k + 1
                while n > 9: n -= 9
                n_col.append(n)
            field[i] += n_col

    MAX_Y = len(field) - 1
    MAX_X = len(field[0]) - 1

    # print_field(field)

    start = Node((0, 0), 0, None)
    end = astar(
        field,
        start,
        Node((MAX_X, MAX_Y), field[MAX_Y][MAX_X], None)
    )

    print(end.get_path()[0].g)
