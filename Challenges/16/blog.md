# Blog

## Insertion Sort

Insertion Sort is a simple algorthim to sort an array (in this case ascendingly). Its approach is to go through the array items serveral times to compare items n build the sorted array.

## Approach

The approach is basically about using a loop to go through the array elements. First to check whether the element is an integer or not, then a nested loop would be engaged to check if previous elements are bigger or not. If so,the element will be switched with the bigger one (pushed back in array order).

## Pseudocode

 InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp

## Sorting Trace

Array: [20, 18, 12, 8, 5, -2]

- Step 1: Compare 18 & 20, n push 18 back to index 0.
  [18, 20, 12, 8, 5, -2]

- Step 2: Compare 12 & 20, n push 12 back to index 1.
  [18, 12, 20, 8, 5, -2]

- Step 3: Compare 18 & 12, n push 12 back to index 0.
  [12, 18, 20, 8, 5, -2]

- Step 4: Compare 20 & 8, n push 8 back to index 2.
  [12, 18, 8, 20, 5, -2]

- Step 5: Compare 118 & 8, n push 8 back to index 1.
  [12, 8, 18, 20, 5, -2]

- Step 6: Compare 12 & 8, n push 8 back to index 0.
  [8, 12, 18, 20, 5, -2]

- Step 7: Compare 20 & 5, n push 5 back to index 3.
  [8, 12, 18, 5, 20, -2]

- Step 8: Compare 18 & 5, n push 5 back to index 2.
  [8, 12, 5, 18, 20, -2]

- Step 9: Compare 12 & 5, n push 5 back to index 1.
  [8, 5, 12, 18, 20, -2]

- Step 10: Compare 8 & 5, n push 5 back to index 0.
  [5, 8, 12, 18, 20, -2]

- Step 11: Compare 20 & -2, n push -2 back to index 4.
  [5, 8, 12, 18, -2, 20]

- Step 12: Compare 18 & -2, n push -2 back to index 3.
  [5, 8, 12, -2, 18, 20]

- Step 13: Compare 23 & -2, n push -2 back to index 2.
  [5, 8, -2, 12, 18, 20]

- Step 14: Compare 8 & -2, n push -2 back to index 1.
  [5, -2, 8, 12, 18, 20]

- Step 15: Compare 5 & -2, n push -2 back to index 0.
  [-2, 5, 8, 12, 18, 20]

## Efficency

Big O:

- Time: O(n^2)
  Comparing work is a bit of an exponential time consumer as each item is compared to others more than once.
- Space: O(1)
  No space consumption. Same space occupied by given array is used without expansion.
