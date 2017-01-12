
class Maze:
	
	def __init__(self):
		self.data  = [[1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],  
			 [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1 ],
			 [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1 ],
			 [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1 ],
			 [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1 ],
			 [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1 ],
			 [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1 ],
			 [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1 ],
			 [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1 ],
			 [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1 ],
			 [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1 ],
			 [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1 ],
			 [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 ],
			 [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 ],
			 [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1 ],
			 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1 ],
			 [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1 ]]
	 
def findGoalPoint(self):
	for index, value in enumerate(maze[0]):
		if value == 0:
			return (0, index)

def findStartPoint(self):
	for index, value in enumerate(maze[-1]):
		if value == 0:
			return (len(maze)-1, index)
					

def goNorth(state):
	return (state[0]-1, state[1])

def goSouth(state):
	return (state[0]+1, state[1])
	
def goEast(state):
	return (state[0], state[1]+1)

def goWest(state):
	return (state[0], state[1]-1)

def applyDirection(direction, state):
	Position = ""
	if direction == "North":
		Position = goNorth(state)
	elif direction ==  "South":
		Position = goSouth(state)
	elif direction == "East":
		Position = goEast(state)
	elif direction 	== "West":
		Position = goWest(state)
	return Position

def findParent(state, positionHeuristics, costOrRemainingDistance):
	for index, element in enumerate(costOrRemainingDistance):
		for idx, val in enumerate(element):
			if idx < 2:
				if state in val:
					return (positionHeuristics[index], index)

	
def mazeHeight(maze):
	return len(maze)
	
def mazeWidth(maze):
	return len(maze[0])
	
def valueOfPosition(state, maze):
	return maze[state[0]][state[1]]

def printMaze(maze,currentPosition):
		x=0
		print "\n\n--------------------------------------------"
		print "       PRINTING MAZE - VISUALIZATION"
		print "--------------------------------------------\n"
		print "       0 0 0 0 0 0 0 0 0 0 1 1 1 1 1"
		print "       0 1 2 3 4 5 6 7 8 9 0 1 2 3 4"
		print "       | | | | | | | | | | | | | | |"
		for i in range(len(maze)):
			if x<=9:
			   print '   0%d-' % x,
			   x=x+1
			else:
				print '   %d-' % x,
				x=x+1
			for j in range(len(maze[0])):
				if maze[i][j] == 1:
					print u"\u2588",
				else:
		 			if i==currentPosition[0] and j==currentPosition[1]:
						print "@",
					else:
						print " ",
			print ""
		print "\n    Current Position = \t",currentPosition
		print "--------------------------------------------"
		raw_input('Press <ENTER> to continue')


def printPath(maze,visited):
		x=0
		print "\n\n--------------------------------------------"
		print "       PRINTING MAZE - ALL VISITED PATHS"
		print "--------------------------------------------\n"
		print "       0 0 0 0 0 0 0 0 0 0 1 1 1 1 1"
		print "       0 1 2 3 4 5 6 7 8 9 0 1 2 3 4"
		print "       | | | | | | | | | | | | | | |"
		for indI,valI in enumerate(maze):
			if x<=9:
			   print '   0%d-' % x,
			   x=x+1
			else:
				print '   %d-' % x,
				x=x+1
			for indJ, valJ in enumerate(valI):
				if (indI, indJ) in visited:
					print "*",
				else:
					if valJ == 1:
						print u"\u2588",
					else:
						print " ",	
			print ""
		print "\n    Final Position = \t",visited[-1]
		print "--------------------------------------------"
		print "                 END MAZE"
		print "--------------------------------------------"
		raw_input('Press <ENTER> to continue')


