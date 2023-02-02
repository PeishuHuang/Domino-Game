#----------------------------------------------------
# Assignment 2: assignment2
# 
# Author: Peishu Huang 
# Collaborators/References: N/A
#----------------------------------------------------
# the code below is a domino game
# it can only choose the testmode now
# testmode will execute the test automatically
# the gamemode is under Construction
#----------------------------------------------------

from domino175 import Domino, DominoDeck, DominoStack

class Table():
    def __init__(self):
        self.__deck = DominoDeck()
        self.__grid = [[],[],[],[]]
        self.__playing_area = []
        # add Dominostack 3 times
        for i in range(3):
            self.__playing_area.append(DominoStack())
                
    def dealGrid(self, useFile):
        '''
        fills the deck with dominoes from a file (if useFile is True) or from a standard "double-six" set (if useFile is False)
        If the deck was filled successfully, dominoes are dealt from the deck and added face down to the grid
        '''
        # useFile will be passed into populate method
        self.__deck.populate(useFile)
        # if there is no exception, then there will have 28 dominoes
        # so we add them by order into the grid
        for row in range(4):
            for col in range(7):
                domino = self.__deck.deal()
                domino.turnOver()
                self.__grid[row].append(domino)
                
    def select(self,row,col):
        '''
         removes the domino at the specified row, column position from the grid and replaces it with the string ***
        '''
        assert 0 <= row <= 3 and 0 <= col <= 6, "Error: Invalid input"
        # that means, this position hasn't been choosen before
        if self.__grid[row][col] != ' *** ':
            domino = self.__grid[row][col]
            if domino.isFaceDown():
                domino.turnOver()
            self.__grid[row][col] = ' *** '  # replace the domino by ***
            return domino
        else:
            raise Exception("There is no domino at row %s, column %s"%(str(row),str(col)))
    
    def playDomino(self, domino, stackNum):
        '''
        add the provided domino to the top of the stack indicated by stackNum, and displays a message describing this action
        if successfully added, return True, else return False
        '''
        assert isinstance(domino,Domino), "Error: Invalid domino input"
        assert 0<= stackNum <= 2, "Error: Invalid stack number input"
        stack = self.__playing_area[stackNum]  # the index of the stack in playing area is its stack number
        try:
            stack.push(domino)
        except Exception:
            msg = "Play %s on stack %s: Cannot play %s on stack %s" % (str(domino),str(stackNum),str(domino),str(stackNum))
            print(msg)
            return False  # in this case, cannot add the domino onto the top of the stack
        else:
            msg = "Play %s on stack %s: Success!" % (str(domino),str(stackNum))
            print(msg)
            return True
        
    def isWinner(self):
        '''
        returns True if one of the stacks contains at least 6 dominoes, False otherwise
        '''
        for i in range(3):  # there are 3 stacks
            stack = self.__playing_area[i]  # the index of the stack in playing area is its stack number
            if stack.size() >= 6:  # if it is greater than or equal to 6
                return True
        return False  # in this case, every stacks are smaller than 6
    
    def getNumStacks(self):
        '''
        returns the integer number of stacks in the playing area. 
        '''
        return len(self.__playing_area)
    
    def getNumRows(self):
        '''
        returns the integer number of rows in the grid of dominoes
        '''
        return len(self.__grid)
    
    def getNumColumns(self):
        '''
        returns the integer number of columns in the grid of dominoes
        '''
        return len(self.__grid[0])
    
    def revealGrid(self):
        '''
        displays the face up version of all dominoes that are currently in the grid, for the player to see
        nothing is returned
        '''
        print(self.__gridstring(True))       
    
    def __gridstring(self, reveal):  # this is a private method
        '''
        this method will return a string representation of grid
        reveal is a boolean value, if it is True, than it will return face up domino grid
        else face down
        '''
        # total 63
        # 1(row index) + 3(space) + 5*7(domino) + 4*6(space)
        
        # the below is the first line        
        string = " "*6
        for i in range(7):
            string = string + str(i) + " "*8
        # the below is the grid part
        name = locals()  # I want to use this inside for loop
        for row in range(4):
            name["string" + str(row)] = str(row) + " "*3
            for col in range(7):
                domino = self.__grid[row][col]
                if reveal:
                    # this will show [num|num]
                    domino.turnOver()
                    name["string" + str(row)] = name["string" + str(row)] + str(domino) + " "*4
                    domino.turnOver()
                else:
                    # this will show [?|?]
                    name["string" + str(row)] = name["string" + str(row)] + str(domino) + " "*4
            string = string + "\n" + name["string" + str(row)]
        
        return string
    
    def __stackstring(self):  # this is a private method
        '''
        this method will return the string representation of stack in playing area
        '''
        string = "Domino Stacks:"
        for i in range(3):
            string = string + "\n" + str(i) + "|| " + str(self.__playing_area[i])
        return string

    def __str__(self):
        '''
        a string representation of the table
        '''
        string = "Selection Grid:\n"
        string = string + self.__gridstring(False) + "\n\n" + self.__stackstring() + "\n" + "-"*66
        return string

