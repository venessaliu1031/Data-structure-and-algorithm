
# coding: utf-8

# In[6]:


# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c
        
        #self.key = [4, 2, 5, 1, 3]
        
        #self.left = [1, 3, -1, -1, -1]
        #self.right = [2, 4, -1, -1, -1]

    def inOrder(self):
        self.result = []
        self.inOrderTraverse(0)
    
    # Finish the implementation
    # You may need to add a new recursive method to do that
                
        return self.result
    
    def inOrderTraverse(self, i):
        if i == -1:
            return
        self.inOrderTraverse(self.left[i])
        self.result.append(self.key[i])
        self.inOrderTraverse(self.right[i])
        
        



    def preOrder(self):
        self.result = []
        self.preOrderTraverse(0)
    # Finish the implementation
    # You may need to add a new recursive method to do that
                
        return self.result
    
    def preOrderTraverse(self, i):
        if i == -1:
            return
        self.result.append(self.key[i])
        self.preOrderTraverse(self.left[i])
        self.preOrderTraverse(self.right[i])

    def postOrder(self):
        self.result = []
        self.postOrderTraverse(0)
    # Finish the implementation
    # You may need to add a new recursive method to do that
                
        return self.result
    
    def postOrderTraverse(self, i):
        if i == -1:
            return
        
        self.postOrderTraverse(self.left[i])
        self.postOrderTraverse(self.right[i])
        self.result.append(self.key[i])

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()