def applyDirections(maze, positionHeuristics, visited,goalState):
	directions = ["North","South", "East", "West"]
	i = 0
	currentPosition = visited[-1]
	while currentPosition not in positionHeuristics and (currentPosition != goalState):
		
		if (directions[i] == "North"):
			nextPosition = goNorth(currentPosition)
			if (nextPosition[0] < 0 or valueOfPosition(nextPosition, maze) == 1):
				i += 1
			elif nextPosition in visited:
				i += 1
			else:
				currentPosition = nextPosition
				if currentPosition not in visited:
					visited.append(currentPosition)
					print "VISITED:",visited
					printMaze(maze,currentPosition)
				i = 0
				
				
		elif (directions[i] == "South"):
			nextPosition = goSouth(currentPosition)
			if (nextPosition[0] >= mazeHeight(maze) or valueOfPosition(nextPosition, maze) == 1):
				i += 1
			elif nextPosition in visited:
				i += 1
			else:
				currentPosition = nextPosition
				if currentPosition not in visited:
					visited.append(currentPosition)
					print "VISITED:",visited
					printMaze(maze,currentPosition)
				i = 0

		elif (directions[i] == "East"):
			nextPosition = goEast(currentPosition)
			if (nextPosition[1] > mazeWidth(maze) or valueOfPosition(nextPosition, maze) == 1):
				i += 1
			elif nextPosition in visited:
				i += 1
			else:
				currentPosition = nextPosition
				if currentPosition not in visited:
					visited.append(currentPosition)
					print "VISITED:",visited
					printMaze(maze,currentPosition)
				i = 0

		elif (directions[i] == "West"):
			nextPosition = goWest(currentPosition)
			if (nextPosition[0] < 0 or valueOfPosition(nextPosition, maze) == 1):
				i += 1
			elif nextPosition in visited:
				i += 1
			else:
				currentPosition = nextPosition
				if currentPosition not in visited:
					visited.append(currentPosition)
					print "VISITED:",visited
					printMaze(maze,currentPosition)
				i = 0
		
		

		#print currentPosition , "   '", i

	return visited

def sortList(opened,positionHeuristics,remainingDistance):
	unsorted=[]
	for element in opened:
		i = positionHeuristics.index(element)
		unsorted.append((element, remainingDistance[i][2]))
	sortedList = sorted(unsorted, key=lambda distance:distance[1])
	opened = []
	for element in sortedList:
		opened.append(element[0])
	return opened

def hillClimbing (maze,positionHeuristics,remainingDistance):
	print "  \n\n  ****************************************************"
	print "  ****************************************************"
	print "  **                 Hill Climbing                  **"
	print "  ****************************************************"
	print "  ****************************************************"
	startState = findStartPoint(maze)
	goalState = findGoalPoint(maze)	
	currentPosition = startState
	visited = [currentPosition]
	printMaze(maze, currentPosition)
	while not (currentPosition == goalState):
		if currentPosition not in positionHeuristics:
			visited = applyDirections(maze, positionHeuristics, visited,goalState)
			currentPosition = visited[-1]
		else : 
			i = positionHeuristics.index(currentPosition)
			if remainingDistance[i][0] == "deadEnd":
				print "  ****************************************************"
				print "  ****************************************************"
				print "  ** Hill Climbing reached a deadend , we are stuck **"
				print "  ****************************************************"
				print "  ****************************************************"
				visited.append(currentPosition)
				break
			elif (remainingDistance[i][0][1] < remainingDistance[i][1][1]):
					chosenDirection =  remainingDistance[i][0][0]
			else:
					chosenDirection =  remainingDistance[i][1][0]
			currentPosition = applyDirection(chosenDirection, currentPosition)
			printMaze(maze, currentPosition)
			visited.append(currentPosition)
		
	
	return visited

