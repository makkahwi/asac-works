# Insert to Middle of an Array

To add a given number to a given array in middle index without using built-in methods.

## Whiteboard Process

 [Whiteboard](/Challenges/2/array-insert-shift.jpg)

## Approach & Efficiency

The approach was to first decide the middle position of the given array. Once that position is decided, a loop will go through the original array n push its elements to new array except at middle position where the given number will be pushed.
Big O:
Time: O(arr.length+1)
Space: O(1)
