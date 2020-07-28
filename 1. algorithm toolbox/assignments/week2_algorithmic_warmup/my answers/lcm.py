
# coding: utf-8

# In[ ]:


#least common multiple
def gcd(n, m):
    r = 0
    if m == 0: return n
    else: 
        r = n%m
        n = m
        m = r
    return gcd(n,m)

a = [int(x) for x in input().split()]
lcm = int(a[0]*a[1]/gcd(a[0], a[1]))
print (lcm)

