# Advent of Code: https://adventofcode.com/2024/day/2

from collections import Counter
import numpy as np

def isSafe (levels: list) -> bool:
	if Counter(levels).most_common()[0][1] > 1:
		print('Unsafe - Duplicates\n')
		return False
	elif levels != sorted(levels) and levels != sorted(levels, reverse=True):
		print('Unsafe - Unsorted\n')
		return False
	elif max(np.abs(np.diff(levels))) > 3:
		print('Unsafe - Spread too far\n')
		return False

	return True

numSafe = 0

with open('input.txt', 'r') as fin:
	for lineNum, line in enumerate(fin.readlines()):
		levels = [int(level.replace('\n', '')) for level in line.split(' ')]
		print(f'{lineNum + 1}: {levels = }')
		if not isSafe(levels):
			continue

		print('Safe\n')
		numSafe += 1

	print(f'{numSafe = }')

# Passed! - 559