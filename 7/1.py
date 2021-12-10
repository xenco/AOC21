#!/usr/bin/python3

crabs = [int(x) for x in open("input").read().split(",")]

fuel_sums = []
for target in crabs:
	fuel_sum = 0
	for crab in crabs:
		fuel_sum += abs(crab - target)
	fuel_sums.append({"target": target, "sum": fuel_sum})

min_fuel = None
for fuel_sum in fuel_sums:
	if not min_fuel or fuel_sum["sum"] < min_fuel["sum"]:
		min_fuel = fuel_sum

print(min_fuel)