import math

from edge import Edge

class Node:

    def __init__(self):
        self.id = ""
        self.indegrees = []
        self.outdegrees = []
        self.output = 0.0
        self.input = 0.0

    def addIndegree(self, origin, weight):
        edge = Edge(origin, self, weight)
        self.indegrees.append(edge)
        origin.outdegrees.append(edge)
        return edge

    def collectInput(self):
        self.input = 0.0
        for edge in self.indegrees:
            self.input += edge.origin.output * edge.weight
        return self.input

# TODO : remove threshold, non-working logistic activation
##    def activate(self, threshold):
##        self.output = 1/(1+math.e**self.collectInput())
##        return self.output

    def activate(self, threshold):
        if self.collectInput() > threshold: self.output = 1
        else: self.output = 0
        return self.output

    def __repr__(self):
        ret = "%s,%.4f,%.4f" % (self.id, self.input, self.output)
        if len(self.indegrees)> 0:
            ret += ","
        for indegree in self.indegrees:
            ret += "(%s:%.4f)" % (indegree.origin.id,indegree.weight)
        return ret
