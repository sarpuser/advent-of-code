import re
from math import ceil
from numpy import roots

with open('input.txt', 'r') as fin:
	raceTime = int(re.search(' +(.+)', fin.readline())[0].replace(' ', ''))
	raceRecord = int(re.search(' +(.+)', fin.readline())[0].replace(' ', ''))

winningDistance = raceRecord + 1
print('Race 1: ' + str(raceTime) + 'ms, ' + str(raceRecord) + 'mm')

# find solutions to Tx - x^2 - winningDistance, T = time
winningButtonPressDurationBounds = (roots([-1, raceTime, -winningDistance]))

# If lower root is an integer the difference is non inclusive
if winningButtonPressDurationBounds[1].is_integer():
	winningButtonPressDurationBounds[0] += 1

# The integer of the difference between the bounds gives us the number of winning methods
numWinningMethods = int(ceil(winningButtonPressDurationBounds[0]) - winningButtonPressDurationBounds[1])
print('Winning methods:', numWinningMethods)

# Passed! - 33875953