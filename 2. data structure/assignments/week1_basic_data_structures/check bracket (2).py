
# coding: utf-8

# In[18]:


# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack: 
                return i+1
            if not are_matching(opening_brackets_stack.pop(), next):
                return i+1
    if not opening_brackets_stack: 
        return -1
    else: return len(opening_brackets_stack)


def main():
    text = input()
    #text = "[]]]]]"
    mismatch = find_mismatch(text)
    if mismatch == -1 : 
        print("Success")
    else: print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()

