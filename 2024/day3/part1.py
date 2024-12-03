# Advent of Code: https://adventofcode.com/2024/day/3

import re

sum = 0

with open('input.txt', 'r') as fin:
	memory = fin.read()

multiplyInstructions = re.findall('(?:mul\((\d+,\d+)\))', memory)

for instruction in multiplyInstructions:
	numbers = instruction.split(',')
	sum += int(numbers[0]) * int(numbers[1])
	print(f'{numbers = }, {sum = }')

# Passed! = 153469856