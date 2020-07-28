
# coding: utf-8

# In[33]:


# binary search
# Uses python3
import sys

def binary_search(a, left, right, x):
    print("left: " + str(left))
    print("right" + str(right))

    if right < left: return -1
    mid = round((left+right)/2)
    print("mid: "+ str(mid))
    if x == a[mid]: 
        return mid
    elif x < a[mid]:
        right = mid-1
        return binary_search(a, left, right, x)
    else: 
        left = mid+1
        return binary_search(a, left, right, x)
    # write your code here

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    #a = [1, 5, 8, 12, 13]
    #m = [13]
    left = 0
    right = len(a)-1
    
    #for x in m:
        #print(binary_search(a, left, right, x), end = ' ')
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, left, right, x), end = ' ')
        
    

