# 18. Object Oriented Programming Concepts (OOPs) : 
class Human:
    species = 'Homo Sapiens'    #Class Attribute
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
x = Human('Neel',19,'Male')     #Class Object-1
y = Human('Abhi',22,'Male')     #Class Object-2
print(x.name)
print(y.name)
print('\n-----------------------------------------')
print(x.species)
print(y.species)
print(f'HELLO! My Name is {x.name}.I am {x.age} years old and my Gender is {x.gender}.')
print(f'HELLO! My Name is {y.name}.I am {y.age} years old and my Gender is {y.gender}.')
print('\n------------------------------------------------------------')
class Human:
    #class attribute
    species = "Homo Sapiens"
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    #Instance Method
    def speak(self):
        return f"Hello everyone! I am {self.name}"
    #Instance Method
    def eat(self, favouriteDish):
        return f"I love to eat {favouriteDish}!!!"
x = Human("Neel",19,"Male")
print(x.speak())
print(x.eat("apple"))

    