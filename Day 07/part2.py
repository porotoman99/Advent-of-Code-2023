import os

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2023_day_7_input.txt"
# inputFilePath = filePath + "\\part1.txt"

def typeSort(hand):
	cardCount = {
		"J": 0,
		"2": 0,
		"3": 0,
		"4": 0,
		"5": 0,
		"6": 0,
		"7": 0,
		"8": 0,
		"9": 0,
		"T": 0,
		"Q": 0,
		"K": 0,
		"A": 0
	}
	for card in hand:
		cardCount[card] += 1
	jokerCount = cardCount["J"]
	cardCount["J"] = 0
	cardTotals = list(cardCount.values())
	cardTotals.sort(reverse=True)
	if(cardTotals[0] + jokerCount == 5):
		return 6
	elif(cardTotals[0] + jokerCount == 4):
		return 5
	elif(
		cardTotals[0] + jokerCount == 3 and cardTotals[1] == 2
		or cardTotals[0] == 3 and cardTotals[1] + jokerCount == 2
	):
		return 4
	elif(cardTotals[0] + jokerCount == 3):
		return 3
	elif(
		cardTotals[0] + jokerCount == 2 and cardTotals[1] == 2
		or cardTotals[0] == 2 and cardTotals[1] + jokerCount == 2
	):
		return 2
	elif(cardTotals[0] + jokerCount == 2):
		return 1
	else:
		return 0

def bucketSort(camelCard):
	totalScore = 0
	cardOrder = ["J","2","3","4","5","6","7","8","9","T","Q","K","A"]
	hand = camelCard[0]
	totalScore += cardOrder.index(hand[4]) * 15 ** 1
	totalScore += cardOrder.index(hand[3]) * 15 ** 2
	totalScore += cardOrder.index(hand[2]) * 15 ** 3
	totalScore += cardOrder.index(hand[1]) * 15 ** 4
	totalScore += cardOrder.index(hand[0]) * 15 ** 5
	return totalScore

hands = []
bids = []

with open(inputFilePath) as inputFile:
	for line in inputFile:
		lineSplit = line.split()
		hand = lineSplit[0]
		bid = lineSplit[1]
		hands.append(hand)
		bids.append(bid)

bids = [int(bid) for bid in bids]

camelCards = list(zip(hands,bids))

typeBuckets = [[],[],[],[],[],[],[]]

for camelCard in camelCards:
	hand = camelCard[0]
	typeScore = typeSort(hand)
	typeBuckets[typeScore].append(camelCard)

finalCardSort = []

for bucket in typeBuckets:
	if(len(bucket) > 1):
		bucket.sort(key=bucketSort)
	for camelCard in bucket:
		finalCardSort.append(camelCard)

camelScores = []

for camelIndex in range(len(finalCardSort)):
	scoreMultiplier = camelIndex + 1
	camelCard = finalCardSort[camelIndex]
	camelScores.append(camelCard[1] * scoreMultiplier)

print(sum(camelScores))