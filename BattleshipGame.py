"""
Portions of this code are derived from w0300133
Source code: https://gist.github.com/w0300133/7f3e3e6f836e519f64272150ca34080c
Edits by Beau Anderson, Anna Watson, and George Engel
"""


# --- Import needed data libraries ---
import csv
import time

class BattleshipGame():
    global currentMap
    global previousShots
    # TODO file in parameters
    def __init__(self, file):
        self.file = file
            #TODO: make own_board.txt input through server parameters(in init Game)
        fileName = "own_board.txt"  # file where the ship layout is kept
        accessMode = "r"  # access mode w to write to the file
        shipMap = []
        self.shipMap = shipMap
        shotCoordinateList = []
        self.shotCoordinateList = shotCoordinateList

        try:
            with open(fileName, accessMode) as fileData:
                shipLocations = csv.reader(fileData)
                for row in shipLocations:
                    shipMap.append(row)
        except FileNotFoundError:
            print("Sorry, there was an error loading a required file.")

        global currentMap
        currentMap = self.generateStartMap(10)
        global previousShots
        previousShots = []

    BattleshipHit = 4
    SubmarineHit = 3
    DestroyerHit = 2
    CarrierHit = 5
    CruiserHit = 3

    # --- Function definition for generateStartMap ---
    # Will take in the size of the map to be made and produce an empty starting map for the game.
    def generateStartMap(self,size):
        startingMap = []
        for counter in range(size):
            currentLine = []
            for counter in range(size):
                currentLine.append("~")
            startingMap.append(currentLine)

        return startingMap

    #usershot is a string of two ints; IE; "12" or x=1, y=2
    def shoot(self, x, y):
        userShot = (str(x) + str(y))
        print(userShot)
        previousShots.append(userShot)
        self.shotCoordinateList = self.shotToNumbers(userShot, self.validColumns)

        print(self.shipMap)

        # --- Check the shot vs. shipMap to verify a hit or miss ---
        self.shotResult = self.checkHit(self.shotCoordinateList, self.shipMap)
        print(self.shotResult[1])

        # --- Update the  game map to refer to when checking ship status ---
        self.shipMap = self.updateMap(self.shotCoordinateList, "X", self.shipMap)
        return (self.shotResult[0])

    def checkStillAlive(self):
        # - Check the status of the ships to check win condition -
        shipsStillAlive = checkShipStatus(shipSymbols, shipMap)
        for index in range(len(shipsStillAlive)):
            if shipsStillAlive[index]:
                print("The " + shipNames[index] + " still sails!")
            else:
                print("You have sunk the " + shipNames[index] + "!")

        # - Check win condition. If not ships remain end the game. ---
        if True not in shipsStillAlive:
            print("Good shooting! You have destroyed the enemy fleet!")

    # --- Function definition for shotToNumbers ---
    # Will take in a string of a letter and number and return a list of two numbers.
    def shotToNumbers(self,coordinateString, headingsList):
        shotList = []
        shotList.append(int(coordinateString[1]))

        for column in headingsList:
            if coordinateString[0] == column:
                shotList.append(headingsList.index(column))

        return shotList

    # --- Function definition for checkHit ---
    # Will take in shotCoordinateList and shipMap and return whether the shot hit or missed.
    def checkHit(self,shot, map):
        global BattleshipHit
        global SubmarineHit
        global DestroyerHit
        global CarrierHit
        global CruiserHit

        print(map[shot[0]][shot[1]])
        if map[shot[0]][shot[1]] == "0":
            return ["X", "Miss!"]
        elif map[shot[0]][shot[1]] == "B":
            self.BattleshipHit = self.BattleshipHit - 1
            if self.BattleshipHit == 0:
                return ["B1]", "You sunk the BATTLESHIP!"]
            else:
                return ["H", "HIT!"]
        elif map[shot[0]][shot[1]] == "S":
            self.SubmarineHit -= 1
            if self.SubmarineHit == 0:
                return ["S", "You sunk the SUBMARINE!"]
            else:
                return ["H", "HIT!"]
        elif map[shot[0]][shot[1]] == "D":
            self.DestroyerHit -= 1
            if self.DestroyerHit == 0:
                return ["D", "You sunk the Destroyer!"]
            else:
                return ["H", "HIT!"]
        elif map[shot[0]][shot[1]] == "C":
            self.CarrierHit -= 1
            if self.CarrierHit == 0:
                return ["C", "You sunk the CARRIER!"]
            else:
                return ["H", "HIT!"]
        elif map[shot[0]][shot[1]] == "R":
            self.CruiserHit -= 1
            print("CruserHit")
            if self.CruiserHit == 0:
                return ["R", "You sunk the CRUISER!"]
            else:
                return ["H", "HIT!"]
        else:
            return ["Q", "Try again"]

    # --- Function definition for updateMap ---
    # Takes in the current map and the last shot results and returns an updated map.
    def updateMap(self,lastShotCell, lastShotResult, map):
        map[lastShotCell[0]][lastShotCell[1]] = lastShotResult
        return map

    # --- Function definition for checkShipStatus ---
    # Will check the ship layout to check which ships have been sunk.
    def checkShipStatus(self, shipList, shipMap) -> object:
        shipStatus = []
        ship = len(shipList)
        for index in range(ship):
            shipStatus.append(False)
        for index in range(ship):
            for list in shipMap:
                if shipList[index] in list:
                    shipStatus[index] = True
        return shipStatus


    def checkWin(self):
        # - Check the status of the ships to check win condition -
        self.shipsStillAlive = self.checkShipStatus(self.shipSymbols, self.shipMap)
        for index in range(len(self.shipsStillAlive)):
            if self.shipsStillAlive[index]:
                print("The " + self.shipNames[index] + " still sails!")
            else:
                print("You have sunk the " + self.shipNames[index] + "!")

        global currentMap
        # --- Update currentMap ---
        currentMap = self.updateMap(self.shotCoordinateList, self.shotResult[0], currentMap)

        # - Check win condition. If not ships remain end the game. ---
        if True not in self.shipsStillAlive:
            print("Good shooting! You have destroyed the enemy fleet!")
            return True
        else:
            return False

    # --- Game variables ---
    gridSize = 10
    validRows = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    validColumns = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    shipSymbols = ["B", "S", "D", "C", "R"]
    shipNames = ["BATTLESHIP", "SUBMARINE", "DESTROYER", "CARRIER", "CRUISER"]
    playing = True

    # ----------- Starting the Game. Code will need to loop until the user quits. -----------

