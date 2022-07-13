# Tree Breadth First

To build a list function for trees. Listing is to be based on breadth-first concept.

![Whiteboard](./whiteboard.jpg)

## Approach & Efficiency

- Check if the tree has a root. If not, return error msg.
- Initiate a Queue and enqueue tree root.
- Using a loop, enqueue both children (if they exist) of the front of the queue, then dequeue it and append the dequeued value to the list to be returned. Keep the loop going so till the queue is empty.

Time: O(n)
Space: O(n)
