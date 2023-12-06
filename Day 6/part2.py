import os
from math import floor

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2023_day_6_input.txt"
# inputFilePath = filePath + "\\part1.txt"

times = []
distances = []

with open(inputFilePath) as inputFile:
	for line in inputFile:
		colonSplit = line.split(":")
		if(colonSplit[0] == "Time"):
			times = colonSplit[1].split()
		else:
			distances = colonSplit[1].split()

bigTime = ""
for time in times:
	bigTime += time
bigTime = int(bigTime)

bigDistance = ""
for distance in distances:
	bigDistance += distance
bigDistance = int(bigDistance)

def distanceTraveled(raceTime, buttonTime):
	moveTime = raceTime - buttonTime
	return moveTime * buttonTime


winCount = 0
for buttonTime in range(bigTime):
	distance = distanceTraveled(bigTime, buttonTime)
	if(distance > bigDistance):
		winCount += 1

print(winCount)