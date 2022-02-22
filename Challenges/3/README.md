# Binary Search of Sorted Array

To find the index of given key in a given array.

## Whiteboard Process

 [Whiteboard](/Challenges/3/array-binary-search.jpg)

## Approach & Efficiency

The approach was to set a default start, middle n end point for the search process, n then go into a loop to start looking for the given key. If the given key is in the middle, middle point will be return as an answer. If middle point is bigger than given key, the middle n end points will be changed to look into the first half only of the previous search range, else if middle is smaller, the start n middle points will be updated so that the search range will cover the second half only of the previous search range.

Big O:
Time: O(arr.length /4)
Space: O(1)
