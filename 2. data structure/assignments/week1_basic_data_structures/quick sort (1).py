
# coding: utf-8

# In[6]:


# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    j = l
    y = l
    
    for i in range(l+1, r+1):
        if a[i] < x:
            j += 1
            y += 1
            if j != y:
                a[i], a[j] = a[j], a[i]
                a[i], a[y] = a[y], a[i]
            else: a[i], a[j] = a[j], a[i]
        elif a[i] == x:
            y += 1
            a[i], a[y] = a[y], a[i]
    a[l], a[j] = a[j], a[l]
    return [j, y]


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition3(a, l, r)
    randomized_quick_sort(a, l, m[0] - 1);
    randomized_quick_sort(a, m[1] + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #n = 10
    #a = [10,9,8,7,6,5,4,3,2,1]
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

