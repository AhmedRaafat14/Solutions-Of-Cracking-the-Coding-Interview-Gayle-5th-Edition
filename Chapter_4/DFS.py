from Chapter_4.Graph import Graph


# iterative solution
def dfs(g , start_vx):
    visited , st = set ( ) , [ start_vx ]
    while st:
        vx = st.pop ( )
        if vx not in visited:
            visited.add ( vx )
            # st.extend( set(g.getVertex(vx).getNeighbors()) - visited )
            for nbr in g.getVertex ( vx ).getNeighbors ( ):
                if nbr not in visited:
                    st.append ( nbr )
    return visited

# recursive solution
def recursive_dfs(g , start , visited=None):
    if not visited:
        visited = set ( )
    visited.add ( start )
    for vx in set ( g.getVertex ( start ).getNeighbors ( ) ) - visited:
        recursive_dfs ( g , vx , visited )
    return visited


# get graph paths
def dfs_paths(g , start , goal):
    st = [ (start , [ start ]) ]
    paths = [ ]
    while st:
        (vx , path) = st.pop ( )
        for vx in set ( g.getVertex ( vx ).getNeighbors ( ) ) - set ( path ):
            if vx == goal:
                paths.append ( path + [ vx ] )
                # yield path + [vx]
            else:
                st.append ( (vx , path + [ vx ]) )
    return paths


if __name__ == '__main__':
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

    print( list( dfs_paths(g, 'A', 'F') ) )
    print( dfs_paths(g, 'A', 'F') )
    print(dfs(g, 'A'))
    print( recursive_dfs(g, 'A') )

    # for v in g.getVertices():
    #     g_vx = g.getVertex(v)
    #     print( str(g_vx.getKey()) + ' : ' + str(g_vx.getNeighbors()) )

