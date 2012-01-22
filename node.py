from edge import Edge

class Node:

    def __init__(self):
        self.id = ""
        self.indegrees = []
        self.output = 0.0
        self.input = 0.0

    def addIndegree(self, origin, weight):
        edge = Edge(origin, self, weight)
        self.indegrees.append(edge)

    def collectInput(self):
        self.input = 0.0
        for edge in self.indegrees:
            self.input += edge.origin.output
        return self.input

    def activate(self):
        if self.collectInput > 0.5: self.output = 1
        self.output = 0
        return self.output
