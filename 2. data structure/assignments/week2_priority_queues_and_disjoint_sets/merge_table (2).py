
# coding: utf-8

# In[13]:


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False
        
        
        
        self.row_counts[src_parent] += self.row_counts[dst_parent]
        self.row_counts[dst_parent] = 0
        self.parents[dst_parent] = src_parent

        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        
        
        if self.row_counts[src_parent] > self.max_row_count:
            self.max_row_count = self.row_counts[src_parent]
        self.max_row_count = max(self.row_counts)
        return True

    def get_parent(self, table):
        if self.parents[table] == table: return self.parents[table]
        self.parents[table] = self.get_parent(self.parents[table])
        
        # find parent and compress path
        return self.parents[table]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    
    #n_tables = 6
    #n_queries = 4
    #counts = [10, 0, 5, 0, 3, 3]
    
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        #print(db.row_counts)
        #print(db.parents)
        print(db.max_row_count)


if __name__ == "__main__":
    main()


# In[17]:


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))
        self.true_index = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False
        
        true_src = self.true_index[src_parent]
        true_dst = self.true_index[dst_parent]
        
        self.row_counts[true_src] += self.row_counts[true_dst]
        self.row_counts[true_dst] = 0
        
        if self.ranks[dst_parent] <= self.ranks[src_parent]:
            self.parents[dst_parent] = src_parent
        else: 
            self.parents[src_parent] = dst_parent
            self.true_index[src_parent], self.true_index[dst_parent] =  self.true_index[dst_parent], self.true_index[src_parent]
        if self.ranks[dst_parent] == self.ranks[src_parent]:
            self.ranks[dst_parent] += 1

        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        
        
        if self.row_counts[src_parent] > self.max_row_count:
            self.max_row_count = self.row_counts[src_parent]
        self.max_row_count = max(self.row_counts)
        return True

    def get_parent(self, table):
        if self.parents[table] == table: return self.parents[table]
        self.parents[table] = self.get_parent(self.parents[table])
        
        # find parent and compress path
        return self.parents[table]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    
    #n_tables = 5
    #n_queries = 5
    #counts = [1, 1, 1, 1, 1]
    
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        #print(db.row_counts)
        #print(db.parents)
        print(db.max_row_count)


if __name__ == "__main__":
    main()

