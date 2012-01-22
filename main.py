from graph import Graph
from edge import Edge
from node import Node

def learnNAND():
    graph = Graph([2,1])

    training = [[0,0,1],[0,1,1],[1,0,1],[1,1,0]]
    learnRate = 0.1
    threshold = 0.5
    iterations = 9

    print("x1,x2,y,err,corr,w0,w1,w2")

    # loop through training iterations
    for i in range(0,iterations):

        print("---------- round %i ----------" % i)
        
        # loop through training set
        for j in range(0,len(training)):
            # set inputs
            graph.layers[0][0].output = training[j][0]
            graph.layers[0][1].output = training[j][1]

            # activate node, analyze
            result = graph.layers[1][0].activate(threshold)
            error = (training[j][2] * 1.0) - result
            correction = learnRate * error

            print("%i,%i,%i,%.4f,%.4f," \
                  % (training[j][0], training[j][1], result, \
                     error, correction)),

            # modify edge weights
            for edge in graph.layers[1][0].indegrees:
                incomingGuess = edge.origin.output

                # guess right: reward edges that guessed correctly OR
                # guess wrong: punish edges that guessed incorrectly
                if (correction > 0 and incomingGuess == training[j][2]) \
                   or (correction < 0 and incomingGuess != training[j][2]):
                    edge.weight += correction

                print("%.4f," % edge.weight),

            print

    return graph

def run():
    print repr(learnNAND())

run()
