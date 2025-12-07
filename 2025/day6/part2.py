# https://adventofcode.com/2025/day/6#part2

import operator
import re
from functools import reduce

import numpy as np

allLines = []
allLinesPadded = []
sum = 0
maxLineLen = 0

with open("input.txt", "r") as fin:
    for line in fin.readlines():
        line.replace("\n", "")
        maxLineLen = len(line) if len(line) > maxLineLen else maxLineLen
        lineList = re.findall(r"(.)", line)
        allLines.append(lineList)


for line in allLines:
    lineArr = np.array(line)
    padded = np.pad(
        lineArr, (0, maxLineLen - len(line)), mode="constant", constant_values=" "
    )
    allLinesPadded.append(padded)

print(np.array(allLinesPadded))
problemLines = np.transpose(np.array(allLinesPadded))
print(problemLines)

problemNums = []
for line in problemLines:
    if line[-1] == "+":
        op = operator.add
    elif line[-1] == "*":
        op = operator.mul

    try:
        num = int("".join(line[:-1]))
        problemNums.append(num)
    except ValueError:
        result = reduce(op, problemNums)
        sum += result
        print(
            f"problemNums: {problemNums}, operator: {op}, result: {result}, sum: {sum}"
        )
        problemNums = []

# Passed! - 7450962489289
