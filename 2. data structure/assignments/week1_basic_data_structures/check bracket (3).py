
# coding: utf-8

# In[45]:


# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    current_opening = []
    
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            current_opening.append(i+1)
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack: 
                return i+1
            closing = opening_brackets_stack.pop()
            if not are_matching(closing, next):
                return i+1
            else: current_opening.pop()
                
                
            pass
    if not opening_brackets_stack: 
        return -1
    else: return min(current_opening)


def main():
    text = input()
    #text = ""
    mismatch = find_mismatch(text)
    if mismatch == -1 : 
        print("Success")
    else: print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()

