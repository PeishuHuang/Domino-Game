#----------------------------------------------------
# Assignment 2: domino175
# 
# Author: Peishu Huang 
# Collaborators/References: N/A
#----------------------------------------------------
# the code below is a module for assignment2
# it contains class Domino, DominoDeck
# and DominoStack
#----------------------------------------------------

from queues import CircularQueue
from stack import Stack
import random

class Domino:
    '''
    this is a class of Domino
    '''
    def __init__(self,dotsA,dotsB):
        assert isinstance(dotsA,int) and isinstance(dotsB,int), ("Error: Invalid input")
        # the below statement will kepp the bigger dots be top always
        if dotsA >= dotsB:
            self.__top = dotsA  
            self.__bottom = dotsB
        else:
            self.__top = dotsB  
            self.__bottom = dotsA            
        self.__faceDown = False
        
    def setTop(self,dots):
        assert dots in [self.__top,self.__bottom], "Error: No such dots existing"

        # the below statements execute when there is a need to exchange the top and bottom
        if self.__top != dots:
            self.__bottom = self.__top
            self.__top = dots
        # else there is no need to exchange the top and bottom
    
    def turnOver(self):
        '''updates the Domino instance so that if it was facing up, it will now be facing downSimilarly, if it was facing down, it will now be facing up. Nothing is returned. '''
        self.__faceDown = not self.__faceDown
    
    def getTop(self):
        ''' returns the integer number of dots on the top end of the Domino instance. '''
        return self.__top
    
    def getBottom(self):
        ''' returns the integer number of dots on the bottom end of the Domino instance. '''
        return self.__bottom
        
    def isFaceDown(self):
        ''' returns the Boolean value indicating whether the Domino instance is facing down 
    (True) or up (False). '''
        return self.__faceDown == True
        
    def __str__(self):
        '''' returns the string representation of the Domino instance. The format of this string 
    should be '[bottom number of dots|top number of dots]' if it is facing up. Any domino that is facing down 
    will have question marks, '?' '''
        if self.__faceDown:
            return "[?|?]"
        else:
            return "[%s|%s]" % (str(self.__bottom),str(self.__top))

class DominoDeck:
    '''
    this is a class of DominoDeck
    '''
    def __init__(self):
        self.__deck = CircularQueue(28)
    
    def __populate_from_file(self):  
        # this is a private method, it will read domino data from file
        # the below will ask user to input a valid filename
        openfile = False
        while not openfile:
            filename = input("Name of file that should be used to populate the grid of dominoes: ")
            try:
                file = open(filename, "r")
                openfile = True
            except Exception:
                print("Invalid input")
        
        # the below will read file content
        content = file.readlines()            
        file.close()          
        # if the size is not 28, then it is not valid
        if len(content) != 28:
            print("Cannot populate deck: invalid data in %s" % (filename))
            raise Exception("Cannot populate deck: invalid data in %s" % (filename))
        
        for domino in content:
            split_index = domino.index("/")
            # if the data is not valid, int1 and int2 will raise the exception
            try:
                integer1 = int(domino[split_index-1])
                integer2 = int(domino[split_index+1])                
                self.__deck.enqueue(Domino(integer1,integer2))
            except Exception:  
                self.__deck.clear()
                print("Cannot populate deck: invalid data in %s" % (filename))
                raise Exception("Cannot populate deck: invalid data in %s" % (filename))                

    def populate(self,useFile):
        '''
        adding new dominoes face up to the rear of the deck. Nothing is returned.
        if useFile is True, then it will ask the user to input a file name
        if useFile is False, then it will generate a Dominoes set
        '''
        assert isinstance(useFile,bool), "Cannot populate deck: invalid argument provided."
        
        if useFile:
            self.__populate_from_file() 
        else:
            # it will generate a completed dominoes set
            temp_list = []
            for i in range(7):
                for j in range(i+1):
                    a_domino = Domino(i,j)
                    temp_list.append(a_domino)
            # it will shuffle them randomly, and add it into the deck
            random.shuffle(temp_list)
            for domino in temp_list:
                self.__deck.enqueue(domino)
    
    def deal(self):
        '''
        removing the domino from the front of the deck, and returns that front domino, face down.
        '''
        if self.__deck.isEmpty():
            raise Exception('Cannot deal domino from empty deck')
        else:
            front_domino = self.__deck.dequeue()
            if front_domino.isFaceDown():
                front_domino.turnOver()
                return front_domino
            else:
                return front_domino
    
    def isEmpty(self):
        '''
        returns a Boolean value indicating whether there are no dominoes in the deck (True) or 
        if there is at least one domino in the deck (False). 
        '''
        return self.__deck.isEmpty()
    
    def size(self):
        '''
        return the integer numbers of dominoes on current deck
        '''
        return self.__deck.size()
    
    def __str__(self):
        '''
        a string representation of all dominoes on the deck
        '''
        string = "Frontmost ->" + str(self.__deck)[1:-2] + "<- Rearmost"
        return string      
    
