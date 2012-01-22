from training import Training
from graph import Graph
from edge import Edge
from node import Node

def learnNAND():
    train = Training.readFromFile("training/NAND")
    graph = train.train(0.5)
    print repr(graph)

    print graph.activate([0,0],0.5)
    print graph.activate([1,0],0.5)
    print graph.activate([0,1],0.5)
    print graph.activate([1,1],0.5)

    return graph

def run():
    learnNAND()

run()
