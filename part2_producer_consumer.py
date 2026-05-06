# Producer-Consumer Problem
# Name: Syed Tahmid Manzoor

import threading
import time
import queue

basket = queue.Queue(maxsize=5)                 # create queue of max size 5 to represent the basket with limited capacity

def baker(name):
    for i in range (5):
        bread = f"Bread {i}"                    # create a bread item with unique name for each iteration
        basket.put(bread)                       # add bread to the basket, if basket is full, baker will wait until space is available
        print (f"{name} made {bread}")           
        time.sleep(1)                 # simulate time taken to bake bread, added delay to show the effect 

def customer(name):
     for i in range (5):
         bread = basket.get()            # get bread from the basket, if basket is empty, customer will wait until bread is available
         print(f"{name} ate {bread}")  
         time.sleep(1.5)              # simulate time taken to eat bread, added delay to show the effect

Baker1 = threading.Thread(target=baker,args=("Baker-1",))  # create thread for baker 1 and pass name as args to baker func
Baker2 = threading.Thread(target=baker,args=("Baker-2",))  # create thread for baker 2 and pass name as args to baker func      

Customer1 = threading.Thread(target=customer,args=("Customer-1",)) # create thread for customer 1 and pass name as args to customer func 
Customer2 = threading.Thread(target=customer,args=("Customer-2",)) # create thread for customer 2 and pass name as args to customer func



Baker1.start()       # start baker 1 thread
Baker2.start()
Customer1.start()    # start customer 1 thread
Customer2.start()
Baker1.join()       # wait for baker 1 thread to finish before moving on
Baker2.join()
Customer1.join()   # wait for customer 1 thread to finish before moving on
Customer2.join()

