import re
from math import ceil
from numpy import roots

product = 1

with open('input.txt', 'r') as fin:
	raceTimes = [int(time) for time in re.findall('(\d+)', fin.readline())]
	raceRecords = [int(record) for record in re.findall('(\d+)', fin.readline())]

races = zip(raceTimes, raceRecords)

for raceNum, race in enumerate(races):
	time = race[0]
	record = race[1]
	winningDistance = record + 1
	print('Race ' + str(raceNum + 1) + ': ' + str(time) + 'ms, ' + str(record) + 'mm')

	# find solutions to Tx - x^2 - winningDistance, T = time
	winningButtonPressDurationBounds = (roots([-1, time, -winningDistance]))

	# If lower root is an integer the difference is non inclusive
	if winningButtonPressDurationBounds[0].is_integer():
		winningButtonPressDurationBounds[0] += 1

	# The integer of the difference between the bounds gives us the number of winning methods
	numWinningMethods = int(ceil(winningButtonPressDurationBounds[0]) - winningButtonPressDurationBounds[1])
	product *= numWinningMethods
	print('Winning methods:', numWinningMethods)
	print('Product:', product)

print('Final product:', product)

# Passed! - 281600