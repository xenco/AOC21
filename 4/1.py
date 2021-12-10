#!/usr/bin/python3
import os

input_raw = open("input").readlines()
numbers = [int(x.strip()) for x in input_raw[0].split(",")]


def get_fields():
    all_fields = [int(y) for x in input_raw[1:] for n in x.split("\n") for y in n.strip().split() if n != '']
    num_fields = int(len(all_fields) / 25)
    fields = [[[{"num": 0, "hit": False} for y in range(5)] for x in range(5)] for a in range(num_fields)]

    c = 0
    for i in range(0, len(all_fields) - 1, 25):
        for j in range(5):
            fields[c][j] = [{"num": n, "hit": False} for n in all_fields[i + j * 5:i + j * 5 + 5]]
        c += 1

    return fields


def check_win(field):
    row_count = 0
    for y in range(5):
        for x in range(5):
            row_count += int(field[y][x]["hit"])
        if row_count == 5:
            return True
        row_count = 0

    col_count = 0
    for x in range(5):
        for y in range(5):
            col_count += int(field[y][x]["hit"])
        if col_count == 5:
            return True
        col_count = 0


def mark_field(num, field):
    for y in range(5):
        for x in range(5):
            if field[y][x]["num"] == num:
                field[y][x]["hit"] = True
    return field


def print_field(num, field):
    for y in range(5):
        for x in range(5):
            format = f"\033[4m\033[1m\033[92m%s\033[0m" if num == field[y][x]["num"] else f"\033[1m\033[93m%s\033[0m"
            print((format if field[y][x]["hit"] else "%s") % field[y][x]["num"], end='\t')
        print()


drawn_numbers = []
fields = get_fields()

for num in numbers:
    drawn_numbers.append(num)

    os.system('clear')
    print("DRAWN: %s" % num)
    print("DRAWN NUMBERS: %s" % drawn_numbers)

    for field in fields:
        field = mark_field(num, field)
        print_field(num, field)
        print()

        if check_win(field):
            not_hit = []
            for y in range(5):
                for x in range(5):
                    if not field[y][x]["hit"]:
                        not_hit.append(field[y][x]["num"])

            print("!WIN!", sum(not_hit), num, sum(not_hit) * num)
            exit(0)

    print("Draw next number ... ", end='')
    # input()
