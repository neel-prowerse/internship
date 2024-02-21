'''# 25. Scope : 
# Namespace and scope : 
a = 1 # namespace {a: 1}
# a now exists in the namespace
print(a) # 1
# b does not exist in the namespace yet
print(b) # => NameError: name b is not defined
b = 16
# b now exists in the namespace
print(b) # 16
print('\n-----------------------TYPES OF SCOPE----------------------------')

# E.g-1 Local Scope :
def func():
b = "I love interviewBit"
print(b) # will print the string stored in variable b 
func()
print(b) # nameError will be thrown as b exists only in func()'s local scope
'''
# E.g-2 Enclosed Scope : 
def func1():
   a = 10
   def func2():
       print(a)
   func2()
func1()

# E.g-3 Global Scope : 
a = 10
def func1():
   print("inside func1 ", a)  # as a does not exist in the local scope of func1(), according to the LEGB rule, the interpreter looked into the global scope 
func1()
print("at local global scope ", a)
'''
# E.g-4 BuiltIn Scope : 
from math import pi
def func1():
   print('inside func1 ', pi)
pi = 10     don't do this, it will redefine the builtin identifier, as then the builtin value won't be read, and redefined value will be read
print('at global scope ', pi)
func1()
'''

# nonlocal keyword : 
def func1():
   a = 10
   def func2():
       nonlocal a
       print('func2 ', a)
   func2()
   print('func1 ', a)
func1()

# global keyword:
a = 10
def func1():
   global a
   a = 20
   print("inside func1 ", a) # as a does not exist in the local scope of func1(), according to the LEGB rule, the interpreter looked into the global scope 
print("global-1 ", a)
func1()
print("global-2 ", a)
