# Advent of Code: https://adventofcode.com/2023/day/3

import re
from numpy import prod

asteriskIndeces = {}

sum = 0

with open("input.txt", "r") as fin:
	lines = fin.readlines()

for lineNum, line in enumerate(lines):
	asteriskIndeces[lineNum] = [match.start() for match in re.finditer("(\*)", line)]

	for asteriskNumInLine, currentAsteriskIndex in enumerate(asteriskIndeces[lineNum]):
		adjacentNumbers = []
		checkIndices = [0, len(line)]

		if len(asteriskIndeces[lineNum]) > 1:
			if asteriskNumInLine == 0:
				# If first asterisk in line, search from 0 to second asterisk
				checkIndices = [0, asteriskIndeces[lineNum][1]]
			elif asteriskNumInLine > 0 and asteriskNumInLine < len(asteriskIndeces[lineNum]) - 1:
				# If not first of last asterisk in line, search from prev to next
				checkIndices = [asteriskIndeces[lineNum][asteriskNumInLine - 1] + 1, asteriskIndeces[lineNum][asteriskNumInLine + 1]]
			elif asteriskNumInLine == len(asteriskIndeces[lineNum]) - 1:
				# If last asterisk in line, search from prev to the end of the line
				checkIndices = [asteriskIndeces[lineNum][asteriskNumInLine - 1] + 1, len(line)]


		# Search if there is a number immediately before the current asterisk
		number = re.search("(\d+)(?=\*)", line[checkIndices[0]:checkIndices[-1]])
		if number:
			adjacentNumbers.append(int(number.group(0)))

		# Search if there is a number immediately after the current asterisk
		number = re.search("(?<=\*)(\d+)", line[checkIndices[0]:checkIndices[-1]])
		if number:
			adjacentNumbers.append(int(number.group(0)))

		# Find all the numbers in the line above current.
		# Then check if the indeces of those numbers (+/- 1 for corners)
		# matches with the current asterisk index. If yes, we have a match.
		if lineNum > 0:
			numbersInLine = re.finditer("(\d+)", lines[lineNum - 1])
			for number in numbersInLine:
				numberRange = range(number.start() - 1, number.end() + 1)
				if currentAsteriskIndex in numberRange:
					adjacentNumbers.append(int(number.group(0)))

		# Same as above but for the line below
		if lineNum < len(lines) - 1:
			numbersInLine = re.finditer("(\d+)", lines[lineNum + 1])
			for number in numbersInLine:
				numberRange = range(number.start() - 1, number.end() + 1)
				if currentAsteriskIndex in numberRange:
					adjacentNumbers.append(int(number.group(0)))

		# Final calculation and sum
		if len(adjacentNumbers) == 2:
			product = prod(adjacentNumbers)
			sum += product
			print(lineNum + 1, adjacentNumbers, product, sum)

# Passed! - 73201705