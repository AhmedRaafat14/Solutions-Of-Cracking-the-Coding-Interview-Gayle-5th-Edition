"""
Given a directed graph, design an algorithm to find out 
whether there is a route between two nodes
"""
from Chapter_4.Graph import Graph

def bfs_paths(g, start, goal):
    q = [ (start, [start]) ]
    # paths = []
    while q:
        (vx, path) = q.pop(0)
        for v in set( g.getVertex(vx).getNeighbors() ) - set( path ):
            if v == goal:
                return True
                # paths.append( path + [v] )
            else:
                q.append( (v, path + [v]) )
    return False

def dfs_paths(g , start , goal):
    st = [ (start , [ start ]) ]
    paths = [ ]
    while st:
        (vx , path) = st.pop ( )
        for v in set ( g.getVertex ( vx ).getNeighbors ( ) ) - set ( path ):
            if v == goal:
                return True
                # paths.append ( path + [ v ] )
            else:
                st.append ( (v , path + [ v ]) )
    return False

if __name__ == '__main__':
    """
          C <------- A ------> B ---------> D 
                                \          /
                                 \        /
                                  \      /
                                      E
    """

    g = Graph()

    g.addEdge('A', 'B')
    g.addEdge('A', 'C')

    g.addEdge('B', 'D')

    g.addEdge('D', 'E')

    g.addEdge('E', 'B')

    # # if dfs_paths(g, 'A', 'E'):
    # if dfs_paths ( g , 'E' , 'A' ):
    #     print( True )
    # else:
    #     print( False )

    if bfs_paths(g, 'A', 'E'):
    # if bfs_paths ( g , 'E' , 'A' ):
        print ( True )
    else:
        print ( False )

    # for v in g.getVertices():
    #     g_vx = g.getVertex(v)
    #     print( str(g_vx.getKey()) + ' : ' + str(g_vx.getNeighbors()) )