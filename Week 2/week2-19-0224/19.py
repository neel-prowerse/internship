# 19. Data Encapsulation : 
# Getter and Setter : 
class Library:
    def __init__(self, id, name):
        self.bookId = id
        self.bookName = name
    def setBookName(self, newBookName): #setters method to set the book name
        self.bookName = newBookName
    def getBookName(self): #getters method to get the book name
        print(f"The name of book is {self.bookName}")
book = Library(101,"The Witchers")
book.getBookName()
book.setBookName("The Witchers Returns")
book.getBookName()
print('\n-------------------------------------------------------------------------')
# Access Modifiers Private, Public and Protected : 
class Employee:
    def __init__(self, name, employeeId, salary):
        self.name = name    #making employee name public
        self._empID = employeeId  #making employee ID protected
        self.__salary = salary  #making salary private
    def getSalary(self):
        print(f"The salary of Employee is {self.__salary}")
employee1 = Employee("Neel", 1, "$150000")
print(f"The Employee's name is {employee1.name}")
print(f"The Employee's ID is {employee1._empID}")
employee1.getSalary() #will be able to access the employee's salary now using the getter method

