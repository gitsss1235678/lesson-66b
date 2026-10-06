class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for i in range(self.V):
            print("Adjacent list of vertex {}: \n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print("\n")

g = Graph(5)
g.add_edge(1, 0)
g.add_edge(4, 0)
g.add_edge(2, 1)
g.add_edge(3, 1)
g.add_edge(4, 1)
g.add_edge(3, 2)
g.add_edge(4, 3)

g.print_graph()