#!/usr/bin/python3

s, rules = open("input").read().strip().split("\n\n")
rules = {str(r.split(" -> ")[0]): r.split(" -> ")[1] for r in rules.split("\n")}

print(s)

for (i, c) in enumerate(s):
    print(c, end=' ')
print()
for (i, c) in enumerate(s):
    print(i, end=' ')
print()

num_steps = 10
for step in range(num_steps):
    i = 0
    while i + 1 <= len(s) - 1:
        r = str(s[i]) + str(s[i + 1])
        if r in rules:
            s = s[:i + 1] + rules[r] + s[i + 1:]
            i += 2
        else:
            i += 1
    print("After step %s: [len=%s] %s" % (step + 1, len(s), ''))

unique_chars = set([c for c in s])
x = {}
for c in unique_chars:
    x[s.n(c)] = c

print(max(x) - min(x))