
# coding: utf-8

# In[19]:


#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(2*10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(i, tree, mini, maxi):
    if not tree: return True
    if i == -1:
        return True
    
    if tree[i][0] < mini or tree[i][0] > maxi: 
        return False
    
    
    
    
    return (IsBinarySearchTree(tree[i][1], tree, mini, tree[i][0]-1) 
        and IsBinarySearchTree(tree[i][2], tree, tree[i][0], maxi))


  # Implement correct algorithm here


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    #tree = [[2, 1, 2], [2, -1, -1], [3, -1, -1]]
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(0, tree, -4294967296, 4294967296):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()

