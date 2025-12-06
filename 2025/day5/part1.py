# https://adventofcode.com/2025/day/5

import re

numFresh = 0

with open("input.txt", "r") as fin:
    database = fin.read()

rangeBoundries = [
    (int(idRange[0]), int(idRange[1]) + 1)
    for idRange in re.findall(r"(\d+)-(\d+)", database, flags=re.MULTILINE)
]
IDsToCheck = [int(i) for i in re.findall(r"^(\d+)$", database, flags=re.MULTILINE)]

freshIDRanges = []
for idRange in rangeBoundries:
    rangeStart = idRange[0]
    rangeEnd = idRange[1]
    freshIDRanges.append(range(rangeStart, rangeEnd))

for i, id in enumerate(IDsToCheck):
    lastNumFresh = numFresh
    for range in freshIDRanges:
        if id in range:
            numFresh += 1
            print(f"row: {i + 1}, id: {id:,}, numFresh: {numFresh}")
            break

# Passed! - 674
