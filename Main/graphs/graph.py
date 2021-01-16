# representation using adjascency list
# the representation uses a linked list
# fir every vertex as the head f the list, other vertices are adjacent nodes

edges = [("A", "B"), ("A", "C"), ("B","C"), ("B", "D"),("B", "E"), ("C", "D"),("D", "E") ]
class Graph:
    def __init__(self, Nodes, is_directed=False):
        self.nodes = Nodes
        self.adjascenct_list = {}
        self.is_directed = is_directed
    
        #adding nodes to the graph
        for node in self.nodes:
            self.adjascenct_list[node] = []

    def add_edge(self, v, e):
        self.adjascenct_list[v].append(e)
        if not self.is_directed:
            self.adjascenct_list[e].append(v)

    def vertext_degree(self, node):
        return len(self.adjascenct_list[node])

    def print_adj(self):
        for node in self.nodes:
            print(node, ":", self.adjascenct_list[node])
    
    
Nodes = ["A", "B", "C", "D", "E"]
graph = Graph(Nodes, is_directed=True)
for i, j in edges:
    graph.add_edge(i, j)
graph.print_adj()


