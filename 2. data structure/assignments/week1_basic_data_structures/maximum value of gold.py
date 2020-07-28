
# coding: utf-8

# In[19]:


# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    result = 0
    maxWeight = [[0 for x in range(W+1)] for x in range(len(w)+1)]
    for i in range(1,len(w)+1):
        for m in range(1, W+1):
            maxWeight[i][m] = maxWeight[i-1][m]
            if w[i-1] <= m:
                currWeight = maxWeight[i-1][m-w[i-1]]+w[i-1]
                if maxWeight[i][m] < currWeight:
                    maxWeight[i][m] = currWeight
    return maxWeight[len(w)][W]
                
            
                
        

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    #W = 10
    #w = [1, 4, 8]
    print(optimal_weight(W, w))

