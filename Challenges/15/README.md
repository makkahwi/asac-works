# Trees

To build a tree Class & a node class that has properties for the value stored in the node, the left child node, and the right child node (two child node pointers). Binary search class is to have two methods, add new node and find a node by its value.

1[Whiteboard](./whiteboard.jpg)

## Approach & Efficiency

### Add Node

- Out of given value, create a binary node using BinaryNode class.
- Initiate root as tree root.
- Check if root is empty. If so, add create binary node as the root
- Go through the tree nodes using a loop. Based on the binary search tree rule (left is smaller, right is bigger), find the location of where the new node should be placed.
- If found location is empty, place new node there.
- Else if the new node value is smaller than found location’s value, place new node as left child. Else place new node as right child.

Big O
Time: O(n)
Space: O(n)

### Contains Node

- Check if the tree has a root. If not, return error msg.
- Go through the tree nodes using a loop. Based on the binary search tree rule (left is smaller, right is bigger), find the location of the required node value.
- Once it’s found return new. If not found, return a false.

Big O
Time: O(n)
Space: O(1)
