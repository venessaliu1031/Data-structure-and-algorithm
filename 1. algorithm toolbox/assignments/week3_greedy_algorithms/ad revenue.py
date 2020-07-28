
# coding: utf-8

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
print (maxRevenue(n, profit, click))