def bestFirstSearch(maze,positionHeuristics,remainingDistance):	
	print "  \n\n  ****************************************************"
	print "  ****************************************************"
	print "  **              BEST FIRST SEARCH                 **"
	print "  ****************************************************"
	print "  ****************************************************"
	startState = findStartPoint(maze)
	goalState = findGoalPoint(maze)	
	currentPosition = startState
	printMaze(maze, currentPosition)
	visited = [currentPosition]
	opened = []
	closed = []
	while not (currentPosition == goalState):
		if currentPosition not in positionHeuristics:
			visited = applyDirections(maze, positionHeuristics, visited,goalState)
			currentPosition = visited[-1]
			if (visited[-1]) not in opened:
				opened.append(visited[-1])
		else: 
			i = positionHeuristics.index(opened[0])
			if  (remainingDistance[i][0] != "deadEnd"):
				opened.append(remainingDistance[i][0][2])
				opened.append(remainingDistance[i][1][2])
				closed.append(opened.pop(0))
				opened  = sortList(opened,positionHeuristics,remainingDistance)
				if (remainingDistance[i][0][2] == opened[0]):
					chosenDirection =  remainingDistance[i][0][0]
				else:
					chosenDirection =  remainingDistance[i][1][0]
				currentPosition = applyDirection(chosenDirection, currentPosition)
			else:
				closed.append(opened.pop(0))
				currentPosition = opened[0]
			
			printMaze(maze, currentPosition)
			visited.append(currentPosition)
			print "OPEN:" , opened
			
	return visited



def beamSearch(maze,positionHeuristics,remainingDistance):
	print "  \n\n  ****************************************************"
	print "  ****************************************************"
	print "  **                  BEAM SEARCH                   **"
	print "  ****************************************************"
	print "  ****************************************************"
	startState = findStartPoint(maze)
	goalState = findGoalPoint(maze)	
	currentPosition = startState
	printMaze(maze, currentPosition)
	visited = [currentPosition]
	queue = []
	new_queue = []
	w = 2
	while not (currentPosition == goalState ):
		if currentPosition not in positionHeuristics:
			visited = applyDirections(maze, positionHeuristics, visited,goalState)
			currentPosition = visited[-1]
			if (visited[-1]) not in queue:
				if queue == []:
					queue.append((visited[-1], 0))
		else: 
			i = positionHeuristics.index(queue[0][0])
			if  (remainingDistance[i][0] != "deadEnd"):
				
				new_queue.append((remainingDistance[i][0][2], remainingDistance[i][0][1] ))
				new_queue.append((remainingDistance[i][1][2], remainingDistance[i][1][1] ))
				print "new Q", new_queue
				new_queue  = sorted(new_queue, key=lambda cost:cost[1])
				print "new Q 2", new_queue
				new_queue = new_queue[:w]
				print "new Q 3", new_queue

				queue.pop(0)
				print "Q", queue

				if queue == []:
					queue = new_queue
					new_queue = []

				parent = findParent(queue[0][0], positionHeuristics, remainingDistance)
				currentPosition = parent[0]
				if (queue[0][0] == remainingDistance[parent[1]][0][2]):
					chosenDirection =  remainingDistance[parent[1]][0][0]
				else:
					chosenDirection =  remainingDistance[parent[1]][1][0]

				currentPosition = applyDirection(chosenDirection, currentPosition)
				print "Q 2", queue

			else:
				queue.pop(0)
				if queue == []:
					queue = new_queue
					new_queue = []

				print "Q 3", queue
				print "N Q 3", new_queue
				
				parent = findParent(queue[0][0], positionHeuristics, remainingDistance)
				currentPosition = parent[0]
				if (queue[0][0] == remainingDistance[parent[1]][0][2]):
					chosenDirection =  remainingDistance[parent[1]][0][0]
				else:
					chosenDirection =  remainingDistance[parent[1]][1][0]
				currentPosition = applyDirection(chosenDirection, currentPosition)


				print "Q 3", queue

	
			print "current Pos", currentPosition

			printMaze(maze, currentPosition)
			visited.append(currentPosition)
			print "QUEUE:",queue
			
	return visited

