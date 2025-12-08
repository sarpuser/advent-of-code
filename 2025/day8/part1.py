# https://adventofcode.com/2025/day/8


from functools import reduce
from operator import mul

import numpy as np

allPoints = []
distances = {}
circuits: list[set] = []

CONNECTION_SIZE = 1000

with open("input.txt", "r") as fin:
    for line in fin.readlines():
        line = line.strip("\n")
        point = [int(i) for i in line.split(",")]
        allPoints.append(point)

for i, firstPoint in enumerate(allPoints):
    for secondPoint in allPoints[i + 1 :]:
        distance = np.linalg.norm(np.array(firstPoint) - np.array(secondPoint))
        key = (tuple(firstPoint), tuple(secondPoint))
        distances[key] = distance

distanceValues = list(distances.values())
pointPairs = list(distances.keys())
smallestDistanceIndices = np.argsort(distanceValues)
for i in smallestDistanceIndices[:CONNECTION_SIZE]:
    points = pointPairs[i]
    firstPoint = points[0]
    secondPoint = points[1]
    firstPointCircuitIndex = None
    secondPointCircuitIndex = None

    for j, circuit in enumerate(circuits):
        if firstPoint in circuit:
            firstPointCircuitIndex = j
        if secondPoint in circuit:
            secondPointCircuitIndex = j

    if firstPointCircuitIndex is not None and secondPointCircuitIndex is not None:
        newCircuit = set.union(
            circuits[firstPointCircuitIndex], circuits[secondPointCircuitIndex]
        )
        print(
            f"Merged circuits - Points: {points}, first circuit: {circuits[firstPointCircuitIndex]}, second circuit: {circuits[secondPointCircuitIndex]}"
        )
        circuits.pop(max(firstPointCircuitIndex, secondPointCircuitIndex))
        circuits.pop(min(firstPointCircuitIndex, secondPointCircuitIndex))
        circuits.append(newCircuit)
    elif firstPointCircuitIndex is not None and secondPointCircuitIndex is None:
        circuits[firstPointCircuitIndex].add(secondPoint)
        print(
            f"Added point 2 to existing - points: {points}, circuit: {circuits[firstPointCircuitIndex]}"
        )
    elif secondPointCircuitIndex is not None and firstPointCircuitIndex is None:
        circuits[secondPointCircuitIndex].add(firstPoint)
        print(
            f"Added point 1 to existing - points: {points}, circuit: {circuits[secondPointCircuitIndex]}"
        )

    else:
        newSet = set([firstPoint, secondPoint])
        circuits.append(newSet)
        print(f"Created new circuit - points: {points}")


circuitSizes = sorted([len(i) for i in circuits], reverse=True)
print(f"Product of the largest 3 circuit sizes: {reduce(mul, circuitSizes[:3])}")

# Passed! - 32103
