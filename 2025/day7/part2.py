# https://adventofcode.com/2025/day/7

numPathsFromPosition = {}
checkedPositions = set()
manifoldGrid = []


def countPaths(startPosition: tuple[int]) -> int:
    global checkedPositions
    global numPathsFromPosition
    global manifoldGrid

    if startPosition[0] == len(manifoldGrid):
        return 1

    childRow = startPosition[0] + 1

    if manifoldGrid[startPosition[0]][startPosition[1]] == "^":
        checkedPositions.add(startPosition)
        leftChild = (childRow, startPosition[1] - 1)
        rightChild = (childRow, startPosition[1] + 1)
        children = [leftChild, rightChild]
    else:
        children = [(childRow, startPosition[1])]

    print(f"Checking: {startPosition}, children: {children}")

    numPaths = 0
    for child in children:
        if child not in checkedPositions:
            numPaths += countPaths(child)
        else:
            numPaths += numPathsFromPosition[child]

    numPathsFromPosition[startPosition] = numPaths

    return numPaths


with open("input.txt", "r") as fin:
    for line in fin.readlines():
        line = line.strip("\n")
        manifoldGrid.append(list(line))

startingPoint = (0, manifoldGrid[0].index("S"))
numPaths = countPaths(startingPoint)
print(f"num paths: {numPaths}")

# Passed! - 135656430050438
