#!/usr/bin/python3

lines = [l.strip() for l in open("input").readlines()]

opening_brackets = ['(', '[', '{', '<']
closing_brackets = [')', ']', '}', '>']


def check_line(l):
    stack = []
    for (j, c) in enumerate(l):
        if c in opening_brackets:
            stack.append(c)
        else:
            for (k, cb) in enumerate(closing_brackets):
                if c == cb:
                    if stack[-1] != opening_brackets[k]:
                        return False
                    stack.pop()
    return True


def complete_line(l):
    s = 0

    while '()' in l or '[]' in l or '{}' in l or '<>' in l:
        l = l.replace('()', '')
        l = l.replace('[]', '')
        l = l.replace('{}', '')
        l = l.replace('<>', '')

    for c in reversed(l):
        matching_bracket = closing_brackets[opening_brackets.index(c)]

        s *= 5
        if matching_bracket == ')':
            s += 1
        if matching_bracket == ']':
            s += 2
        if matching_bracket == '}':
            s += 3
        if matching_bracket == '>':
            s += 4

    return s


valid_lines = [l for l in lines if check_line(l)]

scores = []
for line in valid_lines:
    scores.append(complete_line(line))

print(sorted(scores)[int(len(scores) / 2)])
