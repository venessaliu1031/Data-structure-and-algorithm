
# coding: utf-8

# In[34]:


# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))
    
def pre_hash(text, P, p, x):
    T = len(text)
    S = text[T-P:]
    H = [0]*(T-P+1)
    H[T-P] = poly_hash(S, p, x)
    y = 1
    for i in range(1, P+1):
        y = (y*x)%p
    for i in reversed(range(0, T-P)):
        H[i] = (x*H[i+1]+ord(text[i])-y*ord(text[i+P]))%p
    return H
    
    
def poly_hash(S, p, x):
    polyhash = 0
    for i in reversed(range(0,len(S))):
        polyhash = (polyhash*x + ord(S[i]))%p
    return polyhash
        
        
    

def get_occurrences(pattern, text):
    # indexes
    T = len(text)
    P = len(pattern)
    p = T*P+100000
    x = 26
    results = []
    pHash = poly_hash(pattern, p, x)
    
    H = pre_hash(text, P, p, x)
    
    for i in range(T-P+1):
        cur_hash = poly_hash(text[i:i+P], p, x)
        cur_substr = text[i:i+P]
        if pHash == cur_hash:
            if cur_substr == pattern:
                results.append(i)
    

    return results

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

