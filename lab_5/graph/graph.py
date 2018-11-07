import numpy as np
import copy
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, params_drawing = {}, storage_method = 'list'):
        """
        Parameters
        ----------
            params_drawing : dict
                The dict with params for drawing.
                'font_size' --- 'node_size' --- 'node_color' --- 'font_color' --- 'font_weight'
                
            storage_method : optional
                Variable to choose the method of the vertices' storing.
                
                ========    ============
                'matrix'    matrix only
                'list'      list only
                'both'      both of them
        """
        self.stor_method = storage_method
        self.list = list()     # adjacency List
        self.AM = None         # adjacency Matrix
        self.keys_idx = dict()
        self.idx_keys = dict()  
        self.params_drawing = {'font_size': 15, 'node_size' : 1000, 'node_color' : 'black',\
                               'font_color' : 'w', 'font_weight': 'bold'}
        self.m = 0    #num of the edges
        self.n = 0    #num of the vertices
        
        self.params_drawing.update(params_drawing)
        print(self.params_drawing)
      
    
    def _addTo_graph_list(self):
        "Expand the adjacency list when adding a point"
        self.list.append([])

            
    def _addTo_graph_matrix(self):
        "Expand the adjacency matrix when adding a point"
        if self.AM is not None:
            self.AM = np.hstack((self.AM, np.zeros((self.AM.shape[0], 1)) ))
            self.AM = np.vstack((self.AM, np.zeros((1, self.AM.shape[1])) ))
        else:
            self.AM = np.zeros((1, 1)) 
    
    
    def _add_adj(self, v, other_v, value = 1):
        "Add the adjacency between the vertex 'v' and the vertices(vertex) 'other_v' "
        self.AM[v, other_v] = value
        self.AM[other_v, v] = value
    
    def _del_adj(self, v, other_v):
        "Delete the adjacency between the vertex 'v' and the vertices(vertex) 'other_v' "
        self.AM[v, other_v] = 0
        self.AM[other_v, v] = 0
        
        
    def _keys_to_indexis(self, keys):
        "Transform vertices' keys to the vertices' idx"
        if type(keys) is tuple or type(keys) is list:
            return [self.keys_idx.get(el) for el in keys]
        else:
            return self.keys_idx.get(keys)
        
    def _indexis_to_keys(self, idxs):
        "Transform vertices' indexis to the vertices' keys"
        if type(idxs) is not int and type(idxs) is not str:
            return [self.idx_keys.get(el) for el in idxs]
        else:
            return self.idx_keys.get(idxs)
    
    def _creatr_idx_dict_from_keys_dict(self):
        "Create new the idx_keys dictionary from the keys_dict dictionary"
        self.idx_keys.clear()
        for key in self.keys_idx:
            self.idx_keys.setdefault(self.keys_idx[key], key)
        
        
    def _update_dicts(self, idx):  
        "Update dicts"
        for key in self.keys_idx:
            if self.keys_idx[key] > idx:
                  self.keys_idx[key] -=1
        self._creatr_idx_dict_from_keys_dict()
            
        
    def _del_v(self, v):
        "Delete the vertex v from the graph"
        #"Delete all connections of the point v with other ones"
        self.AM[v, :] = 0
        self.AM[:, v] = 0
        self.n -= 1
        
        #Selecte coordinates of the every point in the graph 
        #which is adjacent with some anather one
        col, row = np.where(self.AM == 1)
        
        #Create new adjacency matrix without old vertex
        self.AM = np.zeros((self.n, self.n))

        #Prepare coordinates for the created matrix
        for i in range(len(col)):
            if col[i] > v: col[i] -= 1
            if row[i] > v: row[i] -= 1
        
        self.AM[col, row] = 1
        
        
    def _matrix_to_list(self):
        "Transform the graph' adjacency matrix to the adjacency list"
        #Selecte coordinates of the every point in the graph 
        #which is adjacent with some anather one
        col, row = np.where(self.AM)
        
        #Create new adjacency list, and append all verteces from the gtaf
        self.list = []
        for _ in range(self.n):
            self._addTo_graph_list()
        
        #Add adjacency to the list
        for i in range(len(col)):
            self.list[col[i]].append(row[i])
    

    def get_list(self):
        self._matrix_to_list()
        return self.list


    def get_size(self):
        return self.n
        
    
    def add_v(self, *args):
        """
        Add the vertices to the graph.
        
        Parameters
        ----------
            args : tuple
                Set of the points (v1, v2, ... v_k).
        """
        for key in args:
            if self.keys_idx.get(key) == None:
                # add each new vertex to the dicts
                self.keys_idx.setdefault(key, self.n)
                self.idx_keys.setdefault(self.n, key)

                #expand the storage objects
                self._addTo_graph_matrix()
                #number of the vertices +1
                self.n += 1
    
        
    def add_adj(self, data):
        """ 
        Add the adjacency to the graph.
        
        Parameters
        ----------
            data : dict( key_i : (v_n) )
                Make adjacency between vertexx key_i and vertex/vertices v_n.
            
                =====    ==========================
                key_i    Any vertices in the graph.
                (v_n)    The tuple of vertices.
        """ 
        for key in data:
            #transform 'names' receiving from the user to the indexes
            idx = self.keys_idx.get(key)
            idxs_adj = self._keys_to_indexis(data[key])
            
            #add the edges to the storage objects
            self._add_adj(idx, idxs_adj)
    
    
    def remove_v(self, *args):
        """
        Remove the vertices from the graph.
        
        Parameters
        ----------
            args : tuple
                Set of the points (v1, v2, ... v_k).
        """
        for key in args:
            #transform key to the index of the point
            v_main = self._keys_to_indexis(key)
            
            #delete the vertex from the both dictionaries
            self.keys_idx.pop(key)
            self._update_dicts(v_main)
            
            #delete vertex from the adjacency matrix
            self._del_v(v_main)
        
            
    def set_weights(self, points, w):
        """ 
        Add the weight (w) the couple of the points.
        
        Parameters
        ----------
            points --- array
                Couple of the points (v1, v2).
            w --- value/array
                Weight between the couple of the points.
        """ 
        try:
            for i in range(len(w)):
                v1, v2 = self._keys_to_indexis(points[i])
                self._add_adj(v1, v2, w[i])
        except:
            v1, v2 = self._keys_to_indexis(points)
            self._add_adj(v1, v2, w)
    
            
    def remove_adj(self, data):
        """ 
        Remove the adjacency from the graph.
        
        Parameters
        ----------
            data --- dict( key_i : (v_n) )
                Delete adjacency between vertex key_i and vertex/vertices v_n.
                
                ======   ==========================
                key_i    Any vertices in the graph.
                (v_n)    Tuple of the vertices.
        """ 
        for key in data:
            #transform the 'names' receiving from the user to the indexes
            idx = self.keys_idx.get(key)
            idxs_adj = self._keys_to_indexis(data[key])
            
            #delete the edges from the storage objects
            self._del_adj(idx, idxs_adj)
    
    def remove_adj_completely(self):
        self.AM = np.zeros_like(self.AM)
    
    
    
    def print(self):
        """ 
        Print the incidence list.
        """
        
        self._matrix_to_list()
        for i, row in enumerate(self.list):
            print(self.idx_keys.get(i), ' : ', tuple([self.idx_keys.get(k) for k in row]))
        self.list = None
    
    
    def draw(self):
        """ 
        Draw the graph.
        """
        
        G=nx.Graph(self.AM)
#         labels = nx.get_edge_attributes(G,'weight')
        nx.draw(G, labels = self.idx_keys, \
                font_size= self.params_drawing.get('font_size'), \
                node_size=self.params_drawing.get('node_size'),  \
                node_color=self.params_drawing.get('node_color'),\
                font_color=self.params_drawing.get('font_color'),\
                font_weight=self.params_drawing.get('font_weight'))
