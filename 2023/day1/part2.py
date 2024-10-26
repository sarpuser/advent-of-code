# Advent of Code: https://adventofcode.com/2023/day/1

import re

digitsSpelled = {
	'one': "1",
	'two': "2",
	'three': "3",
	'four': "4",
	'five': "5",
	'six': "6",
	'seven': "7",
	'eight': "8",
	'nine': "9"
}

sum = 0

with open("input.txt", "r") as fin:
	for lineNum, line in enumerate(fin.readlines()):
		# The input file contains overlapping digits, such as oneight and twone
		# Doing a normal regex would only get the left digit, not the right one
		# Doing positive lookahead do not consume the letters
		# Adding a capture group inside allows it to be matched
		allDigitsMixed = re.findall("(?=([0-9]|zero|one|two|three|four|five|six|seven|eight|nine))", line.lower())
		allDigits = [digitsSpelled[digit] if digit not in "1234567890" else digit for digit in allDigitsMixed]
		lineSum = int(allDigits[0] + allDigits[-1])
		sum += lineSum
		print(lineNum + 1, allDigitsMixed, lineSum, sum)

# Passed! - 53855