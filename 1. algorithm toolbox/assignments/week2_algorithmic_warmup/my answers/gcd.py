
# coding: utf-8

# In[ ]:


#greatest common divider

def gcd(n, m):
    r = 0
    if m == 0: return n
    else: 
        r = n%m
        n = m
        m = r
    return gcd(n,m)

a = [int(x) for x in input().split()]
gcd(a[0], a[1])

