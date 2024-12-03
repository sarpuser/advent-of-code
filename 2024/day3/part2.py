# Advent of Code: https://adventofcode.com/2024/day/3

import re

sum = 0
active = True

with open('input.txt', 'r') as fin:
	memory = fin.read()

instructions = re.findall(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', memory)

for instruction in instructions:
	if instruction =='do()':
		print('Activate')
		active = True
	elif instruction == 'don\'t()':
		print('Deactivate')
		active = False
	elif active:
		numbers = re.findall('\d+', instruction)
		sum += int(numbers[0]) * int(numbers[1])
		print(f'{numbers = }, {sum = }')
	else:
		print(f'Skipping {instruction}')

# Passed! - 77055967