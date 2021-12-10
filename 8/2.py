#!/usr/bin/python3

def chars_in(s1, s2):
    return all([c in s1 for c in s2]) if len(s1) > len(s2) else all([c in s2 for c in s1])


def get_num(s, known={}):
    l = len(s)

    if l == 2:
        return 1
    elif l == 3:
        return 7
    elif l == 4:
        return 4
    elif l == 7:
        return 8
    elif l == 5:
        try:
            if chars_in(s, known[1]):
                return 3
            elif not chars_in(s, known[6]):
                return 2
            elif chars_in(s, known[6]):
                return 5
        except:
            return None
    elif l == 6:
        if chars_in(s, known[4]) and chars_in(s, known[7]):
            return 9
        elif not chars_in(s, known[4]) and chars_in(s, known[1]) and chars_in(s, known[8]):
            return 0
        else:
            return 6


def build_known(line, k=None):
    if not k:
        k = {get_num(i): i for i in line.split("|")[0].split() if len(i) in [2, 3, 4, 7]}

    for x in range(10):
        for o in line.split("|")[1].split() + line.split("|")[0].split():
            try:
                num = get_num(o, k)
                if num and num not in k:
                    k[num] = o
            except:
                pass

    return k


s = 0
for line in open("input").readlines():
    s += int(''.join([str(get_num(output, build_known(line))) for output in line.split("|")[1].split()]))

print(s)
