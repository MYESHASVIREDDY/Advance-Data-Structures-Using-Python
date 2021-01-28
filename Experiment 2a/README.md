# EXPERIMENT 2A
### Aim of the experiment: To execute a program that uses functions to perform merge sort
### PROCEDURE
Create a function merge_sort that takes a list and two variables start and end as arguments.
 The function merge_sort will sort the list from indexes start to end – 1 inclusive.
 If end – start is not greater than 1, then return.
 Otherwise, set mid equal to the floor of (start + end)/2.
 Call merge_sort with the same list and with start = start and end = mid as arguments.
 Call merge_sort with the same list and with start = mid and end = end as arguments.
Call the function merge_list, passing the list and the variables start, mid and end as arguments.
 The function merge_list takes a list and three numbers, start, mid and end as arguments and assuming the list is sorted from indexes start to mid – 1 and from mid to end – 1, merges them to create a new sorted list from indexes start to end – 1.
