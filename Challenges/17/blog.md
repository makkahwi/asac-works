# Blog

## Merge Sort

Merge Sort is a divide and conquer algorithm. It's about splitting the array into nested halves, doing the comparison and rearrange work and then merge back the splits into 1 array..

## Pseudocode

 ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

## Sorting Trace

Array: [20, 18, 12, 8, 5, -2, 59, 91]

Step 1: Split given array into two halves.
      First half: [20, 18, 12, 8]
      Second half: [5, -2, 59, 91]

Step 2: Split first half array into two halves.
      First quarter: [20, 18]
      Second quarter: [12, 8]

Step 3: Split first quarter array into two halves.
      [20] & [18]

Step 4: Compare the splitted integers, sort them n merge them into 1 array.
      [18, 20]

Step 5: Split second quarter array into two halves.
      [12] & [8]

Step 6: Compare the splitted integers, sort them n merge them into 1 array.
      [8, 12]

Step 7: Compare the sorted first & second quarters, sort them n merge them into 1 array.
      Sorted First Half: [8, 12, 18, 20]

Step 8: Split second half array into two halves.
      Third quarter: [5, -2]
      Forth quarter: [59, 91]

Step 9: Split third quarter array into two halves.
      [5] & [-2]

Step 10: Compare the splitted integers, sort them n merge them into 1 array.
      [-2, 5]

Step 11: Split forth quarter array into two halves.
      [59] & [91]

Step 12: Compare the splitted integers, sort them n merge them into 1 array.
      [59, 91]

Step 13: Compare the sorted third & forth quarters, sort them n merge them into 1 array.
      Sorted Second Half: [-2, 5, 59, 91]

Step 14: Compare the sorted first & second halves, sort them n merge them into 1 array.
      [-2, 5, 8, 12, 18, 20, 59, 91]

## Efficency

Big O:

Time: O(n * log n): As a recursion algo.
Space: O(n): As new splitted arrays are created.
