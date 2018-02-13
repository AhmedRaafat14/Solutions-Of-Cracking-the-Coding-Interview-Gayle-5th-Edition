from Chapter_4.Graph import Graph

g = Graph()

for i in range(6):
    g.addVertex(i)
#
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

# for vx in g:
#     print(vx.getKey())

# print( 2 in g )
# print( g.getVertices() )
for i in range(6):
    g_vx = g.getVertex(i)
    # print( str(g_vx.getKey()) + '  is ConnectedTo:  ' + str(g_vx.getNeighbors()) )
    print ( str ( g_vx.getKey ( ) ) + '  is ConnectedTo: {vertex: edge weight/cost}  ' + str ( g_vx.getEdges ( ) ) )
#
# for v in g:
#     # print(v)
#     for w in v.getNeighbors():
#         print( "(%s, %s)" % (v.getKey(), str(w)) )