"""while playing:
    # --- Initializing the ship locations ---
    fileName = "own_board.txt"           # file where the ship layout is kept
    accessMode = "r"                    # access mode w to write to the file
    shipMap = []


    try:
        with open(fileName, accessMode) as fileData:
            shipLocations = csv.reader(fileData)
            for row in shipLocations:
                shipMap.append(row)
    except FileNotFoundError:
        print("Sorry, there was an error loading a required file.")

    # --- Difficulty select. Loop created to ensure valid input entered. ---
    while True:
        missileCount = 100
        break


    # --- Variables to be set before each round ---
    currentMap = generateStartMap(gridSize)
    previousShots = []

    # ------ Starting the round. Code will need to loop until the user runs out of guesses or wins. ------
    while missileCount > 0:
        # --- Display currentMap to the user ---
        print("---------------------------")
        print("  " + " ".join(validColumns))
        for counter in range(gridSize):
            print(str(counter) + " " + " ".join(currentMap[counter]))
        print("---------------------------\n")
         #     "MISSILES REMAINING: " + str(missileCount))

        # --- Get location input from the user for their shot ---
        while True:
            #TODO: Change to take in server coords
            userShot = input("Enter the coordinates you wish to shoot: ").upper()
            if len(userShot) != 2:
                print("Please enter a valid coordinate:")
            elif userShot in previousShots:
                print("You've already shot there, pick a different coordinate.")
            elif userShot[0] not in validColumns or userShot[1] not in validRows:
                print("Please choose a coordinate in range.")
            else:
                previousShots.append(userShot)
                shotCoordinateList = shotToNumbers(userShot, validColumns)
                break

        print("---------------------------")

        # --- Check the shot vs. shipMap to verify a hit or miss ---
        shotResult = checkHit(shotCoordinateList, shipMap)
        print(shotResult[1])

        # --- Update the  game map to refer to when checking ship status ---
        shipMap = updateMap(shotCoordinateList, "X", shipMap)

        # - Check the status of the ships to check win condition -
        shipsStillAlive = checkShipStatus(shipSymbols, shipMap)
        for index in range(len(shipsStillAlive)):
            if shipsStillAlive[index]:
                print("The " + shipNames[index] + " still sails!")
            else:
                print("You have sunk the " + shipNames[index] + "!")

        # --- Update currentMap ---
        currentMap = updateMap(shotCoordinateList, shotResult[0], currentMap)

        # - Check win condition. If not ships remain end the game. ---
        if True not in shipsStillAlive:
            print("Good shooting! You have destroyed the enemy fleet!")
            break

        # - Check lose condition. Modify the missile count then check if the user has shots remaining. -
        missileCount -= 1
        if missileCount == 0:
            print("Looks like the enemy fleet has escaped the harbour! You had better get your crew in order Admiral!")
            playing = False



    # ----------- End of the Game. -----------
print("\nThanks for playing!")
"""