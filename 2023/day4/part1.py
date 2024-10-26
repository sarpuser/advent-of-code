# Advent of Code: https://adventofcode.com/2023/day/4

import re

sum = 0
with open("input.txt", "r") as fin:
	lines = fin.readlines()

for lineNum, line in enumerate(lines):
	# Why not use str.find and str.split?
	# Because regex is harder but also cleaner
	cardNumber = re.search("(\d+)(?=:)", line)[0]
	winningNumbers = re.findall("(\d+)(?!.*:)(?=.+\|)", line)
	drawnNumbers = re.findall("(\d+)(?!.+\|)", line)
	commonNumbers = set(winningNumbers).intersection(drawnNumbers)
	numWinningNumbers = len(commonNumbers)

	cardPoints = 2 ** (numWinningNumbers - 1) if numWinningNumbers > 0 else 0

	sum += cardPoints
	print(cardNumber, commonNumbers, numWinningNumbers, cardPoints, sum)

# Passed! - 24848