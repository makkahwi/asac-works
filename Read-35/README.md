# Lesson 35 Reading

Navigation | [Past Reading](../Read-34/README.md) | [Home Page](../README.md) | [Next Reading](../Read-36/README.md) |

## Graphs

[Source](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-35/resources/graphs.html)

### Definition

Graph is a non-linear data structure of nodes. Those nodes could be shaped in random ways as it's basically about having nodes and connections between any of them. Graphs are constructed of vertex / nodes (data objects), edges (connections between nodes). And each vertex have one or more Neighbors (nodes with common edges) & degree (no of edges linked to the node).

### Types

There are variant features nodes & graphs could have, like directed vs undirected, Complete vs Connected vs Disconnected, Cyclic vs Acyclic, Weighted vs Unweighted.

- Directed graphs: graphs where edges have specific directions.
- Complete graphs: graphs where each vertex have common edges with all the others.
- Connected graphs: graphs where each vertex have a minimum of one common edge with another vertex.
- Disconnected graphs: graphs where some vertex doesn't have any common edge with another vertex.
- Cyclic graphs: directed graphs with ability of going into circles through all the vertex.
- Weighted graphs: graphs with number-base weights for its edges.

### Representations

#### Matrices

Graphs could be represented using matrix. So following graph could be represented with following matrix.

![Graph](./graph.png)

|   | A | B | C | D | E | F | G | H |
| A | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| B | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| C | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| D | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 1 |
| E | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| F | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| G | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| H | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |

Where the values could represent the existence of an edge between vertices, or the weight of the edge in weighted graphs.

#### Adjacency List

Graphs could also represented using Adjacency List, which lists all the vertices and connected ones to them. So for the same graph above, Adjacency List is...

| A | -> | B | -> | D |    |   |    |   |    |   |
| B | -> | A | -> | D | -> | C |    |   |    |   |
| C | -> | B | -> | G |    |   |    |   |    |   |
| D | -> | A | -> | B | -> | E | -> | F | -> | H |
| E | -> | D |    |   |    |   |    |   |    |   |
| F | -> | D | -> | H |    |   |    |   |    |   |
| G | -> | B |    |   |    |   |    |   |    |   |
| H | -> | D | -> | F |    |   |    |   |    |   |

### Traversals

Graph Traversal could be done using...

- Queue-based Breadth First approach
- Or Stack-based Depth First approach

### Applications

- GPS and Mapping
- Driving Directions
- Social Networks
- Airline Traffic
- Netflix uses graphs for suggestions of products
