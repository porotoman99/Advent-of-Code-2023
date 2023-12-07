import os

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2023_day_7_input.txt"
# inputFilePath = filePath + "\\part1.txt"

CARD_ORDER = "J23456789TQKA"

def typeSort(camelCard):
	cardCount = {}
	for card in CARD_ORDER:
		cardCount[card] = 0
	hand = camelCard[0]
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

def handSort(camelCard):
	totalScore = 0
	hand = camelCard[0]
	totalScore += CARD_ORDER.index(hand[4]) * 15 ** 1
	totalScore += CARD_ORDER.index(hand[3]) * 15 ** 2
	totalScore += CARD_ORDER.index(hand[2]) * 15 ** 3
	totalScore += CARD_ORDER.index(hand[1]) * 15 ** 4
	totalScore += CARD_ORDER.index(hand[0]) * 15 ** 5
	return totalScore

hands = []
bids = []

with open(inputFilePath) as inputFile:
	for line in inputFile:
		lineSplit = line.split()
		hand = lineSplit[0]
		bid = lineSplit[1]
		hands.append(hand)
		bids.append(int(bid))

camelCards = list(zip(hands,bids))
camelCards = sorted(camelCards, key=lambda x: (typeSort(x), handSort(x)))

camelScores = []

for camelIndex in range(len(camelCards)):
	scoreMultiplier = camelIndex + 1
	camelCard = camelCards[camelIndex]
	camelScores.append(camelCard[1] * scoreMultiplier)

print(sum(camelScores))