import Sort.Sorter

class Searcher:
    '''
    The `Searcher` class includes both linear and binary search methods to find
    elements within a dataset.

    Attributes:
    - data (list): The dataset in which to perform searches.
    '''

    def __init__(self, data):
        '''
        Initializes the Searcher with a dataset.

        Parameters:
        - data (list): A list of elements to be searched.
        '''
        self.data = data

    def linear_search(self, target):
        '''
        Performs a linear search on the dataset.

        Parameters:
        - target: The element to search for in the dataset.

        Returns:
        - int: The index of the target if found.
        - None: If the target is not in the dataset.
        '''

        # Iterate over each element in the data list
        for index in range(0, len(self.data)):
            # Check if the current element is equal to the target
            if self.data[index] == target:
                return index
        # Return None if the target is not found
        return None

    def binary_search(self, target):
        '''
        Performs a binary search on the dataset.

        This method sorts the dataset using quicksort before performing the binary search.
        It returns the index of the target element if found. If the target is not found,
        it returns `None`.

        Parameters:
        - target: The element to search for in the dataset.

        Returns:
        - int: The index of the target if found.
        - None: If the target is not in the dataset.
        '''

        # Create a new Searcher instance to sort the data
        s = Searcher(self.data)
        s.simple_quicksort()  # Sort the data using quicksort
        data = s.data  # Get the sorted data

        # Initialize the start and end points for the search
        first = 0
        last = len(data) - 1

        # Perform binary search
        while first <= last:
            # Find the midpoint
            midpoint = (first + last) // 2
            # Check if the midpoint element is the target
            if data[midpoint] == target:
                return midpoint
            # If target is greater, ignore the left half
            elif data[midpoint] < target:
                first = midpoint + 1
            # If target is smaller, ignore the right half
            else:
                last = midpoint - 1

        # Return None if the target is not found
        return None
