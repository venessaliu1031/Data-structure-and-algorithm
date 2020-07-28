
# coding: utf-8

# In[14]:


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
    for number, name in contacts.items():
        if number == cur_number:
            contacts[number] = cur_name
            break
    else: # otherwise, just add it
        contacts[cur_number] = cur_name
    
    return contacts


def find_contact(contacts, cur_number):
    for number, name in contacts.items():
        if number == cur_number:
            return name
    return 'not found'

def delete_contact(contacts, cur_number):
    for number, name in contacts.items():
        if number == cur_number:
            contacts.pop(number)
            break
    return contacts

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = {} #number: name
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            contacts = add_contact(contacts, cur_query.number, cur_query.name)
            
        elif cur_query.type == 'del':
            contacts = delete_contact(contacts, cur_query.number)
            
        else:
            response = find_contact(contacts, cur_query.number)
            result.append(response)
    return result




if __name__ == '__main__':
    write_responses(process_queries(read_queries()))


# In[ ]:


add 911 police
add 76213 Mom
find 76213
find 910
find 911
del 911