def branchAndBoundSearch(maze,positionHeuristics,positionCost):	
	print "  \n\n  ****************************************************"
	print "  ****************************************************"
	print "  **                BRANCH AND BOUND                **"
	print "  ****************************************************"
	print "  ****************************************************"
	startState = findStartPoint(maze)
	goalState = findGoalPoint(maze)	
	currentPosition = startState
	printMaze(maze, currentPosition)
	visited = [currentPosition]
	queue = []
	closed = []
	while not (currentPosition == goalState ):
		if currentPosition not in positionHeuristics:
			visited = applyDirections(maze, positionHeuristics, visited,goalState)
			currentPosition = visited[-1]
			if (visited[-1]) not in queue:
				if queue == []:
					queue.append((visited[-1], 0))
		else: 
			i = positionHeuristics.index(queue[0][0])
			if  (remainingDistance[i][0] != "deadEnd"):
				queue.append((remainingDistance[i][0][2], positionCost[i][0][1] + queue[0][1]))
				queue.append((positionCost[i][1][2], positionCost[i][1][1] + queue[0][1]))
				closed.append(queue.pop(0))
				
				queue  = sorted(queue, key=lambda cost:cost[1])
				
				if (positionCost[i][0][2] == queue[0][0]):
					chosenDirection =  positionCost[i][0][0]
				elif (positionCost[i][1][2] == queue[0][0]):
					chosenDirection =  positionCost[i][1][0]
				else:
					parent = findParent(queue[0][0], positionHeuristics, positionCost)
					currentPosition = parent[0]
					if (queue[0][0] == positionCost[parent[1]][0][2]):
						chosenDirection =  positionCost[parent[1]][0][0]
					else:
						chosenDirection =  positionCost[parent[1]][1][0]
				currentPosition = applyDirection(chosenDirection, currentPosition)

			else:								
				queue.pop(0)
				parent = findParent(queue[0][0], positionHeuristics, positionCost)
				currentPosition = parent[0]
				if (queue[0][0] == positionCost[parent[1]][0][2]):
					chosenDirection =  positionCost[parent[1]][0][0]
				else:
					chosenDirection =  positionCost[parent[1]][1][0]
				currentPosition = applyDirection(chosenDirection, currentPosition)

			printMaze(maze, currentPosition)
			visited.append(currentPosition)
			print "QUEUE:",queue
			
	return visited


def branchAndBoundSearchWithUnderestimate(maze,positionHeuristics,positionCost,remainingDistance):
	print "  \n\n  ****************************************************"
	print "  ****************************************************"
	print "  **       BRANCH AND BOUND WITH UNDERESTIMATE      **"
	print "  ****************************************************"
	print "  ****************************************************"	
	startState = findStartPoint(maze)
	goalState = findGoalPoint(maze)	
	currentPosition = startState
	printMaze(maze, currentPosition)
	visited = [currentPosition]
	queue = []
	closed = []
	while  (currentPosition != goalState ):
		if currentPosition not in positionHeuristics:
			visited = applyDirections(maze, positionHeuristics, visited,goalState)
			currentPosition = visited[-1]
			if (visited[-1]) not in queue:
				if queue == []:
					queue.append((visited[-1], 0))
		else: 
			i = positionHeuristics.index(queue[0][0])
			if  (positionCost[i][0] != "deadEnd"):
				if queue[0][0] == (15,9):
					queue.append((positionCost[i][0][2], (positionCost[i][0][1] + queue[0][1] + remainingDistance[i][0][1])))
					queue.append((positionCost[i][1][2], (positionCost[i][1][1] + queue[0][1] + remainingDistance[i][1][1])))
					closed.append(queue.pop(0))
				else:
					parent = findParent(positionCost[i][0][2], positionHeuristics, positionCost)
					queue.append((positionCost[i][0][2], (positionCost[i][0][1] + queue[0][1] + remainingDistance[i][0][1]-remainingDistance[parent[1]][2])))
					queue.append((positionCost[i][1][2], (positionCost[i][1][1] + queue[0][1] + remainingDistance[i][1][1]-remainingDistance[parent[1]][2])))
					closed.append(queue.pop(0))

				queue  = sorted(queue, key=lambda cost:cost[1])
				
				if (positionCost[i][0][2] == queue[0][0]):
					chosenDirection =  positionCost[i][0][0]
				elif (positionCost[i][1][2] == queue[0][0]):
					chosenDirection =  positionCost[i][1][0]
				else:
					parent = findParent(queue[0][0], positionHeuristics, positionCost)
					currentPosition = parent[0]
					if (queue[0][0] == positionCost[parent[1]][0][2]):
						chosenDirection =  positionCost[parent[1]][0][0]
					else:
						chosenDirection =  positionCost[parent[1]][1][0]

				currentPosition = applyDirection(chosenDirection, currentPosition)

			else:								
				queue.pop(0)
				parent = findParent(queue[0][0], positionHeuristics, positionCost)
				currentPosition = parent[0]
				if (queue[0][0] == positionCost[parent[1]][0][2]):
					chosenDirection =  positionCost[parent[1]][0][0]
				else:
					chosenDirection =  positionCost[parent[1]][1][0]
				currentPosition = applyDirection(chosenDirection, currentPosition)

			printMaze(maze, currentPosition)
			visited.append(currentPosition)
			print "QUEUE:",queue
			
	return visited


