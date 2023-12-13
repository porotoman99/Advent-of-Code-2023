import os

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2023_day_11_input.txt"
# inputFilePath = filePath + "\\part1.txt"

tallUniverse = []

with open(inputFilePath) as inputFile:
	for line in inputFile:
		tallUniverse.append(line[:-1])
		if(line.count(".") == len(line[:-1])):
			tallUniverse.append(line[:-1])

expandedUniverse = tallUniverse.copy()
colOffset = 0

for col in range(len(tallUniverse[0])):
	universeHeight = len(tallUniverse)
	emptyCount = 0
	for line in tallUniverse:
		if(line[col] == "."):
			emptyCount += 1
	if(emptyCount == universeHeight):
		colIndex = col + colOffset
		expandedUniverse = [row[:colIndex]+"."+row[colIndex:] for row in expandedUniverse]
		colOffset += 1

coords = []

for row in range(len(expandedUniverse)):
	for col in range(len(expandedUniverse[0])):
		if(expandedUniverse[row][col] == "#"):
			coords.append((row,col))

distances = []

for coordIndex in range(len(coords)):
	coord = coords[coordIndex]
	if(coordIndex < len(coords)):
		for coord2 in coords[coordIndex+1:]:
			distance = abs(coord[0]-coord2[0]) + abs(coord[1]-coord2[1])
			distances.append(distance)

print(sum(distances))