import os

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2023_day_6_input.txt"
# inputFilePath = filePath + "\\part1.txt"

times = []
distances = []
finalScore = 1

with open(inputFilePath) as inputFile:
	for line in inputFile:
		colonSplit = line.split(":")
		if(colonSplit[0] == "Time"):
			times = colonSplit[1].split()
		else:
			distances = colonSplit[1].split()

times = [int(time) for time in times]
distances = [int(distance) for distance in distances]

def distanceTraveled(raceTime, buttonTime):
	moveTime = raceTime - buttonTime
	return moveTime * buttonTime

for raceIndex in range(len(times)):
	raceTime = times[raceIndex]
	raceRecord = distances[raceIndex]
	winCount = 0
	for buttonTime in range(raceTime):
		distance = distanceTraveled(raceTime, buttonTime)
		if(distance > raceRecord):
			winCount += 1
	finalScore *= winCount

print(finalScore)