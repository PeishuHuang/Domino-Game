class BoundedQueue: 
    def __init__(self, capacity): 
        '''
        Constructor, which creates a new empty queue
        '''        
        assert isinstance(capacity, int), ('Error: Type error: {}'.format(type(capacity)))
        assert capacity >= 0, ('Error: Illegal capacity: {}'.format(capacity))
        self.__items = []
        self.__capacity = capacity
 
    
    def enqueue(self, item): 
        ''' 
        Adds a new item to the back of the queue, and returns nothing
        '''
        if len(self.__items) >= self.__capacity:     
            raise Exception('Error: Queue is full')       
        self.__items.append(item)
        
  
    def dequeue(self):
        '''
        Removes and returns the front-most item in the queue.      
        Returns nothing if the queue is empty.  
        '''
        if len(self.__items) <= 0:            
            raise Exception('Error: Queue is empty')                
        return self.__items.pop(0)            
    
          
    def peek(self):   
        '''
        Returns the front-most item in the queue, and DOES NOT change the queue.
        '''
        if len(self.__items) <= 0:            
            raise Exception('Error: Queue is empty')        
        return self.__items[0]
        
      
    def isEmpty(self):
        '''
        Returns True if the queue is empty, and False otherwise.  
        '''
        return len(self.__items) == 0        
    
        
    def isFull(self):  
        '''
        Returns True if the queue is full, and False otherwise.
        '''
        return len(self.__items) == self.__capacity
    
        
    def size(self):   
        '''
        Returns the number of items in the queue
        '''
        return len(self.__items)        
    
       
    def capacity(self):
        '''
        # Returns the capacity of the queue.
        '''
        return self.__capacity
    
  
    def clear(self):
        '''
        Removes all items from the queue, and sets the size to 0.    
        clear() should not change the capacity.
        '''
        self.__items = []

    
    def __str__(self):   
        '''
        Returns a string representation of the queue. 
        '''
        str_exp = ""        
        for item in self.__items:            
            str_exp += (str(item) + " ")                    
        return str_exp
        
    
    def __repr__(self):    
        '''
        Returns a formal string representation of the object BoundedQueue.
        '''
        return  str(self) + " Max=" + str(self.__capacity)      



class CircularQueue:
    def __init__(self, capacity): 
        '''
        Constructor, which creates a new empty queue.
        '''
        # Check validity of capacity type and value
        if type(capacity) != int or capacity<=0:
            raise Exception('Capacity Error')                
        
        # Initialize private attributes
        self.__items = []
        self.__capacity = capacity
        self.__count=0
        self.__head=0
        self.__tail=0
    
       
    def enqueue(self, item): 
        '''
        Adds a new item to the back of the queue, and returns nothing.
        '''
        if self.__count == self.__capacity:     
            raise Exception('Error: Queue is full')       
        
        if len(self.__items) < self.__capacity:
            self.__items.append(item)
        else:
            self.__items[self.__tail] = item
            
        self.__count +=1
        self.__tail=(self.__tail +1) % self.__capacity
        
       
    def dequeue(self):
        '''
        Removes and returns the front-most item in the queue.      
        Returns nothing if the queue is empty. 
        '''
        if self.__count == 0:            
            raise Exception('Error: Queue is empty') 
        
        item = self.__items[self.__head]     # get item at head of queue
        self.__items[self.__head] = None     # remove item from head of queue
        self.__count -= 1                    # decrease stored size of queue
        self.__head = (self.__head+1) % self.__capacity  # shift head of queue right             
        return item            
    
         
    def peek(self): 
        '''
        Returns the front-most item in the queue, and DOES NOT change the queue. 
        '''
        if self.__count == 0:            
            raise Exception('Error: Queue is empty')        
        
        return self.__items[self.__head]
    
       
    def isEmpty(self):
        '''
        Returns True if the queue is empty, and False otherwise. 
        '''
        return self.__count == 0        
    
        
    def isFull(self):   
        '''
        Returns True if the queue is full, and False otherwise.
        '''
        return self.__count == self.__capacity
    
        
    def size(self):    
        '''
        Returns the number of items in the queue.
        '''
        return self.__count        
    
       
    def capacity(self): 
        '''
        Returns the capacity of the queue. 
        '''
        return self.__capacity
    
       
    def clear(self):
        '''
        Removes all items from the queue, and sets the size to 0.    
        clear() should not change the capacity. 
        '''
        self.__items = []
        self.__count = 0
        self.__head = 0
        self.__tail = 0
    
    
    def __str__(self):
        '''
        Returns a string representation of the queue. 
        '''
        str_exp = "]"        
        i = self.__head
        for j in range(self.__count):            
            str_exp += str(self.__items[i]) + " "
            i = (i+1) % self.__capacity
        return str_exp + "]"
        
       
    def __repr__(self):  
        '''
        Returns a formal string representation of the object CircularQueue 
        '''
        return str(self.__items) + " H= " + str(self.__head) + " T="+str(self.__tail) + " (" +str(self.__count)+"/"+str(self.__capacity)+")"  
 
 
 
    
