import os
from math import floor

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2023_day_5_input.txt"
# inputFilePath = filePath + "\\part1.txt"

seeds = []
nextSeeds = []
numberLine = False

with open(inputFilePath) as inputFile:
	for line in inputFile:
		colonIndex = line.find(":")
		if(line[:colonIndex] == "seeds"):
			seeds = line[colonIndex+2:].split()
			seeds = [int(seed) for seed in seeds]
			nextSeeds = seeds.copy()
		if(line == "\n"):
			numberLine = False
			seeds = nextSeeds.copy()
		if(numberLine):
			numbers = line.split()
			destination = int(numbers[0])
			source = int(numbers[1])
			indexRange = int(numbers[2])
			for seedIndex in range(len(seeds)):
				seed = seeds[seedIndex]
				if(seed >= source and seed < source + indexRange):
					nextSeeds[seedIndex] = destination + (seed - source)
		if(colonIndex != -1):
			numberLine = True

print(min(seeds))