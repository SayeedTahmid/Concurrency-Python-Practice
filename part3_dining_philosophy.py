# Dining Philosophers Problem
# Name: Syed Tahmid Manzoor

import threading
import time

forks = [threading.Lock() for _ in range(3)]     # create locks to represent the forks, each fork can be held by only one philosopher at a time


def philosopher(id):               # id is the philosopher's number (0, 1, or 2)
    left_fork= id                  # left fork is the one with the same number as the philosopher
    right_fork = (id + 1) % 3      # right fork is the one with the next number, using modulo to wrap around to 0 for philosopher 2
    first_fork = min (left_fork, right_fork)  # to avoid deadlock, philosophers will always pick up the lower numbered fork first, this ensures that at least one philosopher can eat at a time
    second_fork = max (left_fork, right_fork)  # the second fork is the higher numbered one, this ensures that philosophers will not wait indefinitely for each other, preventing deadlock  

    for _ in range (3):        # each philosopher will repeat the cycle of thinking and eating 3 times 

        print(f"Philosopher {id} is thinking.")
        time.sleep(1)
        print (f"Philosopher {id} is hungry.")
          
        forks[first_fork].acquire()  # acquire the first fork, if it's not available, philosopher will wait until it is released
        print(f"Philosopher {id} picked up fork {first_fork}.")
        forks[second_fork].acquire() # acquire the second fork, if it's not available, philosopher will wait until it is released
        print(f"Philosopher {id} picked up fork {second_fork}.")  

        print(f"Philosopher {id} is eating.")
        time.sleep(2)

        forks[second_fork].release() # release the second fork after eating, making it available for other philosophers
        print(f"Philosopher {id} put down fork {second_fork}.")
        forks[first_fork].release()  # release the first fork after eating, making it available for other philosophers
        print(f"Philosopher {id} put down fork {first_fork}.")
     

P1=threading.Thread(target=philosopher,args=(0,)) # create thread for philosopher 1 and pass id as args to philosopher func, this will allow us to identify which philosopher is performing which action in the output
P2=threading.Thread(target=philosopher,args=(1,)) # same as above but for philosopher 2
P3=threading.Thread(target=philosopher,args=(2,)) # same as above but for philosopher 3, 
                                                  
 
P1.start()     # start philosopher 1 thread, this will allow philosopher 1 to begin its cycle of thinking and eating concurrently with the other philosophers
P2.start()     # same as above but for philosopher 2
P3.start()     # same as above but for philosopher 3, all three philosophers will run concurrently, simulating the dining philosophers problem where they must coordinate access to shared resources (the forks) without causing deadlock.
P1.join()      # wait for philosopher 1 thread to finish before moving on, this ensures that the main thread will not exit until all philosophers have completed their cycles of thinking and eating
P2.join()      # same as above but for philosopher 2
P3.join()      # same as above but for philosopher 3
