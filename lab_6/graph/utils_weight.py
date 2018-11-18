import copy
from .graph import Graph


def get_merge(A, B):
    """
    Get merge of the A and B graphs.

    Parameters
    -------
        A : object
            First object of the Graph's class.
        B: string, int
            Second object of the Graph's class.
        
    Returns
    -------
        Graph : object
            Graph object - merge of the A and B graphs.
    """
    matr_intersect = copy.deepcopy(A.AM)

    dif = abs(A.AM - B.AM)
    matr_intersect[dif.nonzero()] = 0
    
    matr_intersect += dif
    
    return Graph(matr_intersect)
    
    

def get_min_weight_spanner(G, mod = "P"):
    """
    Get Minimum Spanning Tree.
    
    Parameters
    ----------
        G : object
            The graph's object.

        mod : optional
            The method of searching a Minimum Spanning Tree.

            ===   =======
            'P'    Prime
            'K'    Kruskal

    Returns
    -------
        path : object
            Graph object.
        """
    if mod == 'P':
        return _prim(G)
    elif mod == 'K':
        return _kruskal(G)
    
    
    
def _prim(G):
    "Searching a Minimum Spanning Tree with Kruskal algorithm"
    #Adj matrix of the graph G
    matr = G.AM
    
    #The same graph like G without any adj
    MST = copy.deepcopy(G)
    MST.remove_adj_completely()
    
    #list of visited points
    vizited=[0]
    #total weight
    W = 0
    
    #for each row in Adj Matrix
    for _ in range(len(matr)-1):
        edge, w = __search_min_edge_prime(matr, vizited)
        #edje[0] - old vertex
        #edge[1] - new vertex
        
        vizited.append(edge[1])
        MST._add_adj(edge[0],edge[1], w)
        W += w
    
    return MST, W
        
    


def _kruskal(G):
    "Searching a Minimum Spanning Tree with Kruskal algorithm"
    #Adj matrix of the graph G
    matr = G.AM
    
    #The same graph like G without any adj
    MST = copy.deepcopy(G)
    MST.remove_adj_completely()
    
    #map of components
    marks = [mark for mark in range(matr.shape[0])]
 
    #total weight
    W = 0
    
    #while number edges less than n-1
    for _ in range(matr.shape[0] - 1):
        edge, w = __search_min_edge_kruskal(matr, marks)
        #edje[0] - old vertex
        #edge[1] - new vertex

        __changeMarks(marks, edge)
        MST._add_adj(edge[0],edge[1], w)
        W += w

    return MST, W



def __search_min_edge_prime(matr, vizited):
    min_w = 99999
    for i in vizited:
        for idx, w in enumerate(matr[i]):
            if w > 0 and w < min_w and idx not in vizited:
                min_w = w
                edge = (i, idx)
    return edge, min_w



def __search_min_edge_kruskal(matr, marks):
    min_w = 9999
    
    for i in range(len(matr)):
        for j, w in enumerate(matr[i]):
            if w > 0 and w < min_w and marks[i] != marks[j]:
                    min_w = matr[i][j]
                    edge = (i, j)   
    return edge, min_w



def __changeMarks(marks, edge):
    oldMark, newMark = marks[edge[0]], marks[edge[1]]
    for i in range(len(marks)):
        if marks[i] == oldMark:
            marks[i] = newMark