def testmode_grid(table):
    '''
    this funtion divides a big problem to a smaller problem
    it takes a Dominotable as argument
    and it will print the grids, which all dominoes are facing up
    '''
    print("")
    print("/"*65 + "\n" + "For testing purposes, the grid contains:")
    table.revealGrid()
    print("/"*65)
    print("")

def testmode(table):
    '''
    this funtion divides a big problem to a smaller problem
    it takes a Dominotable as argument
    it will execute the game automatically in order to test if every parts work well
    it will return a Boolean value
    '''
    name = locals()  # I want to use this inside for loop

    try:
        table.dealGrid(True)  # populate from text file
    except Exception:
        return False  # when there is exception, then there will have invalid data in file
    else:
        testmode_grid(table)  # show the grid with facing up dominoes
        for row in range(4):
            for col in range(7):
                print("\n" + str(table))  # show current grid
                domino = table.select(row,col)  # select the domino
                for stacknum in range(3):  # add it into 3 stacks one by one
                    if stacknum == 0:
                        name["success" + str(stacknum)] = table.playDomino(domino,stacknum)
                    else:
                        if name["success" + str(stacknum - 1)] == True:  # that means the domino has been added successfully
                            # so there is no need to add, just let it be true, like a "null" action
                            # and this will let the next adding be a "null" action, like an inductive way
                            name["success" + str(stacknum)] = True  
                        else:
                            # that means the domino hasn't been added successfully
                            name["success" + str(stacknum)] = table.playDomino(domino,stacknum)
                # this means that adding the domino to 3 stacks all fail.
                if ((name["success0"] or name["success1"]) or name["success2"]) == False:
                    print("GAME OVER. Better luck next time.")
                    return False
                # this is using to determine whether the one of the stacks is greater than or equal to 6
                if table.isWinner() == True:
                    print("Congratulations - WINNER!")
                    return False     

def decidemode():
    '''
    this funtion divides a big problem to a smaller problem
    it takes no argument
    it will keep asking the user to input a value untill the value is valid
    and it will return which mode the user chooses
    '''
    print("="*23)
    print("Welcome to DOMINOES 175")
    print("="*23)        
    mode = ""
    while mode not in ["1","2"]:  # this while loop will keep asking
        input_msg = "Please select your play mode:\n1. Test mode\n2. Game mode\n> "
        mode = input(input_msg)
        if mode not in ["1","2"]: 
            print("Invalid choice")
    return mode

def main():
    playing = True
    while playing:
        mode = decidemode()
        table = Table()
        if mode == "1":
            playing = testmode(table)  # the testmode will return a boolean value when the game finished          
        else:
            print("Under Construction")
            playing = False            
    print("Thank you for playing. Goodbye...")

main()