
# coding: utf-8

# In[10]:


#Fibonacci number again
def PisanoPeriod(m):
    m1, m2 = 0, 1
    for i in range(0, m * m): 
        m1, m2 = m2, (m1 + m2) % m 
          
        # A Pisano Period starts with 01 
        if (m1 == 0 and m2 == 1): 
            return i + 1

def FibonacciMod(n, m):
    pp = PisanoPeriod(m)
    n = n % pp
      
    n1, n2 = 0, 1
    if n==0: 
        return 0
    elif n==1: 
        return 1
    for i in range(n-1): 
        n1, n2 = n2, n1 + n2
          
    return (n2 % m) 

a = [int(x) for x in input().split()]

print (FibonacciMod(a[0], a[1]))

