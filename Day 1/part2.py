import os

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2023_day_1_input.txt"

DIGITS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

intList = []

with open(inputFilePath) as inputFile:
	for line in inputFile:
		lineNumber = []
		for charIndex in range(len(line)):
			char = line[charIndex]
			if (char.isdigit()):
				lineNumber.append(char)
			else:
				for digitIndex in range(len(DIGITS)):
					digit = DIGITS[digitIndex]
					if(line.find(digit, charIndex) == charIndex):
						lineNumber.append(str(digitIndex+1))
		intList.append(int(lineNumber[0]+lineNumber[-1]))

print(sum(intList))