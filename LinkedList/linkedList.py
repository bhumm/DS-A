from node import node

class linkedList:
    '''
    A class for creating linked lists

    Attributes:
        head: first node in a linked list
        tail: last node in a linked list
    '''

    def __init__(self):
        '''
        Constructor for initializing a linked list
        '''
        self.head = None
        self.tail = None

    def prepend_node(self, data):
        '''
        Method to prepend a node to the beggining of linked list

        Parameters:
            data: data to store in the new head node
        '''
        new_node = node(data)
        
        # If no head, set as head
        if self.head == None:
            self.head = new_node
        # Set as new head and create link with previous head
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        
        # If no nodes set as tail
        if self.tail == None:
            self.tail = new_node

    def append_node(self, data):
        '''
        Method to append a node to the end of linked list

        Parameters:
            data: data to store in the new tail node
        '''
        new_node = node(data)
        
        # If no nodes, set as tail
        if self.tail == None:
            self.tail = new_node
        # Set as new tail and create link with previous tail
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        # If no nodes, set as tail
        if self.head == None:
            self.head = new_node

    def insert_at_index(self, data, index):
        '''
        Method to insert a node into a linked list at specified index

        Parameters:
            data: data to store in the new node
            index: index at which to insert new node
        '''
        if index < 0:
            raise ValueError('Index cannot be negative.')
        
        i = 0
        new_node = node(data)
        current_node = self.head
        
        # Traverse the list to find the node at the given index
        while current_node and i < index:
            current_node = current_node.next
            i += 1

        # If current_node is None, the index is out of bounds
        if current_node is None:
            raise ValueError('Index out of bound.')

        # Inserting the new node at the found position
        if current_node.prev != None:  # if there is a previous node
            current_node.prev.next = new_node
        new_node.prev = current_node.prev
        new_node.next = current_node
        current_node.prev = new_node

        # If we are inserting at the head of the list
        if index == 0:
            self.head = new_node

        # If current_node was the tail, update the tail reference
        if current_node.next is None:
            self.tail = current_node

    def pop_left(self):
        '''
        Method to delete the head node
        '''
        # If linked list is empty, raise error
        if self.head == None:
            raise ValueError("There is no value to pop.")
        
        # Set new head and delete head node
        else:
            current = self.head
            self.head = current.next
            current.next.prev = None
            del current
            
    def pop_right(self):
        '''
        Method to delete the tail node
        '''
        # If linked list is empty, raise error
        if self.tail == None:
            raise ValueError("There is no value to pop.")

        # Set upstream node as new tail and delete tail node
        else:
            current = self.tail
            self.tail = current.prev
            current.prev.next = None
            del current
    
    def del_index(self, index):
        '''
        Method to delete node at specified index

        Parameters:
            index: index at which to delete node
        '''

        # Error handling to ensure index was passed
        if index == None:
            raise ValueError("You must pass an index.")
        else:
            i = 0
            current_node = self.head

        # Traverse the list to find the node at the given index
        while current_node and i < index:
            current_node = current_node.next
            i += 1

        # If current_node is None, the index is out of bounds
        if current_node is None:
            raise ValueError('Index out of bound.')

        # Set upstream nodes next attribute as following node
        if current_node.prev != None:
            current_node.prev.next = current_node.next
        
        # Set downstream nodes prev attribute as preceding node
        if current_node.next != None:
            current_node.next.prev = current_node.prev

        # If deleting at the head of the list, set new head
        if index == 0:
            self.head = current_node.next

        # If deleting at tail of the list, set new tail
        if current_node.next is None:
            self.tail = current_node.prev

    def traverse(self):
        '''
        Method to traverse a list and print the index and corresponding node value
        '''
        current_node = self.head
        index = 0
        
        while current_node:
            
            print(index, ': ', current_node.data)
            current_node = current_node.next
            
            index += 1
            
            if current_node == self.tail:
                print(index, ': ', current_node.data)
                break

    def display(self):
        '''
        Visual method of displaying the linked list
        '''
        current = self.head
        
        while current:
            if current == self.head:
                print(current.data, end = " <-> ")
                current = current.next
            elif current == self.tail:
                print(current.data)
                current = current.next
            else:
                print(current.data, end = " <-> ")
                current = current.next

    def length(self):
        '''
        Reports the length of the linked list
        '''
        i = 0
        if self.head != None:
            current_node = self.head
            
            while current_node:
                current_node = current_node.next
                i += 1

        return i