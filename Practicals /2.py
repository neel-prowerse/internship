# 1 : 
def swap_string_list(ls):
    ls = list(ls)
    temp = ls[0]
    ls[0] = ls[-1]
    ls[-1] = temp
    print(ls)
swap_string_list([1,2,3])

# 2 :
def swap_string_list(ls):
    ls = list(ls)
    temp = ls[0]
    ls[0] = ls[1]
    ls[1] = temp
    print(ls)
swap_string_list([1,2,3])

# 3 :
def swap_string_list(ls):
    ls = list(ls)
    temp = ls[0]
    ls[0] = ls[-1]
    ls[-1] = temp
    print(ls)
swap_string_list(['Neel','Abhi'])

# 4 : 
def mylist(ls):
    print(len(ls))
mylist([1,2,3,'str'])

# 5 : 
n1 = int(input('Enter Number - 1 : '))
n2 = int(input('Enter Number - 2 : '))
if  n1 > n2:
    print(f'{n1} is max than {n2}')
else:
    print(f'{n2} is max than {n1}')

# 6 : 
n1 = int(input('Enter Number - 1 : '))
n2 = int(input('Enter Number - 2 : '))
if  n1 < n2:
    print(f'{n1} is min than {n2}')
else:
    print(f'{n2} is min than {n1}')
 
# 7 : 
def check_element_list(ls):
    mylist = [1,2,3,4,5]
    if ls in mylist :
            print('Element Present in List')
    else:
            print('Element Not Found !')
check_element_list(6)
