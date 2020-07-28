
# coding: utf-8

# In[9]:


# Uses python3
import sys
import itertools

def partition3(A):
    n = len(A)
    total = 0
    i, j = 0, 0
      
    # calculate sum of all elements 
    for i in range(n): 
        total += A[i] 
      
    if total % 3 != 0: 
        return 0
      
    part = [[ True for i in range(n + 1)]  
                   for j in range(total // 3 + 1)] 
      
    # initialize top row as true 
    for i in range(0, n + 1): 
        part[0][i] = 1
          
    # initialize leftmost column,  
    # except part[0][0], as 0 
    for i in range(1, total // 3 + 1): 
        part[i][0] = 0
      
    # fill the partition table in 
    # bottom up manner 
    for i in range(1, total // 3 + 1): 
          
        for j in range(1, n + 1): 
            part[i][j] = part[i][j - 1] 
              
            if i >= A[j - 1]: 
                part[i][j] = (part[i][j] or 
                              part[i - A[j - 1]][j - 1]) 
          
    return part[total // 3][n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    #A = [3, 3, 3]
    print(partition3(A))

