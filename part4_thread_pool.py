# Part 4: Thread Pool for Parallel Tasks
# Name: Syed Tahmid Manzoor

import concurrent.futures
import threading
import time
import random

def process_task(task_id):
    
    thread_name= threading.current_thread().name      # get the name of the current thread, this will help us identify which thread is processing which task in the output
    work_time= random.uniform(0.5,2.0)    # simulate variable work time for each task, this will help demonstrate the benefits of parallel execution as tasks will complete at different times, showing how threads can work on multiple tasks concurrently   
    
    print(f"Task {task_id} starting on {thread_name}")
    time.sleep(work_time)   
    print (f"Task {task_id} done ! ") 
    
    return task_id

print (" ---- Sequential Execution ----")

start = time.time()  # record the start time of sequential execution, this will allow us to compare the total time taken for sequential vs parallel execution at the end

for i in range (10):

    process_task(i) # process tasks sequentially, demostrate how each task is completed one after the other, this will show the total time taken for sequential execution 

sequential_time = time.time() - start  # calculate the total time taken for sequential execution
print (f"Sequential execution time: {sequential_time:.2f} seconds")    


print (" ---- Parallel Execution ---- ")

start = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:  # create thread pool with maximum of 4 worker threads, this allows to execute multiple tasks concurrently
    results = executor.map (process_task,range(10))  # map the process_task function to a range of task IDs (0 to 9), this will submit all tasks to the thread pool for execution, and they will be processed in parallel by the available worker threads

parallel_time = time.time() - start
print (f"Parallel execution time: {parallel_time:.2f} seconds")


print (" ---- Comparison ---- ")

speedup = sequential_time / parallel_time

if speedup > 1:
    print(f"Parallel is {speedup:.2f}x faster than Sequential!")
else:
    print(f"Sequential is {1/speedup:.2f}x faster than Parallel!")