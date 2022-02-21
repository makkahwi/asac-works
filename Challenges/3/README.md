# Binary Search of Sorted Array

To find the index of given key in array.

## Whiteboard Process

 [Whiteboard](/Challenges/3/array-binary-search.jpg)

## Approach & Efficiency

The approach was simply to go through the elemnts of given array one-by-one n check weather the element equals to given key. If yes it would return the index n break the loop, if not, it would check if current element is bigger thatn key and if so the loop would break. Otherwise loop would keep going through elements of given array.

Big O:
Time: O(arr.length)
Space: O(1)
