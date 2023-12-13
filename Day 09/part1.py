import os

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2023_day_9_input.txt"
# inputFilePath = filePath + "\\part1.txt"

oasisHistories = []

with open(inputFilePath) as inputFile:
	for line in inputFile:
		lineSplit = line.split()
		oasisHistory = [[int(value) for value in lineSplit]]
		oasisHistories.append(oasisHistory)

def getOasisDiff(oasisHistory):
	interpolatedData = []
	for dataIndex in range(len(oasisHistory)-1):
		dataPoint = oasisHistory[dataIndex]
		dataNext = oasisHistory[dataIndex+1]
		interpolatedData.append(dataNext - dataPoint)
	return interpolatedData

def isZeroes(oasisHistory):
	zeroSet = list(set(oasisHistory))
	return len(zeroSet) == 1 and zeroSet[0] == 0

for oasisHistory in oasisHistories:
	while(not isZeroes(oasisHistory[-1])):
		oasisHistory.append(getOasisDiff(oasisHistory[-1]))
	oasisHistory[-1].append(0)
	for oasisIndex in range(len(oasisHistory)-2,-1,-1):
		oasisRow = oasisHistory[oasisIndex]
		oasisRow.append(oasisRow[-1] + oasisHistory[oasisIndex+1][-1])

oasisFutures = []

for oasisHistory in oasisHistories:
	oasisFutures.append(oasisHistory[0][-1])

print(sum(oasisFutures))