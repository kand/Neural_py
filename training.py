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
