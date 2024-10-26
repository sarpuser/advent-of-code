# Advent of Code: https://adventofcode.com/2023/day/2

import re
from enum import Enum

class NumColorsInBag(Enum):
	RED = 12
	GREEN = 13
	BLUE = 14

def getMaxDrawOfColor (color: str, game: list):
	regex = "\d+(?= " + color + ")"
	allDraws = [int(numColor) for numColor in re.findall(regex, game)]
	largestDraw = max(allDraws)
	return largestDraw

sum = 0

with open("input.txt", "r") as fin:
	for line in fin.readlines():
		gameID = int(re.search("\d+(?=:)", line)[0])
		allDraws = re.findall("((?:\d+ \w+(?:, )*)+)", line)
		maxRedDraw = getMaxDrawOfColor("red", line)
		maxGreenDraw = getMaxDrawOfColor("green", line)
		maxBlueDraw = getMaxDrawOfColor("blue", line)

		if maxRedDraw <= NumColorsInBag.RED.value and maxGreenDraw <= NumColorsInBag.GREEN.value and maxBlueDraw <= NumColorsInBag.BLUE.value:
			sum += gameID
			print(gameID, allDraws, sum)

# Passed! - 2149