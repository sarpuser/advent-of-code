# Advent of Code: https://adventofcode.com/2023/day/4

import re
from pprint import pprint

with open("input.txt", "r") as fin:
	lines = fin.readlines()

numCardInstances = [1] * len(lines)

for lineNum, line in enumerate(lines):
	cardNumber = re.search("(\d+)(?=:)", line)[0]
	winningNumbers = re.findall("(\d+)(?!.*:)(?=.+\|)", line)
	drawnNumbers = re.findall("(\d+)(?!.+\|)", line)
	commonNumbers = set(winningNumbers).intersection(drawnNumbers)
	numWinningNumbers = len(commonNumbers)

	for _ in range(numCardInstances[lineNum]):
		for i in range(numWinningNumbers):
			numCardInstances[lineNum + i + 1] += 1

	print(cardNumber, numCardInstances[lineNum], sum(numCardInstances[:lineNum + 1]))

# Passed! - 7258152