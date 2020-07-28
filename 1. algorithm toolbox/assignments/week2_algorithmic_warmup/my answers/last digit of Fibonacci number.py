
# coding: utf-8

# In[ ]:


#last digit of Fibonacci number
a = int(input())
f = {0:1, 1: 1}
for i in range(2,a):
    f[i] = (f[i-1] + f[i-2])%10

print(f[i])

