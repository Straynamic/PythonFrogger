#Jesse Clem 2018
import math #http://stackoverflow.com/questions/19501279/how-do-i-only-round-a-number-float-down-in-python
import webbrowser #http://stackoverflow.com/questions/4302027/how-to-open-a-url-in-python
import time #http://stackoverflow.com/questions/510348/how-can-i-make-a-time-delay-in-python
#http://stackoverflow.com/questions/4706989/how-to-get-the-number-of-elements-in-a-python-list


#Function to "clear" the screen
cls = lambda: print('\n' * 100)

#Cords of player
playerPosition = [7,13]
initialMovement = playerPosition


playerRiding = False
playerLife = 3
score = 0
turns = 0


#Size of level
gridSize = [15,14]


#Container for all enemies [x,y,Direction]
#Simply add 3 new numbers to add an enemy to the game
enemyPositions = []
enemyNumber = 0


#Container for all logs [x,y,Direction]
#Simply add 3 new numbers to add a log to the game
logPositions = []
logNumber = 0


occupiedSlots = []

gameOver = False







#Draws the level, and the player
def drawScene():
    holder = "" #Stores stuff to print
    for y in range(gridSize[1]):
        holder = ""
        for x in range(gridSize[0]):
            #Player Position
            if(playerPosition[0] == x and playerPosition[1] == y):
                holder = whatToDraw(holder,2) #Player
            #Checks list of enemys if current spot is occupied
            elif(EnemyPosition(x,y)):
                holder = whatToDraw(holder,4) #Enemy
            #Checks list of logs if current spot is occupied
            elif(LogPosition(x,y)):
                holder = whatToDraw(holder,7) #Log
            #Water Drawing
            elif (y > 0 and y < 7):
                holder = whatToDraw(holder,3) #Water
            #OccupiedLiliPads
            elif(y == 0 and x % 2 and occupiedByPlayer(x,y)):
                holder = whatToDraw(holder,8) #Occupied
            #LiliPads
            elif(y == 0 and x % 2):
                holder = whatToDraw(holder,5) #LiliPads
            #Road Drawing
            elif (y > 7 and y < 13):
                holder = whatToDraw(holder,6) #Water
            #Empty Space
            else:
                holder = whatToDraw(holder,1) #Grass
        print(holder)





#selective drawing
def whatToDraw(holder, artType):
    #Grass
    if artType == 1:
        holder += "- "
        return holder
    #Player
    if artType == 2:
        holder += "O "
        return holder
    #Water
    if artType == 3:
        holder += "~ "
        return holder
    #Enemy
    if artType == 4:
        holder += "X "
        return holder
    #LiliPad
    if artType == 5:
        holder += "u "
        return holder
    #Road
    if artType == 6:
        holder += "= "
        return holder
    #Log
    if artType == 7:
        holder += "l "
        return holder
    #Occupied
    if artType == 8:
        holder += "o "
        return holder


def occupiedByPlayer(x,y):
    global occupiedSlots
    
    numberOccupied = len(occupiedSlots) / 2
    numberOccupied = math.floor(numberOccupied)

    cordsAndDirection = 0
    for i in range (numberOccupied):    
        if(occupiedSlots[cordsAndDirection : cordsAndDirection + 2] == [x,y]):
            return True
        cordsAndDirection += 2
    return False
        

#Checks the position of each enemy
def EnemyPosition(x,y):
    cordsAndDirection = 0
    for i in range (enemyNumber):    
        if(enemyPositions[cordsAndDirection : cordsAndDirection + 2] == [x,y]):
            return True
        cordsAndDirection += 3
    return False




#Checks the position of each log
def LogPosition(x,y):
    cordsAndDirection = 0
    for i in range (logNumber):    
        if(logPositions[cordsAndDirection : cordsAndDirection + 2] == [x,y]):
            return True
        cordsAndDirection += 3
    return False




