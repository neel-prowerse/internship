#1.
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before Function Call")
        result = func(*args, **kwargs)
        print("After Function Call")
        return result
    return wrapper
@my_decorator
def greet(name):
    print('HELLO, ' + name)
greet("NEEL")
print('\n-----------------------------------------------------------')


#2.
def my_decorator(num):
    def decorators(func):
        def wrapper(*args, **kwargs):
            print("Before Function Call")
            result = func(*args, **kwargs)
            print("After Function Call")
            print("Result : ", result * num )
        return wrapper
    return decorators
@my_decorator(2)
def greet(name):
    return "HELLO, " + name
greet("NEEL")
print("\n-----------------------------------------------------------")


#3. 
class MyClass:
    def __init__(self, value):
        self.value = value
    @my_decorator
    def my_method(self):
        return self.value
obj = MyClass(3)
print(obj.my_method())
