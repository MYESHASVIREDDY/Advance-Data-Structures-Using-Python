# EXPERIMENT 2B
## Aim of the experiment: To execute a program that uses functions to perform heap sort
### PROCEDURE:
Basically, there are two phases involved in the sorting of elements using heap sort algorithm they are as follows:
First, start with the construction of a heap by adjusting the array elements.
Once the heap is created repeatedly eliminate the root element of the heap by shifting it to the end of the array and then store the heap structure with remaining elements.
To begin with, a heap is built by moving the elements to its proper position within the array. This means that as the elements are traversed from the array the root, its left child, its right child are filled in respectively forming a binary tree.
In the second phase, the root element is eliminated from the heap by moving it to the end of the array.
The balance elements may not be a heap. So again steps 1 and 2 are repeated for the balance elements. The procedure is continued until all the elements are eliminated.
When eliminating an element from the heap we need to decrement the maximum index value of the array by one. The elements are eliminated in decreasing order for a max-heap and in increasing order for min-heap.