def branchAndBoundSearchWithDynamicProgrming(maze,positionHeuristics,positionCost):	
	print "  \n\n  ****************************************************"
	print "  ****************************************************"
	print "  **    BRANCH AND BOUND WITH DYNAMIC PROGRAMING    **"
	print "  ****************************************************"
	print "  ****************************************************"
	startState = findStartPoint(maze)
	goalState = findGoalPoint(maze)	
	currentPosition = startState
	printMaze(maze, currentPosition)
	visited = [currentPosition]
	queue = []
	closed = []
	while not (currentPosition == goalState ):
		if currentPosition not in positionHeuristics:
			visited = applyDirections(maze, positionHeuristics, visited,goalState)
			currentPosition = visited[-1]
			if not currentPosition  in queue:
				if queue == []:
					queue.append((currentPosition, 0))
			else:
				queueIndex = queue.index(currentPosition)
				cost = queue[queueIndex][1]
				
				if cost > (positionCost[positionHeuristics.index(currentPosition)][0][1] + queue[0][1]):
					queue[queueIndex][1] = (positionCost[positionHeuristics.index(currentPosition)][0][1] + queue[0][1])
		else: 
			i = positionHeuristics.index(queue[0][0])
			if  (positionCost[i][0] != "deadEnd"):
				queue.append((positionCost[i][0][2], positionCost[i][0][1] + queue[0][1]))
				queue.append((positionCost[i][1][2], positionCost[i][1][1] + queue[0][1]))
				closed.append(queue.pop(0))
				queue  = sorted(queue, key=lambda cost:cost[1])
				if (positionCost[i][0][2] == queue[0][0]):
					chosenDirection =  positionCost[i][0][0]
				elif (positionCost[i][1][2] == queue[0][0]):
					chosenDirection =  positionCost[i][1][0]
				else:
					parent = findParent(queue[0][0], positionHeuristics, positionCost)
					currentPosition = parent[0]
					if (queue[0][0] == positionCost[parent[1]][0][2]):
						chosenDirection =  positionCost[parent[1]][0][0]
					else:
						chosenDirection =  positionCost[parent[1]][1][0]

				currentPosition = applyDirection(chosenDirection, currentPosition)

			else:								
				queue.pop(0)
				parent = findParent(queue[0][0], positionHeuristics, positionCost)
				currentPosition = parent[0]
				if (queue[0][0] == positionCost[parent[1]][0][2]):
					chosenDirection =  positionCost[parent[1]][0][0]
				else:
					chosenDirection =  positionCost[parent[1]][1][0]
				currentPosition = applyDirection(chosenDirection, currentPosition)

			printMaze(maze, currentPosition)
			visited.append(currentPosition)
			print "QUEUE:",queue
	
			
	return visited


