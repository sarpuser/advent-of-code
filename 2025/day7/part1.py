# https://adventofcode.com/2025/day/7

incomingBeamIndices = set()
outgoingBeamIndices = set()
numSplit = 0

with open("input.txt", "r") as fin:
    startPosition = fin.readline().index("S")
    incomingBeamIndices.add(startPosition)
    for line in fin.readlines():
        line = line.strip("\n")
        for i in incomingBeamIndices:
            if line[i] == ".":
                outgoingBeamIndices.add(i)
            else:
                outgoingBeamIndices.add(i - 1)
                outgoingBeamIndices.add(i + 1)
                numSplit += 1

        print(
            f"incoming: {incomingBeamIndices}, outgoing: {outgoingBeamIndices}, len: {len(outgoingBeamIndices)}, numSplit: {numSplit}"
        )
        incomingBeamIndices = outgoingBeamIndices.copy()
        outgoingBeamIndices.clear()

# Passed! - 1602
