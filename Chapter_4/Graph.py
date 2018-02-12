from Chapter_4.Vertex import Vertex

class Graph:
    def __init__(self):
        self.vertixList = {}
        self.vertixCount = 0

    def addVertex(self, key):
        """
        :param key: new vertex key value
        :return: return new added vertex
        """
        self.vertixCount += 1
        new_vx = Vertex(key)
        self.vertixList[key] = new_vx
        return new_vx

    def getVertex(self, vxKey):
        """
        :param vx: the vertex key wiche we want it 
        :return: the vertex if exist otherwise return None
        """
        if vxKey in self.vertixList:
            return self.vertixList[vxKey]

        return None

    def addEdge(self, fromVX, toVx, weight = 0):
        """
        :param fromVX: vertex which we start edge from it
        :param toVx:  vertex which we end the edge on it
        :param weight: Edge cost value
        :return: void
        """
        if fromVX not in self.vertixList:
            new_vx = self.addVertex(fromVX)
        if toVx not in self.vertixList:
            new_vx = self.addVertex(toVx)

        self.vertixList[ fromVX ].addNeighbor ( toVx , weight )

    def getVertices(self):
        """
        :return: graph vertices 
        """
        return self.vertixList.keys()

    def __contains__(self, item):
        """
        :param item: vertex key 
        :return: True if item exist as vertex in graph, Fase oterwise
        """
        return  item in self.vertixList

    def __iter__(self):
        """
        :return: return graph nodes 
        """
        return iter(self.vertixList.values())