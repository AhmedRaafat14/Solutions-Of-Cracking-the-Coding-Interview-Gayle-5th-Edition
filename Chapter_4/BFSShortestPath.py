from Chapter_4.Graph import Graph
import Chapter_4.BFS as bfs

# get shortest path: it will be the first path in generator thrown path
def shortest_path(g, start, goal):
    paths = bfs.bfs_paths(g, start, goal)[0]
    if paths:
        return paths
    return None
    # try:
    #     return next( bfs_paths(g, start, goal) )
    # except StopIteration:
    #     return None



g = Graph()

g.addEdge('A', 'B')
g.addEdge('A', 'C')

g.addEdge('B', 'A')
g.addEdge('B', 'D')
g.addEdge('B', 'E')

g.addEdge('C', 'A')
g.addEdge('C', 'F')

g.addEdge('D', 'B')

g.addEdge('E', 'B')
g.addEdge('E', 'F')

g.addEdge('F', 'C')
g.addEdge('F', 'E')

print( shortest_path(g, 'A', 'F') )

# for v in g.getVertices():
#     g_vx = g.getVertex(v)
#     print( str(g_vx.getKey()) + ' : ' + str(g_vx.getNeighbors()) )

