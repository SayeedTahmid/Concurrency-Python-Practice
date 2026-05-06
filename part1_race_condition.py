# Race Condition and Basic Synchronization
# Name: Syed Tahmid Manzoor

import threading 

class CounterUnsafe:                      # class built for "without lock"
     def __init__(self):
          self.value = 0                  # initialize starting value = 0

     def increment(self):
          temp = self.value               # keep self.value in a temporary variable
          import time 
          time.sleep(0.000001)            # added delay to show race condition otherwise value appeared same without delay  
          temp += 1                       # increment the temporary variable
          self.value = temp               # after adding 1 to temp, assigning value back 

counter=CounterUnsafe()                   # create object of CounterUnsafe class
threads = []                              # empty list to store threads

def run_thread1(counter):                 # each thread will run this function and call increment method 1000 times 
     for i in range (1000):
          counter.increment()             # incrementing the counter 1000 times in each thread

for i in range (3):                       # creating 3 threads and starting them
    t=threading.Thread(target=run_thread1,args=(counter,))   
    threads.append(t)                     # add thread to list of threads
    t.start()                             # start the thread

for t in threads:                               
        t.join()                          # wait for all threads to finish before moving on


print(" ---- Without Lock ---- ")
print(f"Final counter value: {counter.value}")
print("Expected counter value: 3000")

class CounterSafe:                        # class built for "with lock"
     def __init__(self):                   
          self.value = 0                  # initialize starting value = 0
          self.lock = threading.Lock()    # create a lock object to control access to the critical section

     def increment(self):
          with self.lock:                 # acquire the lock before entering the critical section and automatically release it after exiting
               temp = self.value
               temp += 1
               self.value = temp     

counter = CounterSafe()
threads = []

def run_thread2(counter):
     for i in range (1000):
          counter.increment()

for i in range (3):
     t=threading.Thread(target=run_thread2,args=(counter,))
     threads.append(t)
     t.start()

for t in threads:
     t.join()

print(" ---- With Lock ---- ")
print(f"Final counter value: {counter.value}")
print("Expected counter value: 3000")                    















"""
Practice Codes

import threading

def say_hello():
    print("Hello from a thread")

t=threading.Thread(target=say_hello)
t.start()
t.join()


import threading

def three_threads(i):
     print(f"Thread {i} is running")

for i in range(3):
  t=threading.Thread(target=three_threads,args=(i,))
  t.start()
  t.join()


def one_thread():
    print("Thread X is running")

def two_threads():
    print("Thread X is running")

def three_threads():
    print("Thread X is running")    


import threading

class Counter:
    def __init__(self):
        self.value = 0

    def increment (self):
        temp = self.value
        import time
        time.sleep(0.000001)
        temp += 1
        self.value = temp

def run_thread(counter):
    for i in range(1000):
        counter.increment()

counter = Counter()
threads=[]

for i in range(3):
    t=threading.Thread(target=run_thread,args=(counter,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final counter value: {counter.value}")
print("Expected counter value: 3000")



import threading

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment (self):
      with self.lock:
         temp = self.value
         import time
         time.sleep(0.000001)
         temp += 1
         self.value = temp

def run_thread(counter):
    for i in range(1000):
        counter.increment()

counter = Counter()
threads=[]

for i in range(3):
    t=threading.Thread(target=run_thread,args=(counter,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final counter value: {counter.value}")
print("Expected counter value: 3000")

"""