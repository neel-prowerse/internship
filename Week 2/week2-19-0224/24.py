# 24. Modules : 
import example
name = 'Neel'
example.print_name(name)
print('\n------------------------CALLING MODULES---------------------------------')
''' Types of Python Modules : 

1. Inbuilt modules in Python
2. User-Defined Modules in Python

1. Inbuilt modules : 
(i) math
(ii) sys
(iii) os
(iv) random and many more.
'''
# Calling an Inbuilt Modules : 
import math # this is a math module
import random # this is a random module
# now, we use some of the math and random module function to check whether the modules are working or not.
cos30 = math.cos(30)
tan10 = math.tan(10)
pie = math.pi
# now, using the random module to generate some random numbers
random_int = random.randint(0,20)
print(f"Value of cos30 is: {cos30}")
print(f"Value of tan10 is: {tan10}")
print(f"Value of pie is: {pie}")
print(f"The random number generated using random int function: {random_int}")
print('\n----------------------(USER-DEFINED)VARIABLES IN PYTHON-------------------------------')
import variable
fact_of_6 = variable.factorial(6)
power_of_6 = variable.power[6]
alphabet_2 = variable.alphabets[1]
print(f'The Factorial of 6 is {fact_of_6}') 
print(f'The Power of 6 is {power_of_6}') 
print(f'The Second Alphabet is {alphabet_2}') 
print('\n------------------------ANOTHER WAY TO IMPORT---------------------------------')
from math import sqrt, factorial,pi
print(sqrt(9))
print(factorial(9))
print(pi)
print('\n----------------------PYTHON MODULES SEARCH PATH-------------------------------')
import sys
print(sys.path)
print('\n----------------------RENAMING A MODULE----------------------------------------')
import pandas as pd
import random as r
print('Pandas:',pd.__version__)
print('Random:',r.randint(0,10))
print('\n-----------------------RELOADING A MODULE--------------------------------------')
import variable
import imp
imp.reload(variable)
print('\n-----------------------THE dir() BUILT-IN FUNCTION-------------------------------')
import math
print(dir(math))
