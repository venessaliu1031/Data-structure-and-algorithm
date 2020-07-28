
# coding: utf-8

# In[15]:


# python3

def siftDown(i, data, swaps):
    if i >= len(data)//2: return swaps
    minChild = i
    if data[i*2+1] < data[i]: 
        minChild = i*2+1
    if data[i*2+2] < data[i*2+1]:
        minChild = i*2+2
    if minChild !=i:
        data[i], data[minChild] = data[minChild], data[i]
        swaps.append((i, minChild))
        siftDown(minChild, data, swaps)
    else: return swaps
    return swaps

def build_heap(data):
    
    
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    
    
    swaps = []
    for i in reversed(range(0, len(data)//2)):
        swaps = siftDown(i, data, swaps)
        
        
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    
    #n = 5
    #data = [5, 4, 3, 2, 1]
    
    assert len(data) == n
    
    

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

