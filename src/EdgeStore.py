from Edge import Edge

class EdgeStore:
    def __init__(self, func):
        self.edges = []
        self.func = func
    
    def getEdge(self, a, b):
        for edge in self.edges:
            if(edge.isSameEdge(a,b)):
                return edge
        
        edge = Edge(a, b, self.func)
        self.edges.append(edge)
        return edge