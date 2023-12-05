import os
from math import floor

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2023_day_4_input.txt"
# inputFilePath = filePath + "\\part1.txt"

points = 0

with open(inputFilePath) as inputFile:
	for line in inputFile:
		colonIndex = line.find(":")+1
		card = line[colonIndex:-1]
		splitCard = card.split(" | ")
		winningNumbers = splitCard[0].split()
		cardNumbers = splitCard[1].split()
		matchingNumbers = [number for number in cardNumbers if number in winningNumbers]
		matchingCount = len(matchingNumbers)
		points += floor(2 ** (matchingCount - 1))

print(points)