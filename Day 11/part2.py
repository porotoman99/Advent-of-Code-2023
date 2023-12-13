import os

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2023_day_11_input.txt"
# inputFilePath = filePath + "\\part1.txt"

EXPANSION_FACTOR = 1000000

expansionRows = []

expansionCols = []

universe = []

with open(inputFilePath) as inputFile:
	for line in inputFile:
		universe.append(line[:-1])

for rowIndex in range(len(universe)):
	row = universe[rowIndex]
	if(row.count(".") == len(row)):
		expansionRows.append(rowIndex)

for colIndex in range(len(universe[0])):
	universeHeight = len(universe)
	emptyCount = 0
	for line in universe:
		if(line[colIndex] == "."):
			emptyCount += 1
	if(emptyCount == universeHeight):
		expansionCols.append(colIndex)

coords = []

for row in range(len(universe)):
	for col in range(len(universe[0])):
		if(universe[row][col] == "#"):
			pastRows = [val for val in expansionRows if val <= row]
			rowOffset = len(pastRows) * (EXPANSION_FACTOR-1)
			pastCols = [val for val in expansionCols if val <= col]
			colOffset = len(pastCols) * (EXPANSION_FACTOR-1)
			coords.append((row+rowOffset,col+colOffset))

distances = []

for coordIndex in range(len(coords)):
	coord = coords[coordIndex]
	if(coordIndex < len(coords)):
		for coord2 in coords[coordIndex+1:]:
			distance = abs(coord[0]-coord2[0]) + abs(coord[1]-coord2[1])
			distances.append(distance)

print(sum(distances))