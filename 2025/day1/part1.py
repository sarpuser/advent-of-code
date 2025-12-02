from pprint import pprint

numZero = 0
position = 50

with open("input.txt", "r") as fin:
    for line in fin.readlines():
        lineData = []
        direction = line[0]
        amount = int(line[1:-1])
        lineData = [position, direction + str(amount)]

        if direction == "R":
            position += amount
            position %= 100
        else:
            position -= amount + 100
            position %= 100

        lineData.append(position)

        if position == 0:
            numZero += 1

        pprint(lineData)

print(f"Number of zeroes: {numZero}")

# Passed! - 1034
