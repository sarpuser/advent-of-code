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
        if length % 2 != 0:
            continue

        midpoint = length // 2

        if numStr[:midpoint] == numStr[midpoint:]:
            sum += num
            print(f"Range: {idRange}, num: {num}, sum: {sum}")

# Passed! - 28846518423
