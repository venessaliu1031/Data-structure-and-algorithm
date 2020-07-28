
# coding: utf-8

# In[24]:


import sys


def compute_min_refills(distance, tank, stops):
    limit = tank
    fuelN = 0
    stops.append(distance)
    stops.insert(0,0)
    if stops[1] > tank: return -1
    for i in range(1,len(stops)):
        stopDistance = stops[i]-stops[i-1]
        if stopDistance > tank:
            return -1
        if stopDistance <= limit:
            limit = limit-stopDistance
        else:
            fuelN += 1
            limit = tank-stopDistance
    return fuelN

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
    #distance = int(input())
    #miles = int(input())
    #stopN = int(input())
    #stops = [int(x) for x in input().split()]
    #print(compute_min_refills(distance, miles, stops))

