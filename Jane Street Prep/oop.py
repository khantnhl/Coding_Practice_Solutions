class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = [] # list of edge objects

