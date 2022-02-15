# Conway's Game of Life
from ast import While
from calendar import c
from email.header import Header
import random, time, copy

WIDTH = 60
HEIGHT = 20

#Create a list of list for the cells
nextCells = []
for x in range(WIDTH):
    column = [] #Create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # Add a living cell
        else:
            column.append(' ') #Add a dead cell
    nextCells.append(column) #nextCells is a list of column lists

while True: # Main program loop
    print('\n\n\n\n\n') #Seperate each step with new lines
    currentCells = copy.deepcopy(nextCells)

    #Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') #Print the # or space.
        print() #Print a newline at the end of the row

    # Calculate the nex steps cells based on current steps cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):\
            #Get neighbouring coordinates:
            # '% WIDTH' ensures leftCoord is always between 0 and WIDTH -1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            #Count number of living neighbours:
            numNeighbours = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbours += 1 # Top-left neighbour is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbours += 1 #Top neighbour is alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbours += 1 #Top right neighbour is alive
            if currentCells[leftCoord][y] == '#':
                numNeighbours += 1 # Left neighbour is alive
            if currentCells[rightCoord][y] == '#':
                numNeighbours += 1 #right neighbour is alive
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbours +=1 #left bottom neighbour is alive
            if currentCells[x][belowCoord] == '#':
                numNeighbours += 1 #bottom neighbour is alive
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbours += 1 #bottom right neighbour is alive

            #set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbours == 2 or numNeighbours == 3):
                # Living Cells with 2 or 3 neighbours stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbours == 3:
                #Dead Cells with 3 neighbours come alive
                nextCells[x][y] = '#'
            else:
                #everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(1) #add a 1-second pause to reduce flickering