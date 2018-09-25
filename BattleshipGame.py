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
    def __init__(self, fileName, fileName2):
        self.fileName = fileName
        self.fileName2 = fileName2

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

    def stringTo2D(self, string):
        temp = []
        twoD = []
        charList = string.split("\n")
        charList = charList[:10]
        for var in charList:
            temp = (var.split(","))
            temp = temp[:10]
            twoD.append(temp)
        return twoD


    def updateOwnBoard(self,result, x,y):
        x = int(x)
        y = int(y)
        tempString = ""
        if(self.fileName=="Aown_board.txt"):
            with open("Bown_board.txt", "r") as f:
                tempString = f.read()
        else:
            with open("Aown_board.txt", "r") as f:
                tempString = f.read()

        #with open(self.fileName,"r") as f:
        #    tempString = f.read()
        f.close()
        temp = []
        twoD = []
        charList = tempString.split("\n")
        charList = charList[:10]
        for var in charList:
            temp = (var.split(","))
            temp = temp[:10]
            twoD.append(temp)

        if(result == "X"):
            twoD[x][y] = result
        else:
            twoD[x][y] = "H"

        resultant = ""

        for var1 in twoD:
            for var2 in var1:
                resultant+=(var2+",")
            resultant+="\n"

        if (self.fileName == "Aown_board.txt"):
            with open("Bown_board.txt","w") as f:
                f.write(resultant)
            f.close()
        else:
            with open("Aown_board.txt","w") as f:
                f.write(resultant)
            f.close()



    #usershot is a string of two ints; IE; "12" or x=1, y=2
    def shoot(self, x, y):
        userShot = (str(x) + str(y))
        previousShots.append(userShot)
        self.shotCoordinateList = self.shotToNumbers(userShot, self.validColumns)

        # --- Check the shot vs. shipMap to verify a hit or miss ---
        self.shotResult = self.checkHit(self.shotCoordinateList, self.shipMap)
        print(self.shotResult[1])

        # --- Update the  game map to refer to when checking ship status ---
        self.shipMap = self.updateMap(self.shotCoordinateList, "X", self.shipMap)
        #TODO: Change to update opponent's board
        self.sneakyCheck(x,y)
        self.updateOwnBoard(self.shotResult[0],y,x)
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

        if map[shot[0]][shot[1]] == "0":
            return ["X", "Miss!"]
        elif map[shot[0]][shot[1]] == "B":
            self.BattleshipHit = self.BattleshipHit - 1
            if self.BattleshipHit == 0:
                return ["B", "You sunk the BATTLESHIP!"]
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

    def sneakyCheck(self, x, y):

        twoD = []
        if(self.fileName=="Aown_board.txt"):
            #do look at B
            tempfileName = "Bown_board.txt"
            file = open(tempfileName, "r")
            temp=""
            for line in file:
                temp += line
            twoD = self.stringTo2D(temp)
        else:
            #do look at A
            tempfileName = "Aown_board.txt"
            file = open(tempfileName, "r")
            temp =""

            for line in file:
                temp += line
            twoD = self.stringTo2D(temp)
        #Need shot and 2D array to use checkHit()

        shot = [x,y]
        personalFile = open(self.fileName2,"r")
        personalText = ""

        for line in personalFile:
            personalText += line
        #result
        #print(twoD)
        result = self.checkHit(shot,twoD)

        #convert personalText into 2D array
        #print(personalText)
        twoDResult = self.stringTo2D(personalText)
        #print(twoDResult)

        res = result[0]
        #print(res)
        twoDResult[y][x] = res

        resultant = ""

        for var1 in twoDResult:
            for var2 in var1:
                #print(var2)
                resultant += (var2 + ",")
            resultant += "\n"



        file2 = open(self.fileName2, "w")
        file2.write(resultant)

        file2.close()

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
