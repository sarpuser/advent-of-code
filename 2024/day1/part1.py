import re

leftNums = []
rightNums = []
sum = 0

with open('input.txt', 'r') as fin:
	for line in fin.readlines():
		lineList = re.findall('(\d+)', line)
		leftNums.append(int(lineList[0]))
		rightNums.append(int(lineList[1]))

leftNumsSorted = sorted(leftNums)
rightNumsSorted = sorted(rightNums)

for i, num in enumerate(leftNumsSorted):
	sum += abs(num - rightNumsSorted[i])
	print(f'{sum = }')

# Passed! - 2164381