
# coding: utf-8

# In[18]:


# Uses python3
def edit_distance(s, t):
    rows, cols = (len(s)+1, len(t)+1) 
    arr = [[0 for x in range(cols)] for x in range(rows)]
    for i in range(0, len(s)+1):
        for j in range(0, len(t)+1):
            if i == 0:
                arr[i][j] = j
            elif j == 0: 
                arr[i][j] = i    # Min. operations = i 
  
            # If last characters are same, ignore last char 
            # and recur for remaining string 
            elif s[i-1] == t[j-1]: 
                arr[i][j] = arr[i-1][j-1] 
  
            # If last character are different, consider all 
            # possibilities and find minimum 
            else: 
                arr[i][j] = 1 + min(arr[i][j-1],        # Insert 
                                   arr[i-1][j],        # Remove 
                                   arr[i-1][j-1])
            #if j == 0 and i > 0:
            #    arr[i][j] = arr[i-1][j]+1
    
    
    return arr[rows-1][cols-1]
    
    
    #write your code here
    return 0

if __name__ == "__main__":
    #s = "editing"
    #t = "distance"
    #print(edit_distance(s,t))
    print(edit_distance(input(), input()))

