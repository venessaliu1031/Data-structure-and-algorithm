
# coding: utf-8

# In[ ]:


import sys

def get_optimal_value(capacity, weights, values):
    
    n = len(weights)

    unitValues_list = []

    #First lets calculate the unitValues_list
    for i in range (n):
        unitValue = (values[i]/weights[i])
        unitValues_list.append(unitValue)

    #Now lets fill the knapsack, intake is how much is in the bag at the moment!
    intake = 0
    max_value = 0
    factor = True

    while(factor):
        max_index = unitValues_list.index(max(unitValues_list, default=0)) 
        # this gives the index of the max valued element

        if(weights[max_index] <= capacity):
            # In this case, full item is taken in
            intake = weights[max_index]
            capacity -= weights[max_index]
            max_value += values[max_index]

        else:
            # weight_list[max_index] > capacity
            # In this case, fraction to be taken
            fraction = capacity / weights[max_index] 
            max_value += values[max_index]*fraction
            capacity = int(capacity - (weights[max_index] * fraction))

        weights.pop(max_index)
        values.pop(max_index)
        unitValues_list.pop(max_index)
        #print(weights)

        n -= 1 #no. of items left
        factor = ((n != 0) if ((capacity != 0) if True else False) else False)

    return max_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))


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

