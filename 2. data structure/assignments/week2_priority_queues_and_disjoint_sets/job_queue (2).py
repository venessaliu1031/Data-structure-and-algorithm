
# coding: utf-8

# In[45]:


# python3

from collections import namedtuple
import random

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def siftDown(i, next_free_time, worker_keys):
    if i >= len(next_free_time)//2: return
    minChild = i
    if i*2+1 < len(next_free_time) and next_free_time[i*2+1] < next_free_time[i]: 
        minChild = i*2+1
    if i*2+2 < len(next_free_time) and next_free_time[i*2+2] < next_free_time[minChild]:
        minChild = i*2+2
    if minChild != i:
        next_free_time[i], next_free_time[minChild] = next_free_time[minChild], next_free_time[i]
        worker_keys[i], worker_keys[minChild] = worker_keys[minChild], worker_keys[i]
        
        siftDown(minChild, next_free_time, worker_keys)
    else: return
    
def find_free_worker2(i, min_time, next_free_time, worker_keys):
    #if i >= len(next_free_time)//2: return i
    left_index = right_index = i
    left_id = right_id = worker_keys[i]
    if i*2+1 < len(next_free_time):
        left = next_free_time[i*2+1]
        if left == min_time and worker_keys[i*2+1] < worker_keys[i]:
            left_index = find_free_worker2(i*2+1, min_time, next_free_time, worker_keys)

    if i*2+2 < len(next_free_time):
        right = next_free_time[i*2+2]
        if right == min_time and worker_keys[i*2+2] < worker_keys[i]:
            right_index = find_free_worker2(i*2+2, min_time, next_free_time, worker_keys)
    
    minID_index = i
    if worker_keys[left_index] < worker_keys[minID_index]:
        minID_index = left_index
    if worker_keys[right_index] < worker_keys[minID_index]:
        minID_index = right_index
        
        
    return minID_index
 
    
def find_free_worker(i, next_free_time, worker_keys):
    if i >= len(next_free_time)//2: return i
    minKey = worker_keys[i]
    child = i
    if i*2+1 < len(next_free_time) and next_free_time[i*2+1] == next_free_time[i]: 
        
        if worker_keys[i*2+1] < worker_keys[i]:
            left = find_free_worker(i*2+1, next_free_time, worker_keys)
            minKey = worker_keys[i*2+1]
            child = i*2+1
            
    if i*2+2 < len(next_free_time) and next_free_time[i*2+2] == next_free_time[i]:
        if worker_keys[i*2+2] < minKey:
            minKey = worker_keys[i*2+2]
            child = i*2+2
    
    if minKey != worker_keys[i]:
            
        next_free_time[i], next_free_time[child] = next_free_time[child], next_free_time[i]
        worker_keys[i], worker_keys[child] = worker_keys[child], worker_keys[i]
        find_free_worker(i*2+1, next_free_time, worker_keys)
    else: return


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    
    result = []
    next_free_time = [0] * n_workers
    worker_keys = [x for x in range(n_workers)]
    work_log = []
    for job in jobs:
        min_index = find_free_worker2(0, next_free_time[0], next_free_time, worker_keys)
        if min_index != 0:
            next_free_time[0], next_free_time[min_index] = next_free_time[min_index], next_free_time[0]
            worker_keys[0], worker_keys[min_index] = worker_keys[min_index], worker_keys[0]
        work_log.append((worker_keys[0], next_free_time[0]))
        next_free_time[0] += job
        siftDown(0, next_free_time, worker_keys)

    return work_log


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    
    #n_workers = 2
    #n_jobs = 10
    #jobs = []
    #for i in range(n_jobs):
    #    jobs.append(1)
    
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)
    

    for i, j in assigned_jobs:
        print(i, j)


if __name__ == "__main__":
    main()

