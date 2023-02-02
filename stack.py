#--------------------------------------------------------------------
# Stack implementation #2 
# (Top of stack corresponds to back of list)
# 
# Author: CMPUT 175 team
# References: CMPUT 175 lecture slides (Stacks), except for __str__
#--------------------------------------------------------------------

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1] 
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def show(self):
        print(self.items)
    
    def __str__(self):
        stackAsString = 'bottom -> '
        for item in self.items:
            stackAsString += item + ' '
        stackAsString += '<- top'
        return stackAsString
 