class DominoStack:
    '''
    a class of DominoStack
    '''
    def __init__(self):
        self.__stack = Stack()
    
    def peek(self):
        '''
        returns the number of dots on the top of the Domino that is at the top of the stack. 
        '''
        # if the stack does not contain any dominoes. 
        if self.__stack.isEmpty():
            raise Exception("Error: cannot peek into an empty stack")
        # else it will use the peek method from Stack
        else:
            top_domino = self.__stack.peek()
            return top_domino.getTop()
    
    def isEmpty(self):
        '''returns a Boolean value indicating whether there are no dominoes on the stack (True) or 
        if there is at least one domino on the stack (False). 
        '''
        return self.__stack.isEmpty()
    
    def size(self):
        '''
        return the integer numbers of dominoes in current stack
        '''        
        return self.__stack.size()
    
    def push(self,domino):
        '''
        adds the provided domino onto the top of the sel.__stack if it is empty, 
        or if the number of dots on the top of the Domino currently on the top of the stack matches the 
        number of dots on one side of the provided domino. 
        '''
        assert isinstance(domino,Domino), "Can only push Dominoes onto the DominoStack"
        # when the stack is empty
        if self.__stack.isEmpty():
            self.__stack.push(domino)
        # when the stack is not empty
        else:
            current_domino = self.__stack.peek()
            # if the top dots of top domino is equal to the bottom side's dots of the given domino
            if current_domino.getTop() == domino.getBottom(): 
                self.__stack.push(domino)
            # if the top dots of top domino is equal to the top side's dots of the given domino
            elif current_domino.getTop() == domino.getTop():
                domino.setTop(domino.getBottom())
                self.__stack.push(domino)
            # else, it will show that this domino cannot be added into the stack
            else:
                if domino.isFaceDown():
                    domino.turnOver()
                raise Exception("Cannot play %s on stack" % (str(domino)))    
    
    def __str__(self):
        '''
        return a string representation of the domino in stack
        '''
        string = ""
        for item in self.__stack.items:
            string = string + str(item) + "-"
        return string[0:-1]  # it will omit the last dashline

def test():
    '''
    test use only
    '''
    #try:
        #Domino("a",1)
        #is_pass = False
    #except Exception:
        #is_pass = True
    #assert is_pass == True, ("Fail the Invalid input check")
    
    # the below is the check for class Domino
    a_domino = Domino(3,4)
    
    is_pass = (a_domino.getBottom() == 3)
    assert is_pass == True, ("Fail the getBottom() check")
    
    is_pass = (a_domino.getTop() == 4)
    assert is_pass == True, ("Fail the getTop() check")
    
    a_domino.setTop(3)
    
    is_pass = (a_domino.getTop() == 3)
    assert is_pass == True, ("Fail the setTop() check")
    
    is_pass = (a_domino.getBottom() == 4)
    assert is_pass == True, ("Fail the setTop() check")    
    
    is_pass = (str(a_domino) == "[4|3]")
    assert is_pass == True, ("Fail the __str__() check")   
    
    is_pass = (a_domino.isFaceDown() == False)
    assert is_pass == True, ("Fail the isFaceDown() check") 
    
    a_domino.turnOver()
    
    is_pass = (a_domino.isFaceDown() == True)
    assert is_pass == True, ("Fail the turnOver() check") 
    
    is_pass = (str(a_domino) == "[?|?]")
    assert is_pass == True, ("Fail the __str__() check") 
    
    # the below is the check for DominoDeck
    deck = DominoDeck()
    
    is_pass = (deck.isEmpty() == True)
    assert is_pass == True, ("Fail the isEmpty() check")
    
    try:
        is_pass = False
        deck.deal()
    except Exception:
        is_pass = True
    assert is_pass == True, ("Fail the deal() check")
    
    deck.populate(False)
    
    is_pass = (deck.size() == 28)
    assert is_pass == True, ("Fail the size() check")
    
    # the below is the check for Dominostack
    a_stack = DominoStack()
    
    is_pass = (a_stack.isEmpty() == True)
    assert is_pass == True, ("Fail the isEmpty() check")
    
    try:
        is_pass = False
        a_stack.peek()
    except Exception:
        is_pass = True
    assert is_pass == True, ("Fail the peek() check")
    
    a_stack.push(Domino(3,4))
    
    is_pass = (a_stack.size() == 1)
    assert is_pass == True, ("Fail the size() check")
    
    try:
        is_pass = False
        a_stack.push(Domino(1,2))
    except Exception:
        is_pass = True
    assert is_pass == True, ("Fail the push() check")
    
    a_stack.push(Domino(1,4))
    is_pass = (a_stack.size() == 2)
    assert is_pass == True, ("Fail the push() check")
    
    is_pass = (str(a_stack) == "[3|4]-[4|1]")
    assert is_pass == True, ("Fail the __str__() check")
    
    if is_pass:
        print("All things seem good")
    
    print("The below is the test of str(DominoDeck)")
    print(str(deck))

    
if __name__ == "__main__":    
    test()
