# https://adventofcode.com/2025/day/4#part2

import numpy as np
from scipy.ndimage import uniform_filter

sum = 0
allRollsList = []
numAccessibleRolls = None

with open("input.txt", "r") as fin:
    for i, line in enumerate(fin.readlines()):
        line = line.replace("\n", "")
        lineRollsStr = line.replace(".", "0").replace("@", "1")
        lineRollsList = [int(i) for i in lineRollsStr]
        allRollsList.append(lineRollsList)

allRolls = np.array(allRollsList, dtype=float)

while numAccessibleRolls != 0:
    adjacentRollsAverage = uniform_filter(allRolls, 3, mode="constant") * allRolls
    accessibleRolls = (adjacentRollsAverage > 0) & (adjacentRollsAverage < 0.5)
    numAccessibleRolls = np.sum(accessibleRolls)
    allRolls = allRolls * ~accessibleRolls
    sum += numAccessibleRolls
    print(f"Rolls Removed: {numAccessibleRolls}, Sum: {sum}")

# Passed! - 9784
