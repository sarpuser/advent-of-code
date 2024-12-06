# Advent of Code: https://adventofcode.com/2024/day/6

import numpy as np
from itertools import cycle

directions = cycle(['right', 'down', 'left', 'up'])
visitedPlaces = []
guardPos = [0, 0]
guardFacing = 'up'
guardIncrement = {
	'up': (-1,0),
	'down': (1, 0),
	'right': (0, 1),
	'left': (0, -1)
}

with open('input.txt', 'r') as fin:
	labMap = fin.readlines()

mapWidth = len(labMap[0][:-1]) - 1
mapLength = len(labMap) - 1

for lineNum, line in enumerate(labMap):
	line.replace('\n', '')
	guardPosInLine = line.find('^')
	if guardPosInLine != -1:
		guardPos = [lineNum, guardPosInLine]
		visitedPlaces.append(guardPos)

while True:
	nextGuardPos = np.add(guardPos, guardIncrement[guardFacing]).tolist()

	if nextGuardPos[0] < 0 or nextGuardPos[0] > mapLength or nextGuardPos[1] < 0 or nextGuardPos[1] > mapWidth:
		break

	if labMap[nextGuardPos[0]][nextGuardPos[1]] == '#':
		guardFacing = next(directions)
		print(f'Guard turned {guardFacing} at {guardPos}')
	else:
		guardPos = nextGuardPos
		if guardPos not in visitedPlaces:
			visitedPlaces.append(guardPos)
		print(f'Guard moved to {guardPos}, {len(visitedPlaces) = }')

print(f'Final {len(visitedPlaces) = }')

# Passed! - 4647