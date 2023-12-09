import os

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2023_day_8_input.txt"
# inputFilePath = filePath + "\\part2.txt"

directions = ""
nodes = {}
currentNodes = []

with open(inputFilePath) as inputFile:
	for line in inputFile:
		if(directions == ""):
			directions = line.strip()
		elif(line != "\n"):
			splitLine = line.split(" = ")
			node = splitLine[0]
			if(node[-1] == "A"):
				currentNodes.append(node)
			strippedLinks = splitLine[1].lstrip("(").rstrip(")\n")
			splitLinks = strippedLinks.split(", ")
			leftLink = splitLinks[0]
			rightLink = splitLinks[1]
			links = (leftLink, rightLink)
			nodes[node] = links

stepCount = 0
allFinished = False
nextNodes = currentNodes.copy()

while(not allFinished):
	directionIndex = stepCount % len(directions)
	direction = directions[directionIndex]
	for nodeIndex in range(len(currentNodes)):
		currentNode = currentNodes[nodeIndex]
		if(direction == "L"):
			nextNodes[nodeIndex] = nodes[currentNode][0]
		elif(direction == "R"):
			nextNodes[nodeIndex] = nodes[currentNode][1]
	nextNodes = list(set(nextNodes))
	currentNodes = nextNodes.copy()
	stepCount += 1
	zCount = 0
	for node in currentNodes:
		if(node[-1] == "Z"):
			zCount += 1
	allFinished = zCount == len(currentNodes)

print(stepCount)