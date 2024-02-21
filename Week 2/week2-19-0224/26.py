# 26. Error Handling : 
# Basic Syntax of Error Handling : 
'''
try:
    # code that may raise an exception
except:
    # code to handle the exception. '''
# Catching Specific Exceptions in Python : 
def divideNo(a,b):
    return a/b   # An exception might raise here if b is 0 (ZeroDivisionError)
try:
    a = int(input('Enter a : '))
    b = int(input('Enter b : '))
    print('After Division : ',divideNo(a,b))
    a = [1,2,3]
    print(a[3])  # An exception will raise here as size of array ‘a’ is 3 hence is accessible only up until 2nd index
# if IndexError exception is raised
except IndexError:
    print('Index Error')
# if ZeroDivisionError exception is raised
except ZeroDivisionError:
    print('Zero Division Error')
print('\n----------------------------RAISING CUSTOM EXCEPTIONS-------------------------------')
'''
Syntax to raise an exception : 
try:
    # on some specific condition or otherwise
    raise SomeError(OptionalMsg)
Except SomeError as e:
    # Executed if we get an error in the try block
    # Handle exception e accordingly
'''
def isStringEmpty(a):
   if(type(a)!=str):
       raise TypeError('a has to be string')
   if(not a):
       raise ValueError('a cannot be null')
   a.strip()
   if(a == ''):
       return False
   return True 
try:
 a = 123
 print('isStringEmpty:', isStringEmpty(a))
except ValueError as e:
   print('ValueError raised:', e)
except TypeError as e:
   print('TypeError raised:', e)
print('\n---------------------------try except and ELSE!--------------------------------')
# try:
#     # on some specific condition or otherwise
#     raise SomeError(OptionalMsg)
# except SomeError as e:
#     # Executed if we get an error in the try block
#     # Handle exception ‘e’ accordingly
# else
#     # Executed if no exceptions are raised
try:
 b  = 10
 c = 2
 a = b/c
 print(a)
except:
 print('Exception raised')
else:
  print('no exceptions raised')
# Try Clause with Finally : 
try:
 temp = [1, 2, 3]
 temp[4]
except Exception as e:
 print('in exception block: ', e)
else:
 print('in else block')
finally:
 print('in finally block')
