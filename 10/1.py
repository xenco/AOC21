#!/usr/bin/python3

lines = [l.strip() for l in open("input").readlines()]
s = 0

for (i, line) in enumerate(lines):
    correct = True

    opening_brackets = ['(', '[', '{', '<']
    closing_brackets = [')', ']', '}', '>']

    stack = []
    for (j, c) in enumerate(line):
        if c in opening_brackets:
            stack.append(c)
        else:
            for (k, cb) in enumerate(closing_brackets):
                if c == cb:
                    if stack[-1] != opening_brackets[k]:
                        print("Syntax error on line %s,%s: Expected %s but found %s" % (i + 1, j, cb, stack[-1]))
                        if cb == ')':
                            s += 3
                        elif cb == ']':
                            s += 57
                        elif cb == '}':
                            s += 1197
                        elif cb == '>':
                            s += 25137
                    stack.pop()

    if correct:
        print(f"\033[1m\033[92m%s\033[0m" % line)
    else:
        print(f"\033[1m\033[93m%s\033[0m" % line)

print(s)