from pprint import pprint

numZero = 0
position = 50

with open("input.txt", "r") as fin:
    for line in fin.readlines():
        zeroesCrossed = 0
        absolutePosition = None
        startPosition = position
        direction = line[0]
        amountStr = line[1:]
        amount = int(amountStr.replace("\n", ""))

        if direction == "R":
            absolutePosition = startPosition + amount
            zeroesCrossed = absolutePosition // 100
            zeroesCrossed -= 1 if absolutePosition % 100 == 0 else 0
            position = absolutePosition % 100
        else:
            absolutePosition = startPosition - amount
            zeroesCrossed = (absolutePosition // 100) * -1
            zeroesCrossed -= 1 if startPosition == 0 else 0
            position = (absolutePosition + 100) % 100

        numZero += zeroesCrossed

        if position == 0:
            numZero += 1

        lineData = [
            startPosition,
            direction + str(amount),
            position,
            zeroesCrossed,
            numZero,
        ]
        pprint(lineData)

print(f"Number of zeroes: {numZero}")

# Passed! - 6166
