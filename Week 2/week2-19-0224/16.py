#(i) Function : 
# Creating and calling a function :
def my_function():
    print('Hello World !')
my_function()

# Arguments : 
def my_function(fname):
    print(fname + ' is a good boy.')
my_function('Neel')
my_function('Abhi')

# Number of Arguments : 
def my_function(fname,lname):
    print(fname + " " +lname)
my_function("Neelrajsinh","Zala")

# Arbitrary Argument (*args) : 
def my_function(*kids):
    print("The Youngest Child is " + kids[2])
my_function('Neel','Abhi','Kush')

# Passing a List as an Argument : 
def my_function(food):
    for x in food:
        print(x)
fruits = ['apple','banana','cherry']
my_function(fruits)

# Returning a Value in Function : 
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(4))
print(my_function(5))

# Positional-Only Argument : 
def my_function(x,/):
    print(x)
my_function(3)

#Keyword-Only Argument : 
def my_function(*,x):
    print(x)
my_function(x = 3)

# Combining Keyword and Positional Argument : 
def my_function(a,b,/,*,c,d):
    print(a + b + c + d)
my_function(5,6,c = 7,d = 8)

# Recursion in a function : 
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print('\n\nRecursion Example Results  : ')
tri_recursion(5)
print('----------------(ii) Lambda-----------------------')
# (ii) Lambda : 
# E.g-1 :
x = lambda a : a + 10
print(x(5))

# E.g-2 : 
x = lambda a,b : a * b
print(x(5,6))

# E.g-3 : 
x = lambda a, b, c : a + b + c
print(x(5,6,2))

# E.g-4 :
def my_func(n):
    return lambda a : a * n
mydoubler = my_func(2)
print(mydoubler(5))