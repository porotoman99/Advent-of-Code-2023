import os
from math import floor

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2023_day_4_input.txt"
# inputFilePath = filePath + "\\part1.txt"

cardValues = []

with open(inputFilePath) as inputFile:
	for line in inputFile:
		colonIndex = line.find(":")
		cardIndex = int(line[5:colonIndex])-1
		card = line[colonIndex+2:-1]
		splitCard = card.split(" | ")
		winningNumbers = splitCard[0].split()
		cardNumbers = splitCard[1].split()
		matchingNumbers = [number for number in cardNumbers if number in winningNumbers]
		matchingCount = len(matchingNumbers)
		cardValues.append(matchingCount)

cardTotal = len(cardValues)
cardCounts = [1] * cardTotal

for cardIndex in range(cardTotal):
	cardValue = cardValues[cardIndex]
	cardCount = cardCounts[cardIndex]
	for i in range(cardValue):
		countIndex = i + cardIndex + 1
		if(countIndex < cardTotal):
			cardCounts[countIndex] += cardCount

print(sum(cardCounts))