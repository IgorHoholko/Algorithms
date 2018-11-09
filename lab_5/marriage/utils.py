import numpy as np
import copy

def marriage_desire_speed(M, W):
    n = M.shape[0]
    mdict = {i:None for i in range(n)}
    wdict = {i:None for i in range(n)}
    
    for column in M.T:
        for man, choice in enumerate(column):
            #if man is free, see
            if mdict[man] is None:
                #if women is free
                if wdict[choice] == None:
                    #couple without any problems
                    wdict[choice] = man
                    mdict[man] = choice

                #else if choice the women is worse than current one
                elif W[choice, wdict[choice]] > W[choice, man]:
                    #say sorry previous man
                    mdict[wdict[choice]] = None
                    # say 'hi' new man
                    wdict[choice] = man
                    # "my new girl"
                    mdict[man] = choice
                    
    return mdict




def marriage_speed_desire(W, M, MAX = 9999):
    W_copy = copy.deepcopy(W)
    n = M.shape[0]
    mdict = {i:None for i in range(n)}
    wdict = {i:None for i in range(n)}
    
    flag = True
    while flag:
        flag = False
        for women, row in enumerate(W_copy):
            if wdict[women] is None:
                flag = True
                choice = row.argmin()
                
                if mdict[choice] is None:
                    mdict[choice] = women
                    wdict[women] = choice
                
                elif W_copy[mdict[choice], W_copy[mdict[choice]].argmin()] > W_copy[women, choice]:
                    wdict[mdict[choice]] = None
                    W_copy[mdict[choice], W_copy[mdict[choice]].argmin()] = MAX
                    mdict[choice] = women
                    wdict[women] = choice
                else:
                    W_copy[women, choice] = MAX 

    return wdict




def get_description(men, women, couples):
    time = 0
    discontent = 0
    
    for i, j in couples.items():
        discontent += list(men[i]).index(j)
        time += women[i, j]
        
    min_time = np.sum(women.min(axis=1))
        
    print("discontent: ", discontent)
    print("time: ", time)
    print("min_time: ", min_time)
    print("min_time- time = ", time - min_time)