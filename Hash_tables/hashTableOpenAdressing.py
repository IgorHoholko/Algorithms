
# coding: utf-8

# In[ ]:

from math import sqrt

CONST_KNUT = (sqrt(5) - 1) / 2
MY_CONST = 1117

class Hash_tbl_open_adressing:
    def __init__(self, size = 10, K = CONST_KNUT, A = 1117):
        self.size = size
        self.line = [None]*self.size
        self.K = K
        self.A = A
    
    def _get_hash(self, key):
        KA = self.K * self.A
        kKA = key * KA
        kKA = kKA - int(kKA)
        return int(kKA * self.size) 
    
    
    def add(self, *args):
        "args = (key, value)"
        for key_value in args:
        
            idx = self._get_hash(key_value[0])
            
            for i in range(self.size):
                h_idx = (idx + i) % self.size
                
                if self.line[h_idx] is None:
                    self.line[h_idx] = list(key_value)
                    break
                if self.line[h_idx][0] == key_value[0]:
                    self.line[h_idx][1] = key_value[1]
                    break
            if i == self.size - 1:
                print("ERROR. Small table")
                break

    def get(self, key):
        idx = self._get_hash(key)
        
        for i in range(self.size):
            h_idx = (idx + i) % self.size
            
            if self.line[h_idx][0] == key:
                return self.line[h_idx][1]
        return None
    
    
    def delete(self, key):
        idx = self._get_hash(key)
        
        for i in range(self.size):
            h_idx = (idx + i) % self.size  

            if self.line[h_idx][0] == key:
                self.line[h_idx] = None
                return
    
    
    def print(self): 
        for row in self.line:
            if row is not None:
                print( "{} : {}    ".format(row[0], row[1]), end="")
            print()
                

