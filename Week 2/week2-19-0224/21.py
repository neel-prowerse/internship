# 21. Polymorphism : 
# (i) Inbuilt Polymorphic Functions : 
print(len('deepa'))
print(len([1,2,5,9]))
print(len({'1':'apple','2':'cherry','3':'banana'}))
print('\n--------------------------POLYMORPHISMI WITH CLASS-----------------------------')

# (ii) Polymorphism with Class Method : 
class Monkey:
    def color(self):
        print("The monkey is yellow coloured!")
    def eats(self):
        print("The monkey eats bananas!")
class Rabbit:
    def color(self):
        print("The rabbit is white coloured!")
    def eats(self):
        print("The rabbit eats carrots!")
mon = Monkey()
rab = Rabbit()
for animal in (mon, rab):
    animal.color()
    animal.eats()
print('\n-------------------------POLYMORPHISM WITH INHERITANCE---------------------------------')

# (iii) Polymorphism with Inheritance :
class Shape:
    def no_of_sides(self):
        pass
    def two_dimensional(self):
        print("I am a 2D object. I am from shape class")
class Square(Shape):
    def no_of_sides(self):
        print("I have 4 sides. I am from Square class")
class Triangle(Shape):
    def no_of_sides(self):
        print("I have 3 sides. I am from Triangle class")
# Create an object of Square class
sq = Square()
# Override the no_of_sides of parent class
sq.no_of_sides()
# Create an object of triangle class
tr = Triangle()
# Override the no_of_sides of parent class
tr.no_of_sides()
