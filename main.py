from training import Training
from graph import Graph
from edge import Edge
from node import Node

def learnNAND():
    train = Training.readFromFile("training/XOR")
    graph = train.train(0.5)
    print repr(graph)

    print "[0,0]", graph.activate([0,0],0.5)
    print "[1,0]", graph.activate([1,0],0.5)
    print "[0,1]", graph.activate([0,1],0.5)
    print "[1,1]", graph.activate([1,1],0.5)

    return graph

def run():
    learnNAND()

run()
