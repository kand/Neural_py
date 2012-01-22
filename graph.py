from node import Node

class Graph:

    # Create a graph based on given parameters
    #   layers_nodes_count = a list of the number of nodes that should be in
    #       the layer that corresponds with list index
    def __init__(self, layers_nodes_count):
        self.layers = []
        self.nodeCount = 0

        # create layers
        for i in range(0, len(layers_nodes_count)):
            layer = []

            # create nodes in each layer
            for j in range(0, layers_nodes_count[i]):
                node = Node()
                node.id = "n%i" % self.nodeCount

                # connect node to all previous layer nodes, add dummy node
                if i > 0:
                    prevLayer = self.layers[i - 1]
                    for k in range(0, len(prevLayer)):
                        node.addIndegree(prevLayer[k],0.0)
                    dummy = Node()
                    dummy.id = "d"
                    dummy.output = 1.0
                    node.addIndegree(dummy,0.0)
                
                layer.append(node)
                self.nodeCount += 1
            
            self.layers.append(layer)

    # Activate the graph to get a result
    #   input_list = list of inputs
    # returns list of outputs produced by node activation
    def activate(self, input_list, threshold):
        outputs = []

        # set inputs in graph
        for i in range(0, len(input_list)):
            self.layers[0][i].output = input_list[i]
        # active each layer forward through the graph
        for i in range(1, len(self.layers)):
            # sequentially activate each node in layer
            for j in range(0, len(self.layers[i])):
                result = self.layers[i][j].activate(threshold)

                #get outputs
                if i == len(self.layers) - 1:
                    outputs.append(self.layers[i][j].output)
                    
        return outputs

    # String rep of Graph
    def __repr__(self):
        ret = "nodes: %i\n" % self.nodeCount
        ret += "Layer,Node,Input,(Indegree:weight)...\n"

        layerNum = 0
        for layer in self.layers:
            for node in layer:
                ret += "%i,%s,%.4f," % (layerNum, node.id, node.input)
                for indegree in node.indegrees:
                    ret += "(%s:%.4f)" % (indegree.origin.id,indegree.weight)
                ret += "\n"
            layerNum += 1

        return ret
        