def aStarSearch(maze,positionHeuristics,positionCost,remainingDistance):
	print "  \n\n  ****************************************************"
	print "  ****************************************************"
	print "  **                  A* SEARCH                     **"
	print "  ****************************************************"
	print "  ****************************************************"	
	startState = findStartPoint(maze)
	goalState = findGoalPoint(maze)	
	currentPosition = startState
	printMaze(maze, currentPosition)
	visited = [currentPosition]
	queue = []
	closed = []
	while  (currentPosition != goalState ):
		if currentPosition not in positionHeuristics:
			visited = applyDirections(maze, positionHeuristics, visited,goalState)
			currentPosition = visited[-1]
			if (visited[-1]) not in queue:
				if queue == []:
					queue.append((visited[-1], 0))
			
			else:
				queueIndex = queue.index(currentPosition)
				cost = queue[queueIndex][1]
				
				if cost > (positionCost[positionHeuristics.index(currentPosition)][0][1] + queue[0][1]):
					queue[queueIndex][1] = (positionCost[positionHeuristics.index(currentPosition)][0][1] + queue[0][1])
		else: 
			i = positionHeuristics.index(queue[0][0])
			if  (positionCost[i][0] != "deadEnd"):
				if queue[0][0] == (15,9):
					queue.append((positionCost[i][0][2], (positionCost[i][0][1] + queue[0][1] + remainingDistance[i][0][1])))
					queue.append((positionCost[i][1][2], (positionCost[i][1][1] + queue[0][1] + remainingDistance[i][1][1])))
					closed.append(queue.pop(0))
				else:
					parent = findParent(positionCost[i][0][2], positionHeuristics, positionCost)
					queue.append((positionCost[i][0][2], (positionCost[i][0][1] + queue[0][1] + remainingDistance[i][0][1]-remainingDistance[parent[1]][2])))
					queue.append((positionCost[i][1][2], (positionCost[i][1][1] + queue[0][1] + remainingDistance[i][1][1]-remainingDistance[parent[1]][2])))
					closed.append(queue.pop(0))

				
				queue  = sorted(queue, key=lambda cost:cost[1])
				
				if (positionCost[i][0][2] == queue[0][0]):
					chosenDirection =  positionCost[i][0][0]
				elif (positionCost[i][1][2] == queue[0][0]):
					chosenDirection =  positionCost[i][1][0]
				else:
					parent = findParent(queue[0][0], positionHeuristics, positionCost)
					currentPosition = parent[0]
					if (queue[0][0] == positionCost[parent[1]][0][2]):
						chosenDirection =  positionCost[parent[1]][0][0]
					else:
						chosenDirection =  positionCost[parent[1]][1][0]

				currentPosition = applyDirection(chosenDirection, currentPosition)

			else:								
				queue.pop(0)
				parent = findParent(queue[0][0], positionHeuristics, positionCost)
				currentPosition = parent[0]
				if (queue[0][0] == positionCost[parent[1]][0][2]):
					chosenDirection =  positionCost[parent[1]][0][0]
				else:
					chosenDirection =  positionCost[parent[1]][1][0]
				currentPosition = applyDirection(chosenDirection, currentPosition)

			printMaze(maze, currentPosition)
			visited.append(currentPosition)
			print "QUEUE:",queue
			
	return visited



	
