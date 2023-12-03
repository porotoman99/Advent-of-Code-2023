import os

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2023_day_1_input.txt"

intList = []

with open(inputFilePath) as inputFile:
	for line in inputFile:
		lineNumber = []
		for char in line:
			if(char.isdigit()):
				lineNumber.append(char)
		intList.append(int(lineNumber[0]+lineNumber[-1]))

print(sum(intList))