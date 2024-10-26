# Advent of Code: https://adventofcode.com/2023/day/3

import re
from copy import copy

numberLocations = {}

sum = 0

with open("input.txt", "r") as fin:
	lines = fin.readlines()

for lineNum, line in enumerate(lines):
	numberLocations[lineNum] = [list(range(match.start(), match.end())) for match in re.finditer("(\d+)", line)]

	for numberDigitIndices in numberLocations[lineNum]:
		adjacent = False
		checkIndices = copy(numberDigitIndices)

		if numberDigitIndices[0] > 0:
			checkIndices.insert(0, numberDigitIndices[0] - 1)

		if numberDigitIndices[-1] < len(line) - 2:
			checkIndices.append(numberDigitIndices[-1] + 1)

		if re.search("([^\w\s\.])", line[checkIndices[0]:checkIndices[-1] + 1]):
			# Check both sides
			adjacent = True
		elif lineNum > 0 and re.search("([^\w\s\.])", lines[lineNum - 1][checkIndices[0]:checkIndices[-1] + 1]):
			# Check above, including both corners
			adjacent = True
		elif lineNum < len(lines) - 1 and re.search("([^\w\s\.])", lines[lineNum + 1][checkIndices[0]:checkIndices[-1] + 1]):
			# Check below, including both corners
			adjacent = True

		if adjacent:
			number = int(line[numberDigitIndices[0]:numberDigitIndices[-1] + 1])
			sum += number
			print(lineNum + 1, number, sum)

# Passed! - 527446