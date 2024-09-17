# Data Structures & Algorithms
Practice developing data structures for DSA.  
Primary resources and courses that inspired this repo are:  
https://frontendmasters.com/courses/algorithms/  
https://www.youtube.com/watch?v=8hly31xKli0&t=14621s

--------------------

### Doubly linked list using python
Depends on node class. Linked list methods include:

**Insertion**:
- `prepend_node` - add new head node
- `append_node` - add new tail node
- `insert_at_index` - insert node at indicated index

**Deletion**:
- `pop_left` - deletion of head node
- `pop_right` - deletion of tail node
- `delete_index` - deletion of node at indicated index

**QoL**:
- `display` - provides visual of linked list
- `length` - gives length of linked list
- `traverse` - allows for traversal and printout of nodes and their associated values and indices

--------------------

### Queue using python
Depends on node class. Queue methods include:

- `enqueue` - add new tail node to the queue
- `dequeue` - remove head node and return value
- `peek` - observe head node's value
- `display` - human-readable representation of the queue

--------------------

### Stack using python
Depends on node class. Stack methods include:

- `push` - add new head node
- `pop` - remove head node and return value
- `peek` - observe head node's value
- `display` - human-readable representation of the queue

--------------------

### Sort using python
Sort methods include:

- `bubble_sort` - performs bubble sort
- `selection_sort` - performs selection sort
- `quick_sort` - performs recursive quick sort
- `partition` - helper function for recursive quicksort
- `qs` - another helper function for recursive quicksort
- `simple_quicksort` - performs simplified quick sort
- `s_qs` - another helper function for a simplified quicksort
- `merge_sort` - performs merge sort
- `ms` - helper function for merge sort

--------------------

### Search using python
Depends on `simple_quicksort` function in Sorter class. Sort methods include:

- `linear_search` - performs linear search
- `binary_search` - performs binary search
