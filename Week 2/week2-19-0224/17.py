#17. Arrays and Classes : 
#(i) Arrays : It is same as List.
cars = ['BMW','Audi','Volvo']
print(f'Accessing the element through their index : {cars[0]}')
x = cars[0] = 'GTR'
print(f'Replacing the element through their index : {cars}')
print(f'Length of the Cars Array : {len(cars)}') 

# Printing the Elements through Loops : 
for x in cars:
    print(f'Accessing the Element through a Loop : {x}')

# Adding the elements in Array : 
cars.append('Mercedes')
print(f'Adding the element using append Method : {cars}')

# Removing the elements in Array : 
cars.remove('Audi')
print(f'Using Remove Method : {cars}')
cars.pop(1)
print(f'Using Pop Method : {cars}')
print('\n\n-----------------------------------------Classes---------------------------------------------------')
#(ii) Classes : 
# Creating a class :
class Car:
    car = ['BMW','Audi','Volvo']
p1 = Car()
print(p1.car)

# The __init__ Function : 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person('Neel',19)
print(f"Name : {p1.name},\nAge : {p1.age}")

# The __str__ Function : 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return  f"Name is {self.name}, \nAge is {self.age}"
p1 = Person('Neel',19)
print(p1)

# Object Methods : 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print(f'Hello, My Name is {self.name}')
p1 = Person('Neel', 19)
p1.myfunc()
print('----------------------------------------------------------------------')
# We can write any name instead of self, but we just have to add it to function.
class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("Neel", 19)
p1.myfunc()
