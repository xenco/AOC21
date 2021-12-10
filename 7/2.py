#!/usr/bin/python3

crabs = [int(x) for x in open("input").read().split(",")]

fuel_sums = []
for target in range(max(crabs)):
    fuel_sum = 0
    for crab in crabs:
        n = abs(crab - target)
        fuel_sum += int(n * (n + 1) / 2)

    if target not in fuel_sums:
        fuel_sums.append({"target": target, "sum": fuel_sum})

min_fuel = None
for fuel_sum in fuel_sums:
    if not min_fuel or fuel_sum["sum"] < min_fuel["sum"]:
        min_fuel = fuel_sum

print(min_fuel)
