import re
from collections import Counter

leftNums = []
rightNums = []
sum = 0

with open('input.txt', 'r') as fin:
	for line in fin.readlines():
		lineList = re.findall('(\d+)', line)
		leftNums.append(int(lineList[0]))
		rightNums.append(int(lineList[1]))

rightNumsCounter = Counter(rightNums)
for num in leftNums:
	similarity = num * rightNumsCounter[num]
	sum += similarity
	print(f'{num = }, {rightNumsCounter[num] = }, {sum = }')

# Passed! - 20719933