# 30. List Comprehension : 
# Simple Syntax : mylist=[output for item in iterable if condition == True] 
mylist = [x for x in range(6) if x%2==0]
print(mylist)
print('\n----------------------------------------------------------')

# Example of Simple List Comprehension : 
# E.g-1 Simple Loop : 
def simple_list_compre(ls):
    mylist = [i for i in ls]
    print(f"My List is : {mylist}")
simple_list_compre([1,2,3,4,5])
print('\n----------------------------------------------------------')

# E.g-2 Adding Conditions : 
def simple_list_com_con(ls):
    mylist = [i for i in ls if i%2==0]
    print(f"List with even numbers  : {mylist}")
simple_list_com_con([1,2,3,4,5,6,7,8,9,10])
print('\n----------------------------------------------------------')

# Sqaure of Output : 
def simple_list_sqrt(ls):
    mylist = [i**2 for i in ls if i%2==0]
    print(f"Sqaure of Even Number : {mylist}")
simple_list_sqrt([1,2,3,4,5,6,7,8,9,10])
print('\n----------------------------------------------------------')

# List Comprehension with Nested For Loop : 
def nested_loop_com(ls):
    list1 = [[i for i in j] for j in ls]
    print("Nested List : ",ls)
    list2 = [j for i in ls for j in i]
    print("Normal List : ",list2)
nested_loop_com([[1,2,3,4],[5,6,7],[8,9,10]])
print('\n----------------------------------------------------------')

# Equivalent Code : 
def nestedloop(ls):
    ls1, ls2 = [], []    
    for i in ls:
        temp = []
        for j in i:
            temp.append(j)
        ls1.append(temp)
    print("Nested list: ",ls)
    for i in ls:
        for j in i:
            ls2.append(j)
    print("Normal list: ",ls2)
nestedloop([[1,5,6,7],[8,9,10],[11,12]])  
print('\n----------------------------------------------------------')

# List Comprehension with if...else condition : 
def nested_if_else(ls):
    result = [a+10 if a<10 else a+5 for a in ls]
    print("Result : ",result)
nested_if_else([1,2,3,4,5,6,7,8,9,11,12,15])
print('\n----------------------------------------------------------')

# List Comprehension with if...elif...else condition : 
def nested_if_elif(ls):
    result = [a*2 if a<10 else a**2 if not a%2 else a+5 for a in ls]
    print("Result : ",result)
nested_if_elif([1,2,3,4,5,6,7,8,9,11,12,15])
print('\n----------------------------------------------------------')

# Equivalent Code : 
def nested_if_else(ls):
    #nested if else condition
    result = []
    for a in ls:
        if a < 10:
            result.append(a*2)
        elif not a % 2:
            result.append(a**2)
        else:
            result.append(a+5)
    print("Our result is: ",result)
#driver code
nested_if_elif([1,2,3,4,5,6,7,8,9,11,12,15])
print('\n----------------------------------------------------------')

# Using Walrus Operator : 
# Syntax : name:=expression
import random
def record_year():
    return random.randrange(2000,2024)
def walrus():
    records = [rec for i in range(10) if (rec:=record_year())>=2010]
    print(records)
walrus()
print('\n----------------------------------------------------------')

# String Using List Comprehension : 
def list_comprehension(str):
    ls1 = [a for a in str]
    print("First List : ",ls1)
    ls2 = [a for a in str if a.lower() in 'aeiou']
    print('Second List : ',ls2)
    ls3 = ["|" + a + "|" for a in str]
    print("Third List : ",ls3)
list_comprehension("Python")
print('\n----------------------------------------------------------')

# 2. Dict Comprehension : 
# Simple Syntax : {key:value for (key,value) in dict.items() if condition}
# Simpke Merging : NewDict={key:value for(key,value)in iterable}
# Conditional Merging : NewDict={key:value for list in ie=terable if(condition)}
newdict = {x: x**2 for x in range(10) if x**2%2==0}
print(newdict)
print('\n----------------------------------------------------------')

#If Condiontinal Dictionary Comprehension : 
stock_dict = {'Apple':5,'Mango':6,'Banana':13, 'Grapes':10}
refil_dict = {k:v for (k,v) in stock_dict.items() if v <10}
print(refil_dict)
print('\n----------------------------------------------------------')

# Multiple if-else Conditional Dictionary Comprehension :
age_dict = {'Abhi':21,'Neel':20,'Kush':17,'Prem':22}
new_dict = {k:(f"{v} - Applicable" if v>=18 else f"{v} - Not Applicable") for (k,v) in age_dict.items()}
print(new_dict)