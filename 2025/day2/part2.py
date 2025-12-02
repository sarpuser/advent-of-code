import re

sum = 0

with open("input.txt", "r") as fin:
    allIDs = fin.readline()

ranges = re.findall(r"(\d+-\d+)", allIDs)

for idRange in ranges:
    rangeStart = int(re.search(r"(\d+)-", idRange)[1])
    rangeEnd = int(re.search(r"-(\d+)", idRange)[1])
    for num in range(rangeStart, rangeEnd + 1):
        numStr = str(num)
        length = len(numStr)
        midpoint = length // 2

        for patternLen in range(1, midpoint + 1):
            pattern = numStr[:patternLen]
            patternCount = len(re.findall(f"({pattern})", numStr))

            if patternLen * patternCount == length:
                sum += num
                print(f"range: {idRange}, num: {num}, pattern: {pattern}, sum: {sum}")
                break

# Passed! - 31578210022
