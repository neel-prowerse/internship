# 20. Abstract : 
# Abstract Class : 
from abc import ABC
class Vehicle(ABC):  # inherits abstract class
    #abstract method
    def no_of_wheels(self):
        pass
class Bike(Vehicle):
    def no_of_wheels(self): # provide definition for abstract method
        print("Bike have 2 wheels")  
class Tempo(Vehicle):
    def no_of_wheels(self):  # provide definition for abstract method
        print("Tempo have 3 wheels")
class Truck(Vehicle):  # provide definition for abstract method
    def no_of_wheels(self):
        print("Truck have 4 wheels")
bike = Bike()
bike.no_of_wheels()
tempo = Tempo()
tempo.no_of_wheels()
truck = Truck()
truck.no_of_wheels()
print('\n--------------------------------------------------------------------')
