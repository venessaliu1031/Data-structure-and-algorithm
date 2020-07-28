
# coding: utf-8

# In[10]:


#last digit of partial sum of Fibonacci number
a = [int(x) for x in input().split()]

def Fn3(a):
    f0 = 0
    f1 = 1
    if a <= 1: return a
    else:
        rem = a % 60
        if(rem == 0): return 0

        for i in range(2, rem + 3): 
            f =(f0 + f1)% 60
            f0 = f1 
            f1 = f 
  
        s = f1-1
        return(s) 
print ((Fn3(a[1])-Fn3(a[0]-1))%10)

