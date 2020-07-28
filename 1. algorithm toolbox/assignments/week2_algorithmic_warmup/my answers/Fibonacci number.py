
# coding: utf-8

# In[10]:


#Fibonacci number
a = int(input())
a1 = 0
a2 = 1
n = 0
i = 0
while(i < a-1):
    n = a1 + a2
    a1 = a2
    a2 = n
    i += 1

print(n)

