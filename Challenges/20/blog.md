# Blog

## Quick Sort

Quick Sort is a divide and conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot.

## Pseudocode

ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp

## Sorting Trace

Content

## Approach

- Select any element in the list and call it pivot
- Partitioning the list (Partition is a proccess where we select the pivot and rearrange the list)
- Rearrange the list, in which all the elemnts less than the pivot are at the left and all the elements greater than the pivot are at the right of it
- There will be two sublists, reassign the pivot for each sublist
- Rearrange the two sublists, in which all the elemnts less than the pivot are at the left and all the elements greater than the pivot are at the right of it
- When we have only one element in the sublist
        - Stop the recursive call

## Efficency

Big O:

Time: O(n * log n): As a recursion algo.
Space: O(1): Same occupied space is used
