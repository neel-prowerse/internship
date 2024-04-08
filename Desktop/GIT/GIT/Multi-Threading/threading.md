# What is multi-threading?
--> The goal of multi-threading is to complete multiple task at same time, which improves applications rendering and performance.

# How to achieve multithreading in Python?
--> There are two main modules of multithreading used to handle threads in Python.
1. The thread module
2. The threading module

1. The Thread Module : 
--> It is started with Python 3, designated as obsolete, and can only be accessed with _thread that supports backward compatibility.

SYNTAX : thread.start_new_thread ( function_name, args[, kwargs] )  

2. The Threading Modules : 
--> The threading module is a high-level implementation of multithreading used to deploy an application in Python. To use multithreading, we need to import the threading module in Python Program.

start() - A start() method is used to initiate the activity of a thread. And it calls only once for each thread so that the execution of the thread can begin. 
run() - A run() method is used to define a thread's activity and can be overridden by a class that extends the threads class.
join() - A join() method is used to block the execution of another code until the thread terminates.


# Multithreading in Python
--> In Python, the threading module provides a very simple and intuitive API for spawning multiple threads in a program.

# STEP - 1 : Import Module
import threading

# STEP - 2 : Create a Thread 
--> To create a new thread, we create an object of the Thread class. It takes the ‘target’ and ‘args’ as the parameters. The target is the function to be executed by the thread whereas the args is the arguments to be passed to the target function.

t1 = threading.Thread(target, args)
t2 = threading.Thread(target, args)

# STEP - 3 : Start a Thread
--> To start a thread, we use the start() method of the Thread class.

t1.start()
t2.start()

# STEP - 4 : End a Thread Execution
--> Once the threads start, the current program (you can think of it like a main thread) also keeps on executing. In order to stop the execution of the current program until a thread is complete, we use the join() method.

t1.join()
t2.join()

--> As a result, the current program will first wait for the completion of t1 and then t2. Once, they are finished, the remaining statements of the current program are executed.


# What is multiprocessing?
--> Multiprocessing refers to the ability of a system to support more than one processor at the same time. Applications in a multiprocessing system are broken to smaller routines that run independently. The operating system allocates these threads to the processors improving performance of the system.

