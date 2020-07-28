
# coding: utf-8

# In[99]:


# Uses python3
import sys

def get_majority_element(a, lo, hi):
    #if left == right:
    #    return -1
    #if left + 1 == right:
    #    return a[left]
    if len(a) == 1: return a[0]
    if len(a) == 2 and a[0] != a[1]: return -1
    if lo == hi:
        return -1
    if lo+1 == hi:
        return a[lo]

            # recurse on left and right halves of this slice.
    mid = (hi+lo)//2
    left = get_majority_element(a, lo, mid)
    right = get_majority_element(a, mid+1, hi)

            # if the two halves agree on the majority element, return it.
    if left == right:
        return left

            # otherwise, count each element and return the "winner".

    left_count = sum(1 for i in range(lo, hi+1) if a[i] == left)
    right_count = sum(1 for i in range(lo, hi+1) if a[i] == right)
    
    #if left_count >= len(a)//2 and left_count >= right_count: 
    #    return left
    #elif right_count >= len(a)//2 : return right
    #else: return -1
    if left_count > right_count and left_count > (hi-lo+1)//2: 
        return left
    elif right_count > left_count and right_count > (hi-lo+1)//2:
        return right
    else: return -1

    #return left if left_count > right_count else right
    #return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #n = 3
    #a = [1, 2, 3]
    #print(get_majority_element(a, 0, n-1))
    if get_majority_element(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)

