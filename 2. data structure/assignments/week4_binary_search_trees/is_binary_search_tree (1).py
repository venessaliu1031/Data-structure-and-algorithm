
# coding: utf-8

# In[33]:


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
    
    
    
    
    return (IsBinarySearchTree(tree[i][1], tree, mini, tree[i][0]) 
        and IsBinarySearchTree(tree[i][2], tree, tree[i][0], maxi))


  # Implement correct algorithm here

def inOrderTraverse(i):
    if i == -1:
        return
    inOrderTraverse(tree[i][1])
    leftindex = tree[i][1]
    rightindex = tree[i][2]
    if tree[i][0] >= tree[leftindex][0]: return False 
    if tree[i][0] <= tree[rightindex][0]: return False
    inOrderTraverse(tree[i][2])
    
    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    #tree = [[2, 1, 2], [1, -1, -1], [3, -1, -1]]
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(0, tree, -4294967296, 4294967296):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()

