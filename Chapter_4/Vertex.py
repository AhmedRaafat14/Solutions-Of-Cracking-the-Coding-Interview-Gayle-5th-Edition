class Vertex:
    def __init__(self, key):
        # hold vertex key val
        self.key = key
        # hold vertex connected to it neighbors
        self.neighbors = {}

    def addNeighbor(self, vx, weight = 0):
        """
            Add new neighbor to current vertex
        :param vx: new neighbor vertex
        :param weight: the edge between from current to new vx weight
        :return: void
        """
        self.neighbors[vx] = weight

    def getNeighbors(self):
        """
            This to return current vertex neighbors
        :return: list of connected verteces
        """
        return list(self.neighbors.keys())

    def getKey(self):
        """
        :return: current vertext key 
        """
        return self.key

    def getWeigt(self, neighborVx):
        """
        :param neighborVx: vertext want to get weight from current to it 
        :return: edge wieght from current to this neighborVx
        """
        return self.neighbors[neighborVx]

    # def __str__(self):
    #     return str(self.key) + ' connectedTo: ' + str([vx for vx in self.neighbors])