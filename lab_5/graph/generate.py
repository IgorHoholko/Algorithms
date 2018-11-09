import numpy as np 
from .graph import Graph


def generate_graph(low, high, n, drop = .5):
    """
    Get random Graph.

    Parameters
    -------
        low : int
            Lowest weight of the graph.
        high: int
            Highest weight the graph.
        n : int
            Size of the graph.
        drop: double
            Value between 0 and 1. 
            "How many edges do we need to remove?"
        
    Returns
    -------
        Graph : object
            Graph object.
    """
    #weight can't be negative (here)
    if low < 0: 
        print("Error")
        return None
    
    # Adj. natrix of our graph    
    AM = np.zeros((n,n))
    
    for i in range(1, n): 
        #drop vector
        drop_line = np.random.permutation( np.arange(n - i) )[:int((drop)* (n - i) )]
        
        #generate weights
        row = np.random.randint(low, high, (n - i))
        
        #remove ~ {drop}% adj.
        row[drop_line] = 0
        
        AM[i-1, i:] = row
    
    #form another part of the matrix
    AM += AM.T

    return Graph(AM)