#Changes the players stored cords depending on input
def movePlayer(playerInput1):
    global playerPosition
    global wallPosition
    global initialMovement
    global score
    global occupiedSlots
    global turns
    
    cls()

    turns += 1
    initialMovementLocal = playerPosition[:]
    
    if(playerInput1 == "w"):
        playerPosition[1]-=1
    elif(playerInput1 == "a"):
        playerPosition[0]-=1
    elif(playerInput1 == "s"):
        playerPosition[1]+=1
    elif(playerInput1 == "d"):
        playerPosition[0]+=1
    elif(playerInput1 == "secret"):
        webbrowser.open('https://www.youtube.com/watch?v=gMUEFZXkmDA')



    #Hits invisible walls at lilipads
    if(playerPosition[1] == 0 and (playerPosition[0] + 1) % 2):
        print("Hitting Wall")
        playerPosition[:] = initialMovementLocal

    if(playerPosition[1] == 0 and playerPosition[0] % 2 and occupiedByPlayer(playerPosition[0],playerPosition[1])):
        print("Occupied Space")
        playerPosition[:] = initialMovementLocal
        
    elif(playerPosition[1] == 0 and (playerPosition[0]) % 2):
        print("You've reached the end!")
        score += 1
        occupiedSlots += playerPosition
        playerPosition = [7,13]

    if  playerPosition[0] >= gridSize[0]:
        print("Hitting Border")
        playerPosition[:] = initialMovementLocal
        
    if playerPosition[1] >= gridSize[1]:
        print("Hitting Border")
        playerPosition[:] = initialMovementLocal

    if playerPosition[1] < 0:
        print("Hitting Border")
        playerPosition[:] = initialMovementLocal

    if playerPosition[0] < 0:
        print("Hitting Border")
        playerPosition[:] = initialMovementLocal



#Determines under what conditions the player dies
def handlePlayerDeath():
    global playerPosition
    global playerRiding
    global enemyPosition
    global playerLife
    global gameOver

    dead = False
    
    if EnemyPosition(playerPosition[0],playerPosition[1]):
        dead = True
    if (playerPosition[1] > 0 and playerPosition[1] < 7 and playerRiding == False):
        dead = True
        
    if(dead == True):
        print("//////////////////////////////")
        print("//         You Died         //")
        print("////////////////////////////// \n\n\n\n")
        
        playerLife -= 1
        time.sleep(1)
        if playerLife == 0:
            gameOver = True
        playerPosition = [7,13]




#Update Enemy Movement
def Enemy():
    cordsAndDirection = 0
    for i in range (enemyNumber):    
        newEnemyPosition = enemyPositions[cordsAndDirection : cordsAndDirection + 3]
        
        if( newEnemyPosition[2] == 1):
            newEnemyPosition[0] += 1
        else:
            newEnemyPosition[0] -= 1
 
        if newEnemyPosition[0] == gridSize[0] and newEnemyPosition[2] == 1:
            newEnemyPosition[0] = 0
        if newEnemyPosition[0] == -1 and newEnemyPosition[2] == 0:
            newEnemyPosition[0] = gridSize[0] - 1
            
        enemyPositions[cordsAndDirection : cordsAndDirection + 3] = newEnemyPosition
        
        cordsAndDirection += 3

#Determines where the log moves, and how it impacts the player
def Log():
    cordsAndDirection = 0
    for i in range (logNumber):    
        newLogPosition = logPositions[cordsAndDirection : cordsAndDirection + 3]

        global playerPosition
        global playerRiding
        if playerPosition == newLogPosition[0:2]:
            print("onlog")

            movementValue = 0
            
            if newLogPosition[2] == 0:
                movementValue = -1
            #                         Fixes a glitch with logs moving right
            if newLogPosition[2] == 1 and playerRiding == False:
                movementValue = 1
            
            tempPlayer = playerPosition[:]
            tempPlayer[0] = tempPlayer[0] + movementValue
            playerPosition[:] = tempPlayer

            playerRiding = True
        
        if( newLogPosition[2] == 1):
            newLogPosition[0] += 1
        else:
            newLogPosition[0] -= 1
 
        if newLogPosition[0] == gridSize[0] and newLogPosition[2] == 1:
            newLogPosition[0] = 0
        if newLogPosition[0] == -1 and newLogPosition[2] == 0:
            newLogPosition[0] = gridSize[0] - 1
        
            
        logPositions[cordsAndDirection : cordsAndDirection + 3] = newLogPosition
        
        cordsAndDirection += 3



