import os

filePath = os.path.dirname(os.path.realpath(__file__))
inputFilePath = filePath + "\\adventofcode.com_2023_day_10_input.txt"
# inputFilePath = filePath + "\\part1.txt"

loopRows = []

with open(inputFilePath) as inputFile:
	for line in inputFile:
		loopRows.append(line.strip("\n"))

loopArea = len(loopRows) * len(loopRows[0])
loopDistances = []
for _ in loopRows:
	row = [loopArea] * len(loopRows[0])
	loopDistances.append(row.copy())

startPos = (0,0)

for row in range(len(loopRows)):
	for char in range(len(loopRows[0])):
		if(loopRows[row][char] == "S"):
			startPos = (row,char)
			loopDistances[row][char] = 0
			# Start in top-left corner
			if(row == 0 and char == 0):
				loopRows[row] = loopRows[row].replace("S","F")
			# Start in bottom-left corner
			elif(row == len(loopRows)-1 and char == 0):
				loopRows[row] = loopRows[row].replace("S","L")
			# Start in top-right corner
			elif(row == 0 and char == len(loopRows[0])-1):
				loopRows[row] = loopRows[row].replace("S","7")
			# Start in bottom-right corner
			elif(row == len(loopRows)-1 and char == len(loopRows[0])-1):
				loopRows[row] = loopRows[row].replace("S","J")
			# Start on left edge
			elif(char == 0):
				# Can't connect to right
				if(loopRows[row][char+1] not in "7J-"):
					loopRows[row] = loopRows[row].replace("S","|")
				# Can connect to top
				elif(loopRows[row-1][char] in "F|"):
					loopRows[row] = loopRows[row].replace("S","L")
				# Can't connect to top
				else:
					loopRows[row] = loopRows[row].replace("S","F")
			# Start on right edge
			elif(char == len(loopRows[0])-1):
				# Can't connect to left
				if(loopRows[row][char-1] not in "FL-"):
					loopRows[row] = loopRows[row].replace("S","|")
				# Can connect to top
				elif(loopRows[row-1][char] in "7|"):
					loopRows[row] = loopRows[row].replace("S","J")
				# Can't connect to top
				else:
					loopRows[row] = loopRows[row].replace("S","7")
			# Start on top edge
			elif(row == 0):
				# Can't connect to bottom
				if(loopRows[row+1][char] not in "LJ|"):
					loopRows[row] = loopRows[row].replace("S","-")
				# Can connect to left
				elif(loopRows[row][char-1] in "F-"):
					loopRows[row] = loopRows[row].replace("S","7")
				# Can't connect to left
				else:
					loopRows[row] = loopRows[row].replace("S","F")
			# Start on bottom edge
			elif(row == len(loopRows)-1):
				# Can't connect to top
				if(loopRows[row-1][char] not in "F7|"):
					loopRows[row] = loopRows[row].replace("S","-")
				# Can connect to left
				elif(loopRows[row][char-1] in "L-"):
					loopRows[row] = loopRows[row].replace("S","J")
				# Can't connect to left
				else:
					loopRows[row] = loopRows[row].replace("S","L")
			# Start away from the edges
			else:
				north = loopRows[row-1][char] in "F7|"
				south = loopRows[row+1][char] in "LJ|"
				east = loopRows[row][char+1] in "7J-"
				west = loopRows[row][char-1] in "FL-"
				if(north and south):
					loopRows[row] = loopRows[row].replace("S","|")
				elif(east and west):
					loopRows[row] = loopRows[row].replace("S","-")
				elif(north and west):
					loopRows[row] = loopRows[row].replace("S","J")
				elif(north and east):
					loopRows[row] = loopRows[row].replace("S","L")
				elif(south and west):
					loopRows[row] = loopRows[row].replace("S","7")
				elif(south and east):
					loopRows[row] = loopRows[row].replace("S","F")

searching = True
currentPos = list(startPos)
loopLength = 0
while(searching):
	row = currentPos[0]
	char = currentPos[1]
	currentDistance = loopDistances[row][char]
	currentChar = loopRows[row][char]
	north = currentChar in "LJ|"
	south = currentChar in "F7|"
	east = currentChar in "FL-"
	west = currentChar in "7J-"
	if(north and loopDistances[row-1][char] > currentDistance+1):
		currentPos[0] -= 1
	elif(south and loopDistances[row+1][char] > currentDistance+1):
		currentPos[0] += 1
	elif(east and loopDistances[row][char+1] > currentDistance+1):
		currentPos[1] += 1
	elif(west and loopDistances[row][char-1] > currentDistance+1):
		currentPos[1] -= 1
	else:
		searching = False
	loopLength += 1
	loopDistances[currentPos[0]][currentPos[1]] = currentDistance+1

for row in loopDistances:
	row = ["." if distance == loopArea else distance for distance in row]

print(int(loopLength/2))