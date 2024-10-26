# Advent of Code: https://adventofcode.com/2023/day/1

import re

sum = 0

with open("input.txt", "r") as fin:
	for lineNum, line in enumerate(fin.readlines()):
		alldigits = re.findall("[0-9]", line)
		lineSum = int(alldigits[0] + alldigits[-1])
		sum += lineSum
		print(lineNum, alldigits, lineSum, sum)

# Passed! - 54634