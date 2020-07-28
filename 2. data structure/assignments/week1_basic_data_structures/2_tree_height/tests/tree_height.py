
# coding: utf-8

# In[18]:


# python3

import sys
import threading



#dynamic programming

#def compute_height(n, parents):
    # Replace this code with a faster implementation
    #max_height = 0
    #for vertex in range(n):
    #    height = 0
    #    current = vertex
    #    while current != -1:
    #        height += 1
    #        current = parents[current]
    #    max_height = max(max_height, height)
    #return max_height
    
def node_to_root(i, parents, heights):
    if parents[i] == -1: return 1
    
    if heights[i] != -1: return heights[i]
    
    heights[i] = node_to_root(parents[i], parents, heights)+1
    
    return heights[i]

def compute_height(n, parents):
    res = 0
    heights = [-1]*n
    
    for i in range(n):
        
        res = max(res, node_to_root(i, parents, heights))
    return res
            


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    #n = 1
    #parents = [-1]
    
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

