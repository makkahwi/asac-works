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

Array: [8, 4, 23, 42, 16, 15]

Step 1: Check if given left is smaller than given right

Step 2: If so, partition the array by setting the position of the pivot value as follows...
    Step 2-1: set 15 as pivot value
    Step 2-2: less than 15 values are [8, 4] & larger than 15 vales are [23, 42, 16]

Step 3: Partition the subarray of [8, 4] as follows...
    Step 3-1: set 4 as pivot value
    Step 3-2: less than 4 values are [] & larger than 4 vales are [8]

Step 4: Partition the subarray of [23, 42, 16] as follows...
    Step 4-1: set 16 as pivot value
    Step 4-2: less than 16 values are [] & larger than 16 vales are [23, 42]

Step 5: Partition the subarray of [23, 42] as follows...
    Step 5-1: set 42 as pivot value
    Step 5-2: less than 42 values are [23] & larger than 42 vales are []

Step 6: Put togather the sorted array [4, 8, 15, 16, 23, 42]

## Approach

- Set any element of the list as the referance point (pivot).
- Partition the list based on selected pivot.
- Reorder the list so elements smaller than pivot are first, then pivot value comes in the middle, then elements bigger than pivot follow at last.
- Using recusirion, do the partitioning & reorder work for both subarrays (smaller than & bigger than pivot arrays)

## Efficency

Big O:

Time: O(n * log n): As a recursion algo.
Space: O(1): Same occupied space is used
