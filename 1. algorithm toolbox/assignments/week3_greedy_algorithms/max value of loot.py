
# coding: utf-8

# In[ ]:


import sys

def maxLoot(a, items):
    items = dict(sorted(items.items(), key=lambda x: x[1] / x[0]))
    maxValue = 0
    capacity = a[1]
    for i in items.items():
        curWeight = i[1]
        curValue = i[0]
        if capacity == 0: break
        if capacity - curWeight >= 0 :
            maxValue += curValue
            capacity -= curWeight
        else:
            fraction = float(capacity)/curWeight
            maxValue += curValue*fraction
            capacity = 0
        
    return '%.4f' % maxValue

if __name__ == "__main__":
    a = [int(x) for x in input().split()]
    items = dict(input().split() for _ in range(a[0]))
    items = {int(k):int(v) for k, v in items.items()}
    print (maxLoot(a,items))


# In[ ]:


#advertisemnet revenue
n = int(input())
profit = [int(x) for x in input().split()]
click = [int(x) for x in input().split()]
def maxRevenue(n, profit, click):
    profit.sort()
    click.sort()
    maxR = 0
    for i in range(n):
        maxR += profit[i]*click[i]
    
    return maxR
maxRevenue(n, profit, click)

