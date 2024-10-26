# Advent of Code: https://adventofcode.com/2023/day/5

import re

def findMapped (inNum: int, sourceRanges: list[range], destRanges: list[range]) -> int:
	outNum = inNum

	for sourceRangeNum, sourceRange in enumerate(sourceRanges):
		if inNum in sourceRange:
			numIndexInRange = sourceRange.index(inNum)
			outNum = destRanges[sourceRangeNum][numIndexInRange]

	return outNum

def addRangesToDict (map: list):
	mapName = re.match("([\w-]+)", map[0])[0]
	sourceKey = mapName + "-source"
	destKey = mapName + "-dest"
	ranges[sourceKey] = []
	ranges[destKey] = []
	map.remove('') if '' in map else map
	for mapRange in map[1:]:
		rangeNums = mapRange.split(" ")
		dest = int(rangeNums[0])
		source = int(rangeNums[1])
		rangeSize = int(rangeNums[2])
		ranges[sourceKey].append(range(source, source + rangeSize))
		ranges[destKey].append(range(dest, dest + rangeSize))

with open("input.txt", "r") as fin:
	almanac = fin.read()
	seeds = [int(match) for match in re.search("(?<=seeds: )(.+)", almanac)[0].split(" ")]

maps = [map.split("\n") for map in re.findall("(?<=\n{2})((?:.+\n?)+)", almanac)]

ranges = {}
for map in maps:
	addRangesToDict(map)

locations = set()
for seed in seeds:
	soil = findMapped(seed, ranges['seed-to-soil-source'], ranges['seed-to-soil-dest'])
	fertilizer = findMapped(soil, ranges['soil-to-fertilizer-source'], ranges['soil-to-fertilizer-dest'])
	water = findMapped(fertilizer, ranges['fertilizer-to-water-source'], ranges['fertilizer-to-water-dest'])
	light = findMapped(water, ranges['water-to-light-source'], ranges['water-to-light-dest'])
	temperature = findMapped(light, ranges['light-to-temperature-source'], ranges['light-to-temperature-dest'])
	humidity = findMapped(temperature, ranges['temperature-to-humidity-source'], ranges['temperature-to-humidity-dest'])
	location = findMapped(humidity, ranges['humidity-to-location-source'], ranges['humidity-to-location-dest'])

	locations.add(location)
	print(seed, soil, fertilizer, water, light, temperature, humidity, location)

print("min location:", min(locations))

# Passed! - 650599855