def main():
    # Test bounded queue constructor

    bq=BoundedQueue(3)
    print("My bounded queue is:", bq)
    print(repr(bq))
    print("Is my bounded queue empty?", bq.isEmpty())
    print('----------------------------------')
    
    '''
    # 1. To Do: complete Test 1 according to lab description
    # Test when we try to dequeue from an EMPTY queue
    try:
        ## To Do: Write your own test

    except Exception as dequeueError:
        ## To Do: Write a way to handle it

    print('----------------------------------')
    '''
    try:
        bq.dequeue()
    except Exception:
        print("Error: Queue is empty")
    print('----------------------------------')     
    
    '''
    # 2. To Do: complete Test 2 according to lab description
    # Test adding one element to queue
    
    ## Your test code goes here...
    
    print(bq)
    print(str(bq))
    print("Is my bounded queue empty?", bq.isEmpty())    
    print('----------------------------------')
    '''
    bq.enqueue("bob")
    print(bq)   
    print(str(bq))
    print("Is my bounded queue empty?", bq.isEmpty())    
    print('----------------------------------')
    

    bq.enqueue("eva")
    bq.enqueue("paul")
    print(repr(bq))
    print("Is my bounded queue full?", bq.isFull())
    print("There are", bq.size(), "elements in my bounded queue.")
    print('----------------------------------')

 
    '''
    # 4. To Do: complete Test 4 according to lab description
    # Test trying to add an element to a FULL queue
    
    ## Your test code goes here...hint: look at dequeuing from EMPTY queue
        
    print('----------------------------------')
    '''
    try:
        bq.enqueue("Bob")
    except Exception:
        print("Try to enqueue a full bounded queue...")
        print("Error: Queue is full")
    print('----------------------------------')      
    
    '''
    # 5. Uncomment and run Test 5
    # Test removing element from full queue
    item = bq.dequeue()
    print(repr(bq))
    print(item,"was first in the bounded queue:", bq)
    print("There are", bq.size(), "elements in my bounded queue.")
    print('----------------------------------')
    '''
    item = bq.dequeue()
    print(repr(bq))
    print(item,"was first in the bounded queue:", bq)
    print("There are", bq.size(), "elements in my bounded queue.")
    print('----------------------------------')    
    
    '''
    # 6. Uncomment and run Test 6
    # Test capacity of queue
    print("Total capacity is:", bq.capacity())
    '''
    print("Total capacity is:", bq.capacity())
    
    '''
    # 7. To Do: Uncomment print statements, one at a time
    # Can we just access private capacity attribute directly outside of Class definition?
    #print(bq.capacity)
    #print(bq.__capacity)
    '''
    print(bq.capacity)
    
    
if __name__ == '__main__':
   main()


