def get_Euler_path(G, key = None):
    """
    Get Euler path in the graf if it exist.
    
    Parameters
    -------
        G : object
            Object of the Graph's class
        key: string, int
            Starting vertex in the path.
        
    Returns
    -------
        path : array
            Array of the Euler path's vertices.
    """
    #create the adjacency list
    graph = G.get_list()
    
    #if graph is not Euler return None
    for row in graph:
        if len(row) % 2 != 0 or len(row) == 0:
            print("graph hasn't a got Eulear cycle")
            return None

    
    #if user sent the starting vertex's key
    if key is not None:
        #give the vertex's idx from the key
        v = G._keys_to_indexis(key)
        stack = [v]
    else:
        #else start from the first vertex in the graf
        stack = [0]
    #Euler path  
    path = []

    while stack:
        v = stack[-1]
        if graph[v]:
            u = graph[v][0]
            stack.append(u)
            # deleting edge u-v
            del graph[u][ graph[u].index(v)]
            del graph[v][0]
        else:
            path.append( stack.pop() )
           
    return G._indexis_to_keys( path )




def bipartite(G):
    """
    Get componets of the bipartite graph if it is.
    
    Parameters
    -------
        G : object
            Object of the Graph's class.
    Returns
    -------
        components : array
            Array with components of the graph.
    """
    visited = set()
    stack = [0]
    colors = [None]*G.n
    
    graph = G.get_list()
    
    colors[0] = 0
    
    while stack:
        #current vertex
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
        
            #set of vertices 'visited' set doesn't have
            new_vertices = set(graph[vertex]) - visited
            stack.extend(new_vertices)

            for p in new_vertices:
                c = (colors[vertex] - 1) % 2
                if colors[p] == None:
                    colors[p] = c
                elif colors[p] != c:
                    print("Graph isn't bipartite")
                    return None
    
    components = [list([]),list([])]
    for i, fl in enumerate(colors):
        if fl == 0:
            components[0].append(G._indexis_to_keys(i))
        elif fl == 1:
            components[1].append(G._indexis_to_keys(i))
            
    
    return components




    
def bfs_components(G, key):
    """
    Get componets of the bipartite graph if it is.
    
    Parameters
    ----------
        G : object
            Object of the Graph's class.
        key : string, int
            Name of the vertex in the graph we need to define the position.
    
    Returns
    -------
        visited : array
            Array with visited points (components' points) of the graph.
    """
    v = G._keys_to_indexis(key)
    visited = set()
    stack = [v]
    
    graph = G.get_list()
    
    while stack:
        #current vertex
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(set(graph[vertex]) - visited)

    visited = G._indexis_to_keys(visited)
    
    return visited
    


