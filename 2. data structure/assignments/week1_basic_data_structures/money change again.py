
# coding: utf-8

# In[18]:


# Uses python3
import sys

def get_change(m):
    minNumCoins = [0]
    deno = [1, 3, 4]
    for i in range(1, m+1):
        minNumCoins.append(1000)
        for j in range(3):
            if i >= deno[j]:
                numCoins = minNumCoins[i-deno[j]]+1
                if numCoins < minNumCoins[i]:
                    minNumCoins[i] = numCoins  
    #write your code here
    return minNumCoins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    #m = 15
    print(get_change(m))

