class Vertex:
    """
    To creat a vertex (node)

    Args:
        None

    constructor:
        value, edges (list of edges)
    """

    def __init__(self, value):
        self.value = value
        self.edges = []


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, value):
        """
        Add a vertex (note)

        Args:
            Integer

        Returns:
            New Vertex
        """
        if value == None:
            raise Exception("Please give an input")

        vertex = Vertex(value)

        self.adj_list[value] = vertex

        return vertex

    def add_edge(self, first, second, weight=None):
        """
        Add an edge between two Vertices (nodes)

        Args:
            2 Vertices & weight value

        Returns:
            None
        """
        if not (first in self.adj_list):
            raise Exception(f"{first} isn't in the graph")

        if not (second in self.adj_list):
            raise Exception(f"{second} isn't in the graph")

        if weight:
            if not isinstance(weight, int) and not isinstance(weight, float):
                raise Exception("Weight should be numerical")

            self.adj_list[first].edges.append((second, weight))
            self.adj_list[second].edges.append((first, weight))

        else:
            self.adj_list[first].edges.append(second)
            self.adj_list[second].edges.append(first)

    def get_nodes(self):
        """
        Call all the verticies (nodes) as a collection

        Args:
            None

        Returns:
            Collection of verticies (nodes)
        """
        verticies = []

        for vertex in self.adj_list:
            verticies.append(vertex)

        return verticies

    def get_neighbours(self, vertex):
        """
        Call connected edges to a vertex (node) with the connection weight -if any-

        Args:
            Vertex (node)

        Returns:
            Edges collection
        """
        return self.adj_list[vertex].edges

    def size(self):
        """
        Count of verticies (nodes)

        Args:
            None

        Returns:
            integer signifies the size
        """
        return len(self.adj_list) or None


if __name__ == "__main__":
    pass
