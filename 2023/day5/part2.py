# Advent of Code: https://adventofcode.com/2023/day/5

import re

locations = set()
ranges = {}
seedRanges = []

def findSourceNum (destNum: int, destinationRangeStarts: list[int], sourceRangeStarts: list[int], rangeLengths: list[int]) -> int:
	sourceNum = destNum
	for rangeIndex, destRangeStart in enumerate(destinationRangeStarts):
		rangeLength = rangeLengths[rangeIndex]
		sourceRangeStart = sourceRangeStarts[rangeIndex]
		destinationRange = range(destRangeStart, destRangeStart + rangeLength)
		sourceRange = range(sourceRangeStart, sourceRangeStart + rangeLength)
		if destNum in destinationRange:
			numIndexInRange = destinationRange.index(destNum)
			sourceNum = sourceRange[numIndexInRange]
			break

	return sourceNum

def addSortedRangeInfoToDict (map: list):
	mapName = re.match("([\w-]+)", map[0])[0]
	sourceKey = mapName + "-source-starts"
	destKey = mapName + "-destination-starts"
	lengthKey = mapName + "-range-lengths"
	sourceStarts = []
	destStarts = []
	rangeLengths = []
	map.remove('') if '' in map else map
	for mapRange in map[1:]:
		rangeNums = mapRange.split(" ")
		destStarts.append(int(rangeNums[0]))
		sourceStarts.append(int(rangeNums[1]))
		rangeLengths.append(int(rangeNums[2]))

	# Sort the source start, destination start, and length start lists according to the destination starts
	ranges[sourceKey] = [source for _, source in sorted(zip(destStarts, sourceStarts))]
	ranges[lengthKey] = [source for _, source in sorted(zip(destStarts, rangeLengths))]
	ranges[destKey] = sorted(destStarts)

def isLocationValid (location:int) -> tuple[bool, int]:
	# Location is valid if it started from a given seed range
	locationValid = False
	humidity = findSourceNum(location, ranges['humidity-to-location-destination-starts'], ranges['humidity-to-location-source-starts'], ranges['humidity-to-location-range-lengths'])
	temperature = findSourceNum(humidity, ranges['temperature-to-humidity-destination-starts'], ranges['temperature-to-humidity-source-starts'], ranges['temperature-to-humidity-range-lengths'])
	light = findSourceNum(temperature, ranges['light-to-temperature-destination-starts'], ranges['light-to-temperature-source-starts'], ranges['light-to-temperature-range-lengths'])
	water = findSourceNum(light, ranges['water-to-light-destination-starts'], ranges['water-to-light-source-starts'], ranges['water-to-light-range-lengths'])
	fertilizer = findSourceNum(water, ranges['fertilizer-to-water-destination-starts'], ranges['fertilizer-to-water-source-starts'], ranges['fertilizer-to-water-range-lengths'])
	soil = findSourceNum(fertilizer, ranges['soil-to-fertilizer-destination-starts'], ranges['soil-to-fertilizer-source-starts'], ranges['soil-to-fertilizer-range-lengths'])
	seed = findSourceNum(soil, ranges['seed-to-soil-destination-starts'], ranges['seed-to-soil-source-starts'], ranges['seed-to-soil-range-lengths'])

	for seedRange in seedRanges:
		if seed in seedRange:
			locationValid = True
			break

	return locationValid, seed

def main():
	with open("input.txt", "r") as fin:
		almanac = fin.read()

	seedRangeInfo = [int(match) for match in re.search("(?<=seeds: )(.+)", almanac)[0].split(" ")]
	for i, value in enumerate(seedRangeInfo):
		if i % 2 == 0:
			seedRangeStart = value
		else:
			seedRanges.append(range(seedRangeStart, seedRangeStart + value))

	maps = [map.split("\n") for map in re.findall("(?<=\n{2})((?:.+\n?)+)", almanac)]
	for map in maps:
		addSortedRangeInfoToDict(map)

	# The only way that a location is smaller than the minimum mapped range is if its unmapped
	# We loop through all the numbers up to the source start of the minimum range
	# If the current location is already in another range, we skip the entire range
	# Since we are looping to the beginning of the min range, any other ranges will have bigger locations
	# For each location, we check to see if it is a valid starting seed
	location = 0
	while location < ranges['humidity-to-location-source-starts'][0]:
		print(f"{location:,}")
		if location in ranges['humidity-to-location-source-starts']:
			locationRangeIndex = ranges['humidity-to-location-source-starts'].index(location)
			locationRangeLength = ranges['humidity-to-location-range-lengths'][locationRangeIndex]
			location += locationRangeLength
			continue

		locationValid, seed = isLocationValid(location)
		if locationValid:
			print(f"Min unmapped seed: {seed:,}")
			print(f"Min unmapped location: {location:,}")
			locations.add(location)
			break

		location += 1

	# We loop through the range of smallest destination and check if seeds are valid
	location = ranges['humidity-to-location-destination-starts'][0]
	while location < ranges['humidity-to-location-destination-starts'][0] + ranges['humidity-to-location-range-lengths'][0]:
		print(f"{location:,}")

		locationValid, seed = isLocationValid(location)
		if locationValid:
			print(f"Min mapped seed: {seed:,}")
			print(f"Min mapped location: {location:,}")
			locations.add(location)
			break

		location += 1

	print("min location:", min(locations))


if __name__ == "__main__":
	main()

# Passed! - 1240035 (Takes about 35s)