
# coding: utf-8

# In[4]:


import sys


def compute_min_refills(distance, tank, stops):
    x = 0 
    fuelN = 0
    stops.append(distance)
    for i in range(len(stops)):
        if stops[i]-x > tank: 
            fuelN += 1
            x = stops[i-1]
        if x + tank > distance: 
            break
        if stops[i+1]-stops[i]>tank: return -1
    return fuelN

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))

