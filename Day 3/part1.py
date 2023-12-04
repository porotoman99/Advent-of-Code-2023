import os

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2023_day_3_input.txt"
# inputFilePath = filePath + "\\part1.txt"

def getPartNumbers(previousLine, currentLine, nextLine):
	charIndex = 0
	returnNumbers = []
	while(charIndex < len(currentLine)):
		char = currentLine[charIndex]
		if(char.isdigit()):
			numberStartIndex = charIndex
			charIndex += 1
			while(charIndex < len(currentLine) and currentLine[charIndex].isdigit()):
				charIndex += 1
			numberEndIndex = charIndex
			searchStart = max(0,numberStartIndex-1)
			searchEnd = min(len(currentLine)-1,numberEndIndex+1)
			valid = False
			pLine = ""
			cLine = ""
			nLine = ""
			for i in range(searchStart, searchEnd):
				if(previousLine != ""):
					pLine += previousLine[i]
					if(previousLine[i] != "." and not previousLine[i].isdecimal()):
						valid = True
				cLine += currentLine[i]
				if(currentLine[i] != "." and not currentLine[i].isdecimal()):
					valid = True
				if(nextLine != ""):
					nLine += nextLine[i]
					if(nextLine[i] != "." and not nextLine[i].isdecimal()):
						valid = True
			if(valid):
				# print(pLine)
				# print(cLine)
				# print(nLine)
				# print("#####")
				returnNumbers.append(currentLine[numberStartIndex:numberEndIndex])
		charIndex += 1
	return returnNumbers

previousLine = ""
currentLine = ""

partNumbers = []

with open(inputFilePath) as inputFile:
	for nextLine in inputFile:
		if(currentLine != ""):
			newPartNumbers = getPartNumbers(previousLine, currentLine, nextLine)
			for partNumber in newPartNumbers:
				partNumbers.append(int(partNumber))
		previousLine = currentLine
		currentLine = nextLine
	nextLine = ""
	newPartNumbers = getPartNumbers(previousLine, currentLine, nextLine)
	for partNumber in newPartNumbers:
		partNumbers.append(int(partNumber))

print(partNumbers)
print(sum(partNumbers))