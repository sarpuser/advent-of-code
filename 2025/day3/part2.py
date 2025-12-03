sum = 0

with open("input.txt", "r") as fin:
    banks = fin.readlines()

for bank in banks:
    maxJoltageStr = ""
    joltages = [int(i) for i in bank.replace("\n", "")]
    searchIndex = 0

    for i in range(12):
        if i != 11:
            maxJoltageBattery = max(joltages[searchIndex : -(11 - i)])
        else:
            maxJoltageBattery = max(joltages[searchIndex:])
        maxJoltageStr += str(maxJoltageBattery)
        searchIndex = joltages[searchIndex:].index(maxJoltageBattery) + searchIndex + 1

    maxJoltage = int(maxJoltageStr)
    sum += maxJoltage
    print(f"bank: {bank[:-1]}, maxJoltage: {maxJoltage}, sum: {sum}")

# Passed! - 171297349921310
