from collections import Counter

winnings = 0
hands = []
bids = []
handStrengths = []

def getHandType (hand: str) -> str:
	counts = Counter(hand)
	if 5 in counts.values():
		# Five of a kind
		return '6'
	elif 4 in counts.values():
		# Four of a kind
		return '5'
	elif 3 in counts.values() and 2 in counts.values():
		# Full house
		return '4'
	elif 3 in counts.values():
		# Three of a kind
		return '3'
	elif 2 in counts.values() and Counter(counts.values())[2] == 2:
		# Two pair
		return '2'
	elif 2 in counts.values() and Counter(counts.values())[2] == 1:
		# One pair
		return '1'
	else:
		# High card
		return '0'


with open('input.txt', 'r') as fin:
	for line in fin.readlines():
		lineItems = line.split(' ')
		hand = lineItems[0]
		bid = int(lineItems[1].replace('\n', ''))
		hands.append(hand)
		bids.append(bid)

		# Replace all the letters with their rank in hex, A -> 13 (D), K -> 12 (C)...
		handStrength = hand.replace('A', 'E')
		handStrength = handStrength.replace('K', 'D')
		handStrength = handStrength.replace('Q', 'C')
		handStrength = handStrength.replace('J', 'B')
		handStrength = handStrength.replace('T', 'A')

		# Hand type is the most important so we add it to the beginning of handStrength
		handStrength = getHandType(hand) + handStrength

		handStrengths.append(int(handStrength, base=16))

# Sort hands and bids according to the handStrengths
handsSorted = [hand for _, hand in sorted(zip(handStrengths, hands))]
bidsSorted = [bid for _, bid in sorted(zip(handStrengths, bids))]
handStrengthsSorted = sorted(handStrengths)

for bidIndex, bid in enumerate(bidsSorted):
	handWinnings = (bidIndex + 1) * bid
	winnings += handWinnings
	print(handsSorted[bidIndex], bid, handWinnings, winnings)

# Passed! - 250474325