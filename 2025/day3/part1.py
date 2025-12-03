sum = 0

with open("input.txt", "r") as fin:
    banks = fin.readlines()

for bank in banks:
    joltages = [int(i) for i in bank[:-1]]

    maxFirstJoltage = max(joltages[:-1])
    maxFirstJoltageIndex = joltages.index(maxFirstJoltage)
    maxSecondJoltage = max(joltages[maxFirstJoltageIndex + 1 :])

    maxJoltage = int(str(maxFirstJoltage) + str(maxSecondJoltage))

    sum += maxJoltage
    print(f"bank: {bank[:-1]}, maxJoltage: {maxJoltage}, sum: {sum}")

# Passed! - 17193
