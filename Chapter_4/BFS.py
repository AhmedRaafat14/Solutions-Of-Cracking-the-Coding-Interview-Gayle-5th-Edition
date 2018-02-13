from Chapter_4.Graph import Graph

# iterative solution
def bfs(g, start_vx):
    visited, q = set(), [start_vx]
    while q:
        vx = q.pop(0)
        if vx not in visited:
            visited.add(vx)
            for nbr in g.getVertex(vx).getNeighbors():
                if nbr not in visited:
                    q.append(nbr)
    return visited

# get graph paths
def bfs_paths(g, start, goal):
    q = [(start, [start])]
    paths = []
    while q:
        (vx, path) = q.pop(0)
        for vx in set(g.getVertex(vx).getNeighbors()) - set(path):
            if vx == goal:
                paths.append(path + [vx])
                # yield path + [vx]
            else:
                q.append( (vx, path + [vx]) )
    return paths


if __name__ == "__main__":
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

    # print( bfs(g, 'A') )
    print( list( bfs_paths(g, 'A', 'F') ) )

    # for v in g.getVertices():
    #     g_vx = g.getVertex(v)
    #     print( str(g_vx.getKey()) + ' : ' + str(g_vx.getNeighbors()) )