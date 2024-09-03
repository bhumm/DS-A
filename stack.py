from node import node

class Stack:
    '''
    Class for a stack data structure
    
    Attributes
        head: head node
        lenght: length of queue
    '''

    def __init__(self):
        '''
        Constructor for the stack class
        '''
        self.head = None
        self.length = 0

    def push(self, data):
        '''
        Push a new node head
        
        Parameters
            data: new node value
        '''
        new_node = node(data)
        # If there is no head node
        if self.head == None:
            self.length += 1
            self.head = new_node
        # Set new head and link with previous head, increment length
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
    
    def pop(self):
        '''
        Pop head from stack and return value
        '''
        # Error is empty stack
        if self.head == None:
            raise ValueError("No nodes in which to pop.")
        # Remove and return head node and set new head node
        else:
            # Decrement length
            self.length -= 1
            pop_node = self.head
            self.head = self.head.next
            self.head.prev = None
            # Return the value
            return pop_node.data

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
                print(current.data, end="")
            else:
                print(" <-> ", current.data, end="")
            current = current.next