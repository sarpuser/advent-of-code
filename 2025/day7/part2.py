# https://adventofcode.com/2025/day/7

pathCache = {}
manifoldGrid = []


def countPathsFrom(row, col):
    global checkedPositions
    global manifoldGrid

    if row == len(manifoldGrid):
        return 1

    if (row, col) in pathCache:
        return pathCache[(row, col)]

    childRow = row + 1

    if manifoldGrid[row][col] == "^":
        children = [(childRow, col - 1), (childRow, col + 1)]
    else:
        children = [(childRow, col)]

    print(f"Checking: {(row, col)}, children: {children}")

    numPaths = 0
    for childRow, childCol in children:
        pathCount = countPathsFrom(childRow, childCol)
        numPaths += pathCount

    pathCache[(row, col)] = numPaths

    return numPaths


with open("input.txt", "r") as fin:
    for line in fin.readlines():
        line = line.strip("\n")
        manifoldGrid.append(list(line))

numPaths = countPathsFrom(0, manifoldGrid[0].index("S"))
print(f"num paths: {numPaths}")

# Passed! - 135656430050438
# Cleaned up with Claude after passing
