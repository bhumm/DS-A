from node import node

class Queue:
    '''
    Class to create a FIFO queue data structure
    
    Attributes
        head: head node
        tail: tail node
        length: length of queue
    '''
    
    def __init__(self):
        '''
        Constructor for the Queue class
        '''
        self.head = None
        self.tail = None
        self.length = 0
        
    def enqueue(self, data):
        '''
        Add another node to the queue
        
        Parameter
            data: value for queued node
        '''
        # Increment length
        self.length += 1
        # Instantiate new node
        new_node = node(data)
        
        # Set node as head and tail if no head exists (this queue is empty)
        if self.tail == None:
            self.tail = new_node
            self.head = new_node
        # Set new tail and create link with previous tail
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def dequeue(self):
        '''
        Remove the head node and return the value
        
        Returns
            dequeued head node value
        '''
        if self.length < 0:
            raise ValueError('No items in queue to dequeue')
        else:
            # Decrement length
            self.length -= 1
            
            dq_node = self.head
            #self.head.next.prev = None
            self.head = self.head.next
            
            # If last item in a queue set tail to None
            if dq_node == self.tail:
                self.tail = None
            
            return dq_node.data
            
    def peek(self):
        '''
        Peek at the head node value
        '''
        if self.head != None:
            return self.head.data
        
    def display(self):
        """
        Display the contents of the queue in a human-readable format.
        """
        current = self.head
        
        while current:  # Traverse each node in the list
            if current == self.head:
                print(current.data, end=" <-> ")
            elif current == self.tail:
                print(current.data)
            else:
                print(current.data, end=" <-> ")
            current = current.next