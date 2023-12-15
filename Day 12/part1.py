import os

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2023_day_12_input.txt"
# inputFilePath = filePath + "\\part1.txt"

lines = []
numbers = []

with open(inputFilePath) as inputFile:
	for line in inputFile:
		splitLine = line[:-1].split()
		lines.append(splitLine[0])
		splitNumbers = splitLine[1].split(",")
		splitNumbers = [int(number) for number in splitNumbers]
		numbers.append(splitNumbers)

puzzleLines = zip(lines, numbers)
correctGuesses = []

for puzzleLine in puzzleLines:
	line = puzzleLine[0]
	numbers = puzzleLine[1]
	unknownSpaces = line.count("?")
	puzzleOptions = 2 ** unknownSpaces
	correctGuess = 0
	for decimalMask in range(puzzleOptions):
		testLine = line
		for power in range(unknownSpaces):
			maskVal = decimalMask & (2 ** power)
			unknownIndex = testLine.find("?")
			if(maskVal > 0):
				newChar = "#"
			else:
				newChar = "."
			testLine = testLine[:unknownIndex] + newChar + testLine[unknownIndex+1:]
		if(numbers == [len(e) for e in testLine.split(".") if e != ""]):
			correctGuess += 1
	correctGuesses.append(correctGuess)

print(sum(correctGuesses))