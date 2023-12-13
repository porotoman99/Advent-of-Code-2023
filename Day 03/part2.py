import os

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2023_day_3_input.txt"
# inputFilePath = filePath + "\\part1.txt"

def getNumber(line, index):
	numberStartIndex = index
	while(numberStartIndex-1 >= 0 and line[numberStartIndex-1].isdigit()):
		numberStartIndex -= 1
	numberEndIndex = numberStartIndex
	while(line[numberEndIndex].isdigit()):
		numberEndIndex += 1
	return int(line[numberStartIndex:numberEndIndex])


def getGearRatios(previousLine, currentLine, nextLine):
	charIndex = 0
	returnRatios = []
	while(charIndex < len(currentLine)):
		char = currentLine[charIndex]
		if(char == "*"):
			partNumbers = []
			valid = False
			if(charIndex == 0):
				if(previousLine[charIndex].isdigit() or previousLine[charIndex+1].isdigit()):
					if(previousLine[charIndex].isdigit()):
						partNumbers.append(getNumber(previousLine, charIndex))
					else:
						partNumbers.append(getNumber(previousLine, charIndex+1))
				if(currentLine[charIndex+1].isdigit()):
					partNumbers.append(getNumber(currentLine, charIndex+1))
				if(nextLine[charIndex].isdigit() or nextLine[charIndex+1].isdigit()):
					if(nextLine[charIndex].isdigit()):
						partNumbers.append(getNumber(nextLine, charIndex))
					else:
						partNumbers.append(getNumber(nextLine, charIndex+1))
				if(len(partNumbers) == 2):
					valid = True
			else:
				if(previousLine[charIndex-1].isdigit() and previousLine[charIndex+1].isdigit() and not previousLine[charIndex].isdigit()):
					partNumbers.append(getNumber(previousLine, charIndex-1))
					partNumbers.append(getNumber(previousLine, charIndex+1))
				elif(previousLine[charIndex-1].isdigit() or previousLine[charIndex].isdigit() or previousLine[charIndex+1].isdigit()):
					if(previousLine[charIndex-1].isdigit()):
						partNumbers.append(getNumber(previousLine, charIndex-1))
					elif(previousLine[charIndex].isdigit()):
						partNumbers.append(getNumber(previousLine, charIndex))
					else:
						partNumbers.append(getNumber(previousLine, charIndex+1))
				if(currentLine[charIndex-1].isdigit()):
					partNumbers.append(getNumber(currentLine, charIndex-1))
				if(currentLine[charIndex+1].isdigit()):
					partNumbers.append(getNumber(currentLine, charIndex+1))
				if(nextLine[charIndex-1].isdigit() and nextLine[charIndex+1].isdigit() and not nextLine[charIndex].isdigit()):
					partNumbers.append(getNumber(nextLine, charIndex-1))
					partNumbers.append(getNumber(nextLine, charIndex+1))
				elif(nextLine[charIndex-1].isdigit() or nextLine[charIndex].isdigit() or nextLine[charIndex+1].isdigit()):
					if(nextLine[charIndex-1].isdigit()):
						partNumbers.append(getNumber(nextLine, charIndex-1))
					elif(nextLine[charIndex].isdigit()):
						partNumbers.append(getNumber(nextLine, charIndex))
					else:
						partNumbers.append(getNumber(nextLine, charIndex+1))
				if(len(partNumbers) == 2):
					valid = True
			if(valid):
				returnRatios.append(partNumbers[0]*partNumbers[1])
		charIndex += 1
	return returnRatios

previousLine = ""
currentLine = ""

gearRatios = []

with open(inputFilePath) as inputFile:
	for nextLine in inputFile:
		if(currentLine != ""):
			newGearRatios = getGearRatios(previousLine, currentLine, nextLine)
			for gearRatio in newGearRatios:
				gearRatios.append(int(gearRatio))
		previousLine = currentLine
		currentLine = nextLine
	nextLine = ""
	newGearRatios = getGearRatios(previousLine, currentLine, nextLine)
	for gearRatio in newGearRatios:
		gearRatios.append(int(gearRatio))

print(sum(gearRatios))