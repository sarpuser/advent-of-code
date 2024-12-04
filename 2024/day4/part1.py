# Advent of Code: https://adventofcode.com/2024/day/4

import re
from math import dist, sqrt, isclose

def getCharCoordinatesInLine (char: str, lineNum: int) -> list[tuple]:
	charIndicesInLine = [char.start() for char in re.finditer(f'({char})', line)]
	return zip([lineNum] * len(charIndicesInLine), charIndicesInLine)

def countXMAS () -> int:
	xCoordinates = characterCoordinates['X']
	sCoordinates = characterCoordinates['S']
	numXMAS = 0

	for xCoordinate in xCoordinates:
		distances = list(map(dist, [xCoordinate] * len(sCoordinates), sCoordinates))

		# If the distance between X and S is not 3 or 3sqrt(2) (diagonal), S is not in XMAS
		# math.isclose() used bc floating point inaccuracies make the dist not equal to sqrt
		validSCoordinateIndices = [i for i in range(len(distances)) if isclose(distances[i], 3 * sqrt(2)) or distances[i] == 3]

		# Check if the line from X to S includes M and A in order
		for sCoordIndex in sorted(validSCoordinateIndices, reverse=True):
			lineNumDiff = sCoordinates[sCoordIndex][0] - xCoordinate[0]
			colDiff = sCoordinates[sCoordIndex][1] - xCoordinate[1]
			lineNumIncrement = 0 if lineNumDiff == 0 else lineNumDiff // abs(lineNumDiff)
			colIncrement = 0 if colDiff == 0 else colDiff // abs(colDiff)
			nextMInLineCoords = (xCoordinate[0] + lineNumIncrement, xCoordinate[1] + colIncrement)
			nextAInLineCoords = (xCoordinate[0] + 2 * lineNumIncrement, xCoordinate[1] + 2 * colIncrement)

			if (nextMInLineCoords not in characterCoordinates['M'] or nextAInLineCoords not in characterCoordinates['A']):
				validSCoordinateIndices.remove(sCoordIndex)

		numXMAS += len(validSCoordinateIndices)

	return numXMAS

with open('input.txt', 'r') as fin:
	lines = fin.readlines()

sum = 0
characterCoordinates = {
	'X': [],
	'M': [],
	'A': [],
	'S': []
}
numXMAS = 0

for lineNum, line in enumerate(lines):
	characterCoordinates['X'].extend(getCharCoordinatesInLine('X', lineNum))
	characterCoordinates['M'].extend(getCharCoordinatesInLine('M', lineNum))
	characterCoordinates['A'].extend(getCharCoordinatesInLine('A', lineNum))
	characterCoordinates['S'].extend(getCharCoordinatesInLine('S', lineNum))

numXMAS = countXMAS()
print(f'{numXMAS = }')

# Passed! - 2573