class Sorter:
    '''
    A class that provides various sorting algorithms for a dataset.

    Attributes:
    - data (list): The dataset to be sorted.
    '''

    def __init__(self, data):
        '''
        Initializes the Sorter with a dataset.

        Parameters:
        - data (list): A list of elements to be sorted.
        '''
        self.data = data

    def bubble_sort(self):
        '''
        Performs a bubble sort on the dataset.

        This method sorts the dataset in ascending order using the bubble sort 
        algorithm, which repeatedly steps through the list, compares adjacent 
        elements, and swaps them if they are in the wrong order. 
        '''
        arr_len = len(self.data)

        # Iterate over each element in the data list
        for i in range(arr_len):
            swapped = False  # Flag to check if any swapping occurred

            # Last i elements are already in place
            for j in range(0, arr_len - 1 - i):
                # Swap if the current element is greater than the next
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    swapped = True

            # If no elements were swapped, the list is sorted
            if not swapped:
                break

    def selection_sort(self):
        '''
        Performs a selection sort on the dataset.

        This method sorts the dataset in ascending order using the selection sort 
        algorithm, which repeatedly selects the smallest element from the unsorted 
        part of the list and appends it to a new sorted list.
        '''
        unsorted = self.data
        sorted_list = []

        # Iterate until the unsorted list is empty
        while unsorted:
            min_index = 0
            # Find the index of the minimum element
            for i in range(1, len(unsorted)):
                if unsorted[i] < unsorted[min_index]:
                    min_index = i
            # Remove the smallest element and append to sorted_list
            sorted_list.append(unsorted.pop(min_index))

        self.data = sorted_list

    def partition(self, arr, low, hi):
        '''
        Helper method for quick_sort. Partitions the array for quicksort.

        This method selects the last element as a pivot and partitions the given 
        array such that elements smaller than the pivot are on the left and elements 
        greater than the pivot are on the right.

        Parameters:
        - arr (list): The array to partition.
        - low (int): The starting index of the segment to partition.
        - hi (int): The ending index of the segment to partition.

        Returns:
        - int: The index of the pivot element after partitioning.
        '''
        pivot = arr[hi]  # Choose the pivot as the last element
        index = low - 1  # Pointer for the smaller element

        # Iterate through the array to partition it
        for i in range(low, hi):
            if arr[i] <= pivot:
                index += 1
                # Swap elements
                arr[index], arr[i] = arr[i], arr[index]

        # Swap the pivot element with the element at index + 1
        arr[index + 1], arr[hi] = arr[hi], arr[index + 1]
        return index + 1

    def qs(self, arr, low, hi):
        '''
        Helper method for quick_sort. Implements the quicksort algorithm.

        This method recursively sorts the elements before and after the pivot 
        obtained from the partition method.

        Parameters:
        - arr (list): The array to be sorted.
        - low (int): The starting index of the segment to sort.
        - hi (int): The ending index of the segment to sort.
        '''
        if low < hi:
            # Partition the array
            pivot_index = self.partition(arr, low, hi)
            # Recursively sort elements before and after partition
            self.qs(arr, low, pivot_index - 1)
            self.qs(arr, pivot_index + 1, hi)

    def quick_sort(self):
        '''
        Performs a quicksort on the dataset.

        This method sorts the dataset in ascending order using the quicksort 
        algorithm. It uses the `qs` method to sort the dataset.
        '''
        arr = self.data
        self.qs(arr, 0, len(arr) - 1)

    def s_qs(self, arr):
        '''
        Simplified version of quicksort.

        Parameters:
        - arr (list): The array to be sorted.

        Returns:
        - list: The sorted array.
        '''
        if len(arr) <= 1:
            return arr
        less_than_pivot = []
        greater_than_pivot = []
        pivot = arr[0]

        # Partition elements into less_than_pivot and greater_than_pivot lists
        for i in arr[1:]:
            if i < pivot:
                less_than_pivot.append(i)
            else:
                greater_than_pivot.append(i)

        # Recursively sort partitions and combine
        return self.s_qs(less_than_pivot) + [pivot] + self.s_qs(greater_than_pivot)

    def simple_quicksort(self):
        '''
        Sorts the dataset using the simplified quicksort method.
        '''
        self.data = self.s_qs(self.data)

    def ms(self, arr):
        '''
        Helper method for merge_sort. Implements the merge sort algorithm.

        This method sorts the array by recursively dividing it into halves and merging 
        the sorted halves.

        Parameters:
        - arr (list): The array to be sorted.

        Returns:
        - list: The sorted array.
        '''
        if len(arr) <= 1:
            return arr

        middle_index = len(arr) // 2
        left_half = arr[:middle_index]
        right_half = arr[middle_index:]

        # Recursively split and merge
        self.ms(left_half)
        self.ms(right_half)

        i = 0  # Left half index
        j = 0  # Right half index
        n = 0  # Merged array index

        # Merge the halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[n] = left_half[i]
                i += 1
            else:
                arr[n] = right_half[j]
                j += 1
            n += 1

        # Copy remaining elements of left_half, if any
        while i < len(left_half):
            arr[n] = left_half[i]
            i += 1
            n += 1

        # Copy remaining elements of right_half, if any
        while j < len(right_half):
            arr[n] = right_half[j]
            j += 1
            n += 1

        return arr

    def merge_sort(self):
        '''
        Performs a merge sort on the dataset.

        This method sorts the dataset in ascending order using the merge sort algorithm.
        '''
        self.data = self.ms(self.data)
