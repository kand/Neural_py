from graph import Graph

class Training:

    TYPE_EPOCH = "EPOCH"
    TYPE_MIN_ERROR = "MIN_ERROR"

    def __init__(self):
        self.layers = []
        self.learnRate = 0.0
        self.momentum = 0.0
        self.trainingType = Training.TYPE_EPOCH
        self.minError = 0.0
        self.maxIterations = 0
        self.trainingData = []

    # Based on given training parameters, create and train a graph
    #   threshold = activation threshold for nodes
    # returns a new Graph that has been trained
    def train(self, threshold):
        graph = Graph(self.layers)

        # get index of output layer
        outputIndex = len(self.layers)-1
        # get index of last input training data
        lastInputIndex = self.layers[0]

        # infer input/output based on size of layers[0] and
        #   layers[len(layers)-1]
        inputSize = self.layers[0]
        outputSize = self.layers[outputIndex]

        # loop through iterations
        for i in range(0, self.maxIterations):
            # loop through training set
            for j in range(0, len(self.trainingData)):
# TODO : replace this section with graph.activat()
                # set inputs in graph
                for k in range(0, inputSize):
                    graph.layers[0][k].output = self.trainingData[j][k]
                # active each layer forward through the graph
                for k in range(1, len(graph.layers)):
                    # sequentially activate each node in layer
                    for l in range(0, len(graph.layers[k])):
                        graph.layers[k][l].activate(threshold)
                # propagate delta error backwards from output to input
                for k in range(0,outputSize):
# TODO : should really be using derivative of output func, see book
                    node = graph.layers[outputIndex][k]
                    error = self.trainingData[j][lastInputIndex + k] \
                            - node.output
                    # update weights based on error
                    for edge in node.indegrees:
                        edge.weight += self.learnRate * edge.origin.output \
                                       * error
# TODO : should really be using derivative of output func, see book
                for k in range(outputIndex - 1, 0, -1):
                    for node in graph.layers[k]:
                        error = self.trainingData[lastInputIndex + k] \
                                - node.output
                        # update weights based on error
                        for edge in node.indegrees:
                            edge.weight += self.learnRate * edge.origin.output \
                                           * error

        return graph

    def __repr__(self):
        ret = "layers = %s\n" % str(self.layers).replace(" ","")
        ret += "learnRate = %s\n" % repr(self.learnRate)
        ret += "momentum = %s\n" % repr(self.momentum)
        ret += "type = %s\n" % self.trainingType
        ret += "minError = %s\n" % repr(self.minError)
        ret += "maxIterations = %i" % self.maxIterations
        for data in self.trainingData:
            ret += "%s\n" % str(data).strip("[]").replace(" ","")

        ret = ret.rstrip("\n")

        return ret

    # Read a file of training data. An example file layout:
    #   layers = [5,2,2,2]
    #   learnRate = 0.1
    #   momentum = 0.05
    #   type = EPOCH
    #   minError = 0.01
    #   maxIterations = 10000
    #   1,1,1,1,1,0,0
    #   <training data 2>
    #   ...
    #
    #   file_name = relative location of file
    # returns a new Training object set up as described in input file
    @staticmethod
    def readFromFile(file_name):
        ret = Training()
        
        f = open(file_name, 'r')

        # line 1: layer info
        ret.layers = [int(x) for x in f.readline().split()[2].strip("[]").split(",")]

        # line 2: learning rate
        ret.learnRate = float(f.readline().split()[2])

        # line 3: momentum
        ret.momentum = float(f.readline().split()[2])

        # line 4: training type
        ret.trainingType = f.readline().split()[2]

        # line 5: minimum error
        ret.minError = f.readline().split()[2]

        # line 6: max iterations
        ret.maxIterations =  int(f.readline().split()[2])

        # collect rest as training data
        line = f.readline()
        while line is not "":
            ret.trainingData.append([int(x) for x in line.strip().split(",")])
            line = f.readline()
        
        f.close()

        return ret
