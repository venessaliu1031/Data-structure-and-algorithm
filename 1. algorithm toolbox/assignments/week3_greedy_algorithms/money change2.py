
# coding: utf-8

# In[ ]:


#money change
d = [10, 5, 1]
def moneyChange(money):
    coinNumber = 0
    for i in d:
        if money >= i: 
            coinNumber += money//i
            money = money%i
        if money == 0: break
    return coinNumber
print (moneyChange(int(input())))