#initializes where all AI is placed
def aiPositions():
    global logPositions
    global enemyPositions

    # [X,Y,Direction] , # = Continuous
    
    #Y=13 (Player Spawn) (Grass)
    #Y=12
    enemyPositions += [1,12,1]
    enemyPositions += [9,12,1]
    #Y=11
    enemyPositions += [2,11,0]
    enemyPositions += [6,11,0]
    enemyPositions += [10,11,0]
    #Y=10
    enemyPositions += [2,10,1] #
    enemyPositions += [3,10,1]
    enemyPositions += [4,10,1]
    enemyPositions += [5,10,1]

    #Y=9
    enemyPositions += [3,9,0] #
    enemyPositions += [4,9,0]
    enemyPositions += [9,9,0] #
    enemyPositions += [10,9,0]
    #Y=8
    enemyPositions += [3,8,1]
    enemyPositions += [8,8,1]
    enemyPositions += [12,8,1]
    #Y=7 (Grass)
    #Y=6
    logPositions += [2,6,1] #
    logPositions += [3,6,1]
    logPositions += [4,6,1]
    logPositions += [7,6,1] #
    logPositions += [8,6,1]
    logPositions += [9,6,1]
    logPositions += [12,6,1] #
    logPositions += [13,6,1]
    logPositions += [14,6,1]
    #Y=5
    logPositions += [1,5,0] #
    logPositions += [2,5,0]
    logPositions += [3,5,0]
    logPositions += [4,5,0]
    logPositions += [9,5,0] #
    logPositions += [10,5,0]
    logPositions += [11,5,0]
    logPositions += [12,5,0]
    #Y=4
    logPositions += [2,4,1] #
    logPositions += [3,4,1]
    logPositions += [4,4,1]
    logPositions += [7,4,1] #
    logPositions += [8,4,1]
    logPositions += [9,4,1]
    logPositions += [12,4,1] #
    logPositions += [13,4,1]
    logPositions += [14,4,1]
    #Y=3
    logPositions += [1,3,0] #
    logPositions += [2,3,0]
    logPositions += [3,3,0]
    logPositions += [4,3,0]
    logPositions += [9,3,0] #
    logPositions += [10,3,0]
    logPositions += [11,3,0]
    logPositions += [12,3,0]
    #Y=2
    logPositions += [2,2,1] #
    logPositions += [3,2,1]
    logPositions += [4,2,1]
    logPositions += [7,2,1] #
    logPositions += [8,2,1]
    logPositions += [9,2,1]
    logPositions += [12,2,1] #
    logPositions += [13,2,1]
    logPositions += [14,2,1]
    #Y=1
    logPositions += [1,1,0] #
    logPositions += [2,1,0]
    logPositions += [3,1,0]
    logPositions += [4,1,0]
    logPositions += [9,1,0] #
    logPositions += [10,1,0]
    logPositions += [11,1,0]
    logPositions += [12,1,0]
    #Y=0 (LiliPads)




#Screen when the player runs out of lives
def gameOverScreen():
    global score
    global turns
    
    cls()
    print("//////////////////////////////")
    print("//         You Died         //")
    print("////////////////////////////// \n\n\n\n")
    time.sleep(1)
    print("/////////////////////////////")
    print("//        Game Over        //")
    print("/////////////////////////////")
    time.sleep(2)
    print("Moves:", turns)
    print("Score:", score)
    
    playAgain(input("\n\n\n\n\n\n\nContinue? Y/N: "))

def winScreen():
    global score
    global turns
    
    cls()
    print("//////////////////////////////")
    print("//         You Win!         //")
    print("//////////////////////////////")
    time.sleep(2)
    print("Moves:", turns)
    print("Score:", score)
    playAgain(input("\n\n\n\n\n\n\nContinue? Y/N: "))
    

#Gets player input after game over
def playAgain(Input):
    global gameOver
    global playerLife
    global score
    global occupiedSlots
    global turns
    
    if(Input == "y"):
        print("");
        gameOver = False
        score = 0
        turns = 0
        playerLife = 3
        occupiedSlots = []
        initialize()
        
    if(Input == "n"):
        print("");
        gameOver = True




#Runs the main loop until the game is over
def main():
    
    while not gameOver:

        global playerRiding
        global score
        global turns
        playerRiding = False
        
        Enemy()
        movePlayer(input("\nPress W A S D, then enter to move"))
        Log()
        handlePlayerDeath()
        
        print("Crager & Clem's Game of Frogger")
        print("Score:", score, "\tLives:", playerLife)
        
        
        #Draw the game board
        drawScene()
        
        print("Player Cords:", playerPosition)
        print("Moves:", turns)

        if(score == 7):
            winScreen()
        
    if(gameOver == True and score != 7):
        gameOverScreen()
    cls()
        

# warmup
def initialize():
    cls()
    drawScene()
    main()



#Start the program
aiPositions()

number = len(enemyPositions) / 3
enemyNumber = math.floor(number)

number = len(logPositions) / 3
logNumber = math.floor(number)

print('\n' * 10000) #Smooths console run gameplay

initialize()

