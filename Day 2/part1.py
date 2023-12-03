import os

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2023_day_2_input.txt"
# inputFilePath = filePath + "\\part1.txt"

RED = 12
GREEN = 13
BLUE = 14

idList = []

with open(inputFilePath) as inputFile:
	for line in inputFile:
		colonIndex = line.find(":")
		gameId = line[5:colonIndex]
		game = line[colonIndex+2:-1]
		rounds = game.split(";")
		valid = True
		for round in rounds:
			cubes = round.split(",")
			for cube in cubes:
				cubeAttributes = cube.strip().split()
				cubeCount = int(cubeAttributes[0])
				cubeColor = cubeAttributes[1]
				if(cubeColor == "red" and cubeCount > RED):
					valid = False
				elif(cubeColor == "green" and cubeCount > GREEN):
					valid = False
				elif(cubeColor == "blue" and cubeCount > BLUE):
					valid = False
		if(valid):
			idList.append(int(gameId))

print(sum(idList))