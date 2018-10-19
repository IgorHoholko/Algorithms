
# coding: utf-8

# In[ ]:


from math import sqrt

CONST_KNUT = (sqrt(5) - 1) / 2
MY_CONST = 1117

class Hash_tbl_chains:
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
            if self.line[idx] is None:
                self.line[idx] = [list(key_value)]
            else:
                flag = True
                for j in range(len(self.line[idx])):
                    if self.line[idx][j][0] == key_value[0]:
                        self.line[idx][j][1] = key_value[1]
                        flag = False
                        break
                if flag: 
                    self.line[idx].append(list(key_value))
    
    def get(self, key):
        idx = self._get_hash(key)
        if self.line[idx] is None:
            return None
        else:
            for pair in self.line[idx]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    
    def delete(self, key):
        idx = self._get_hash(key)
        if self.line[idx] is None:
            return False
        else:
            for j, pair in enumerate(self.line[idx]):
                if pair[0] == key:
                    self.line[idx].pop(j)
                    return True
        return False
    
    
    def print(self): 
        for row in self.line:
            if row is not None:
                for pair in row:
                    print( f"{pair[0]} : {pair[1]}    ", end="")
                print()
                
        

