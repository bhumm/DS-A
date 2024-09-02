class node:
    '''
    A class for nodes in a doubly linked list

    Attributes:
        data: data to be stored in a node
        next: the next node in a linked list
        prev: the previous node in a linked list
    '''
    def __init__(self, data):
        '''
        Constructor to initialize a node
        
        Parameters:
            data: data in a node
        '''
        self.data = data
        self.next = None
        self.prev = None