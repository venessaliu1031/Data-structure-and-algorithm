
# coding: utf-8

# In[10]:


#last digit of sum of square Fibonacci number
a = int(input())

def Fn4(a):
    f0 = 0
    f1 = 1
    s = 1
    if a <= 1: return a
    else:
        rem = a % 60
        if(rem == 0): return 0

        for i in range(2, rem + 1): 
            f = f0 + f1
            f0 = f1 
            f1 = f 
            s = f*f + s
  
        return (s) 
print(Fn4(a)%10)

