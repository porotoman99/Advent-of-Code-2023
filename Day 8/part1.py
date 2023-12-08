import os

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2023_day_8_input.txt"
# inputFilePath = filePath + "\\part1.txt"

directions = ""
nodes = {}

with open(inputFilePath) as inputFile:
	for line in inputFile:
		if(directions == ""):
			directions = line.strip()
		elif(line != "\n"):
			splitLine = line.split(" = ")
			node = splitLine[0]
			strippedLinks = splitLine[1].lstrip("(").rstrip(")\n")
			splitLinks = strippedLinks.split(", ")
			leftLink = splitLinks[0]
			rightLink = splitLinks[1]
			links = (leftLink, rightLink)
			nodes[node] = links

stepCount = 0
currentNode = "AAA"
while(currentNode != "ZZZ"):
	directionIndex = stepCount % len(directions)
	if(directions[directionIndex] == "L"):
		currentNode = nodes[currentNode][0]
	elif(directions[directionIndex] == "R"):
		currentNode = nodes[currentNode][1]
	stepCount += 1

print(stepCount)