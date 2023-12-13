import os

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2023_day_2_input.txt"
# inputFilePath = filePath + "\\part1.txt"

powerList = []

with open(inputFilePath) as inputFile:
	for line in inputFile:
		colonIndex = line.find(":")
		game = line[colonIndex+2:-1]
		rounds = game.split(";")
		red = 0
		green = 0
		blue = 0
		for round in rounds:
			cubes = round.split(",")
			for cube in cubes:
				cubeAttributes = cube.strip().split()
				cubeCount = int(cubeAttributes[0])
				cubeColor = cubeAttributes[1]
				if(cubeColor == "red"):
					red = max(red, cubeCount)
				elif(cubeColor == "green"):
					green = max(green, cubeCount)
				elif(cubeColor == "blue"):
					blue = max(blue, cubeCount)
		power = red * green * blue
		powerList.append(power)

print(sum(powerList))