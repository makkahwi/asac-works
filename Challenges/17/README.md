# Merge Sort

Convert a Pseudocode-based function to Python-based. The function is about ascending sorting an array of integers but using the merge apprach. Which is about splitting the array into nested halfs n compare elements between the splits before merging them back.

## Whiteboard Process

![WhiteBoard](./whiteboard.jpg)

## Approach & Efficiency

The approach is basically about using a loop to go through the array elements. First to check whether the element is an integer or not, then a nested loop would be engaged to check if previous elements are bigger or not. If so,the element will be switched with the bigger one (pushed back in array order).

Big O:
Time: O(n^2)
Space: O(n)
