import re

map = {}
instructions = str()
reached = False
currentLocation = 'AAA'
stepCount = 0

with open('input.txt', 'r') as fin:
	instructions = fin.readline().replace('L', '0').replace('R', '1').replace('\n', '')
	fin.readline()
	for line in fin.readlines():
		locations = re.findall('(\w{3})', line)
		map[locations[0]] = (locations[1], locations[2])

while not reached:
	for instruction in instructions:
		print(currentLocation, stepCount)

		if currentLocation == 'ZZZ':
			reached = True
			break

		currentLocation = map[currentLocation][int(instruction)]
		stepCount += 1

# Passed! - 17873