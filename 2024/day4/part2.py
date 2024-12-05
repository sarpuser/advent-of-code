# Advent of Code: https://adventofcode.com/2024/day/4

import re
from math import dist, sqrt, isclose
from pprint import pprint

def getCharCoordinatesInLine (char: str, lineNum: int) -> list[tuple]:
	charIndicesInLine = [char.start() for char in re.finditer(f'({char})', line)]
	return zip([lineNum] * len(charIndicesInLine), charIndicesInLine)

def countX_MAS () -> int:
	aCoordinates = characterCoordinates['A']
	mCoordinates = characterCoordinates['M']
	sCoordinates = characterCoordinates['S']
	numXMAS = 0

	for aCoordinate in aCoordinates:
		# Skip first and last line since A has to be in the middle
		if aCoordinate[0] == 0 or aCoordinate[0] == 139 or aCoordinate[1] == 0 or aCoordinate[1] == 139:
			continue

		aToMDistances = list(map(dist, [aCoordinate] * len(mCoordinates), mCoordinates))
		aToSDistances = list(map(dist, [aCoordinate] * len(sCoordinates), sCoordinates))

		diagonalMCoords = [mCoordinates[i] for i, distance in enumerate(aToMDistances) if isclose(distance, sqrt(2))]
		diagonalSCoords = [sCoordinates[i] for i, distance in enumerate(aToSDistances) if isclose(distance, sqrt(2))]

		if len(diagonalMCoords) != 2 or len(diagonalSCoords) != 2:
			# print(f'Skipped A at {aCoordinate}')
			continue

		# One of the coords of the same letter should be the same because if not then it means
		# that the same letter is on both ends of the diagonal, eg. SAS, MAM
		if diagonalMCoords[0][0] == diagonalMCoords[1][0] or diagonalMCoords[0][1] == diagonalMCoords[0][1]:
			numXMAS += 1
			print(f'Added X-MAS at {aCoordinate}, {numXMAS = }, {diagonalMCoords = }, {diagonalSCoords = }')

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

numXMAS = countX_MAS()
print(f'{numXMAS = }')
