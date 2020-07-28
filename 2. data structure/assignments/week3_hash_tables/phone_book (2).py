
# coding: utf-8

# In[24]:


# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    #n = 3
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))
    
def add_contact(contacts, cur_number, cur_name):
    contacts[cur_number] = cur_name

    return contacts


def find_contact(contacts, cur_number):
    if cur_number in contacts:
        return contacts[cur_number]
    else: return 'not found'

def delete_contact(contacts, cur_number):
    if cur_number in contacts:
        contacts.pop(cur_number)
    return contacts

def process_queries(queries):
    # define hashing function
    m = 100000
    p = 100000019
    a = 25
    b = 8
    
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = {} #number: name
    for cur_query in queries:
        key = (a*cur_query.number+b)%p%m
        if cur_query.type == 'add':
            
            # if we already have contact with such number,
            # we should rewrite contact's name
            contacts = add_contact(contacts, key, cur_query.name)
            
        elif cur_query.type == 'del':
            
            contacts = delete_contact(contacts, key)
            
        else:
            response = find_contact(contacts, key)
            result.append(response)
            
    return result




if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

