# https://adventofcode.com/2025/day/4

import numpy as np
from scipy.ndimage import uniform_filter

sum = 0
allRollsList = []

with open("input.txt", "r") as fin:
    for i, line in enumerate(fin.readlines()):
        line = line.replace("\n", "")
        lineRollsStr = line.replace(".", "0").replace("@", "1")
        lineRollsList = [int(i) for i in lineRollsStr]
        allRollsList.append(lineRollsList)
        print(f"Row: {i + 1}, Rolls: {lineRollsStr}")

allRolls = np.array(allRollsList, dtype=float)
adjacentRollsAverage = uniform_filter(allRolls, 3, mode="constant") * allRolls
numAccessibleRolls = np.sum((adjacentRollsAverage > 0) & (adjacentRollsAverage < 0.5))
print(f"Accessible rolls: {numAccessibleRolls}")

# Passed with conceptual (not code) help from Claude - 1551
