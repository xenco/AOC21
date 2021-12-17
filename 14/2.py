#!/usr/bin/python3

s, rules = open("input").read().strip().split("\n\n")
rules = {str(r.split(" -> ")[0]): r.split(" -> ")[1] for r in rules.split("\n")}

elements, pairs = {}, {}

for c in s:
    if c not in elements:
        elements[c] = 0
    elements[c] += 1

for i in range(len(s) - 1):
    index = s[i:i + 2]
    if index not in pairs:
        pairs[index] = 0
    pairs[index] += 1

for _ in range(40):
    for (pair, n) in list(pairs.items()):
        if pair in rules:
            r = rules[pair]

            if r not in elements:
                elements[r] = 0
            elements[r] += n

            if pair not in pairs:
                pairs[pair] = 0
            pairs[pair] -= n

            split1, split2 = pair[0] + r, r + pair[1]

            if split1 not in pairs:
                pairs[split1] = 0
            pairs[split1] += n

            if split2 not in pairs:
                pairs[split2] = 0
            pairs[split2] += n

print(max(elements.values()) - min(elements.values()))