if __name__ == "__main__":

	#INITIALIZING AN INSTANCE OF MAZE OBJECT 
	maze = Maze()
	maze = maze.data
	# DECLARING START & GOAL STATES
	startPoint = findStartPoint(maze)
	goalPoint = findGoalPoint(maze)
	
	# VISUALIZING MAZE
	
	print "    START STATE = \t" , startPoint
	print "    GOAL STATE  = \t", goalPoint
	
	positionHeuristics = [(15,9), (15,5), (11,5), (7,3), (5,3), (5,5), (13,3), (13,7), (9,3), (5,1), (3,3), (1,9), (0,7)]
	remainingDistance = [[("North", 75,(1,9)), ("West", 29,(15,5)),33],
						 [("West", 37,(13,3)), ("North", 25,(11,5)),29], 
						 [("East", 29,(13,7)), ("North", 19,(7,3)),25],
						 [("North", 19,(5,3)), ("West", 29,(9,3)),19], 
						 [("North", 14,(3,3)), ("East", 15,(5,5)),19], 
						 [("North", 27,(5,1)), ("East", 0,(0,7)),15], 
						 ["deadEnd",0,37],
					     ["deadEnd",0,29],
						 ["deadEnd",0,29], 
						 ["deadEnd",0,27],
			    		 ["deadEnd",0,14],
						 ["deadEnd",0,75],
						 ["Goal", 0, 0]]
	positionCost     =   [[("North", 42,(1,9)),("West", 4,(15,5))],
						 [("West", 8,(13,3)), ("North", 4,(11,5))], 
						 [("East", 4,(13,7)), ("North", 6,(7,3))],
						 [("North", 2,(5,3)), ("West", 10,(9,3))], 
						 [("North", 3,(3,3)), ("East", 2,(5,5))], 
						 [("North", 12,(5,1)), ("East", 15,(0,7))], 
						 ["deadEnd",0],
					     ["deadEnd",0],
						 ["deadEnd",0], 
						 ["deadEnd",0],
			    		 ["deadEnd",0],
						 ["deadEnd",0],
						 ["Goal", 0]]


	# DECLARING ORDER OF DIRECTIONS
	directions = ["North","South", "East", "West"]

	number = 10


	while number != "0" :
		while True:
			try:
				print " \n\t> Enter 1 for Hill Climbing Search"
				print " \t> Enter 2 for Best First Search"
				print " \t> Enter 3 for Beam Search"
				print " \t> Enter 4 for Branch and bound Search"
				print " \t> Enter 5 for Branch and bound With Underestimates Search"
				print " \t> Enter 6 for Branch and bound With Dynamic Programing Search"
				print " \t> Enter 7 for A* Search"
				print " \t> Enter 0 to EXIT"

				number = str(raw_input(" \n\t> please enter a number :  "))
			except ValueError:
				print "Sorry, Please enter a valid number"
				continue
			else:
				break

		if number == "1":
			visited =  hillClimbing(maze, positionHeuristics, remainingDistance)
			print "  \n\n  ****************************************************"
			print "  ****************************************************"
			print "  **                 Hill Climbing                  **"
			print "  ****************************************************"
			print "  ****************************************************"
			printPath(maze,visited)
		elif number == "2":
			visited =  bestFirstSearch(maze, positionHeuristics, remainingDistance)
			print "  \n\n  ****************************************************"
			print "  ****************************************************"
			print "  **              BEST FIRST SEARCH                 **"
			print "  ****************************************************"
			print "  ****************************************************"
			printPath(maze,visited)
		elif number == "3":
			visited = beamSearch(maze,positionHeuristics,remainingDistance)
			print "  \n\n  ****************************************************"
			print "  ****************************************************"
 			print "  **                   BEAM SEARCH                  **"
 			print "  ****************************************************"
		 	print "  ****************************************************"
			printPath(maze,visited)
		elif number == "4":
			visited = branchAndBoundSearch(maze,positionHeuristics,positionCost)
			print "  \n\n  ****************************************************"
			print "  ****************************************************"
			print "  **                BRANCH AND BOUND                **"
			print "  ****************************************************"
			print "  ****************************************************"
			printPath(maze,visited)
		elif number == "5":
			visited = branchAndBoundSearchWithUnderestimate(maze,positionHeuristics,positionCost,remainingDistance)
			print "  \n\n  ****************************************************"
			print "  ****************************************************"
			print "  **       BRANCH AND BOUND WITH UNDERESTIMATE      **"
			print "  ****************************************************"
			print "  ****************************************************"
			printPath(maze,visited)
		elif number == "6":
			visited = branchAndBoundSearchWithDynamicProgrming(maze,positionHeuristics,positionCost)
			print "  \n\n  ****************************************************"
			print "  ****************************************************"
			print "  **    BRANCH AND BOUND WITH DYNAMIC PROGRAMING    **"
			print "  ****************************************************"
			print "  ****************************************************"
			printPath(maze,visited)
		elif number == "7":
			visited = aStarSearch(maze,positionHeuristics,positionCost,remainingDistance)
			print "  \n\n  ****************************************************"
			print "  ****************************************************"
			print "  **                  A* SEARCH                     **"
			print "  ****************************************************"
			print "  ****************************************************"	
			printPath(maze,visited)
		elif number == "0":
			break
	


