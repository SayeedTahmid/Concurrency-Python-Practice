# Concurrency Assignment - Syed Tahmid Manzoor

## How to Run
- Part 1: `python part1_race_condition.py`
- Part 2: `python part2_producer_consumer.py`
- Part 3: `python part3_dining_philosophers.py`
- Part 4: `python part4_thread_pool.py`

## Part 1: Race Condition

This program demonstrates what happens when multiple threads 
share a variable without coordination.

For example if two threads both read value 500 at the same time,
both try to write 501 — we lose one update. This is a race condition.

A Lock fixes this by allowing only one thread to read and write 
at a time. Thread 1 reads 500, writes 501, releases lock. 
Then Thread 2 reads 501 and writes 502. No updates lost!

I learned that even simple operations like adding 1 are not 
safe when multiple threads share the same variable.

## Part 2: Producer-Consumer

This program demonstrates the balance between supply and demand
using a bakery simulation.

Bakers (producers) make bread and put it in a basket.
Customers (consumers) take bread from the basket.
The basket has a maximum size of 5.

If the basket is full, the baker waits before adding more.
If the basket is empty, the customer waits before taking.
This prevents overflow and underflow automatically.

Python's queue.Queue handles all of this without needing 
manual locks — put() waits if full, get() waits if empty.

I learned that thread safe data structures like Queue make
producer consumer problems much easier to solve.

## Part 3: Dining Philosophers

This program demonstrates deadlock and how to prevent it.

Deadlock is like a one way road where cars come from both sides
and get stuck — everyone is waiting for someone else to move 
but nobody can move at all.

In this program 3 philosophers sit at a table with 3 forks.
Each philosopher needs 2 forks to eat. Without a rule they all
grab one fork and wait for the other forever — deadlock!

We prevent this by always picking up the lower numbered fork 
first. This breaks the circular waiting because Philosopher 2
must compete with Philosopher 0 for Fork 0 instead of waiting
in a circle. One wins, eats, puts forks down, other proceeds.

I learned that deadlock happens when everyone is waiting for 
each other and nobody can move forward. Breaking the circular
wait prevents it completely.

## Part 4: Thread Pool

This program demonstrates the difference between sequential 
and parallel task execution by measuring and comparing their 
execution times.

In sequential execution, 1 task is done at a time — like 1 
cashier serving customers one by one. In parallel execution, 
4 tasks run at the same time — like 4 cashiers serving 4 
customers simultaneously.

A thread pool means having fixed workers to do multiple tasks 
rather than using 1 worker for 1 task and hiring a new one 
for every next task. The same 4 workers handle all 10 tasks 
by picking up a new task as soon as they finish one.

In my program sequential took 13.69 seconds while parallel 
took only 3.59 seconds — making it 2.81x faster!

I learned that thread pools are efficient because workers are 
reused instead of created and destroyed for every task, and 
running tasks in parallel is much faster than one at a time.

## General Observations

- Concurrency bugs are hard to spot because they depend on timing
- Python has built in tools like Lock, Queue and ThreadPoolExecutor
  that make concurrency much safer and easier
- Always test concurrent code multiple times — a bug that appears
  once every 10 runs is still a bug!