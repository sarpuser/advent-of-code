# https://adventofcode.com/2025/day/6

import operator
import re
from functools import reduce

import numpy as np

allLines = []
sum = 0

with open("input.txt", "r") as fin:
    for line in fin.readlines():
        lineList = re.findall(r"([\d\*+]+)", line)
        try:
            lineInts = [int(i) for i in lineList]
            allLines.append(lineInts)
        except ValueError:
            operators = [operator.add if op == "+" else operator.mul for op in lineList]

problems = np.transpose(np.array(allLines))

for i, problem in enumerate(problems):
    result = reduce(operators[i], problem)
    sum += result
    print(f"Column: {i + 1}, Op: {operators[i]}, result: {result}, sum: {sum}")

# Passed! - 4405895212738
