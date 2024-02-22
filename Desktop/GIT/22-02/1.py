# 1 :
print('\n-------------------------Task-1---------------------------')
def small_large(ls):
    ls = list(ls)
    minimum = min(ls)
    maximum = max(ls)
    print(f'Minimum Number in The List : {minimum}')
    print(f'Maximum Number in The List : {maximum}')
small_large([1,2,98,32])
print('\n-------------------------Task-2---------------------------')

# 2 :
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
split1 = []
split2 = []
for i in range(0,len(list1)//2):
    split1.append(list1[i])
for j in range((len(list1)//2),len(list1)):
        split2.append(list1[j])
print(f'Splitted List - 1 : {split1}')
print(f'Splitted List - 2 : {split2}')
print('\n-------------------------Task-3---------------------------')

# 3 :
mylist = ['','Neel','','Abhi','']
mylist2 = filter(None,mylist)
mylist3 = list(mylist2)
print(f'Removing Empty String From the Given List : {mylist3}')
print('\n-------------------------Task-4---------------------------')

# 4 : 
def swapping(ls):
    ls = list(ls)
    temp = ls[0]
    ls[0] = ls[-1]
    ls[-1] = temp 
    print(f'Swapping of First and Last Element in the List : {ls}')
swapping([1,2,3,4])
print('\n-------------------------Task-5---------------------------')

# 5 :  
mylist = [1,2,3,3,3,2,2,1,4,4,5,6,7,8,8,8]
k = 2
mylist2 = []
for i in mylist:
    freq = mylist.count(i)
    if((freq > k) and i not in mylist2):
        mylist2.append(i)
print(f'Elements with Frequencyv greater than K : {mylist2}')
print('\n-------------------------Task-6---------------------------')

# 6 : 
list1=[1,2,3]
list2=[]
for i in list1:
    list2.append([i])
    for j in range(0,len(list1)):
        for k in range(i+1,len(list1)):
            list2.append([list1[j],list1[k]])
list2.append(list1)
print(f'Possible Combinations of a List : {list2}')
print('\n-------------------------Task-7---------------------------')

# 7 :
def my_list(ls):
    ls = list(ls)
    mylist = [x ** 2 for x in ls ]
    print(f'Square of Each Element in the Given List : {mylist}')
my_list([1,2,3,4])
print('\n-------------------------Task-8---------------------------')

# 8 : Remove All Occurence from the given list : 
list1 = [1,1,1,3,3,34,56,6,7,8]
for i in list1:
     count = list1.count(i)
     if count > 1:
          while i in list1:
               list1.remove(i)
print(f'Removing All Occurrences of an Element From The List : {list1}')
print('\n-------------------------Task-9---------------------------')

# 9 :
def remove_list(ls):
    ls = list(ls)
    mylist = [x for x in ls if x]
    print(f'Remove Empty List from the Given List : {mylist}')
remove_list([1,2,3,[],'hello',[]])
print('\n-------------------------Task-9---------------------------')

# 9 : 
def remove_list(ls):
    ls = list(ls)
    mylist = []
    for x in ls:
        if x:
            mylist.append(x)
    print(f'Remove Empty List from the Given List : {mylist}')
remove_list([1,2,3,[],'hello',[]])
print('\n-------------------------Task-10---------------------------')

# 10 :
mylist=[1,2,3,-4,-5,6,7,8,-9]
def negative(ls):
    return ls > 0
list1=list(filter(negative,mylist))
print(f'Filtered List Removed Negative Element : {list1}')
print('\n-------------------------Task-11---------------------------')

# 11 :
def flatten(ls):
    mylist=sum(ls,[])
    print(f'Flatten List using buit-in Function : {mylist}')
flatten([[1,2,3],[5,6,7],[8,9,10]])
print('\n-------------------------Task-12---------------------------')

#  12 : 
def odd_even(ls):
    count1 = 0
    count2 = 0
    mylist1 = []
    mylist2 = []
    for i in ls:
        if i % 2 == 0:
            count1 = count1 + 1
            mylist1.append(i)
        else:
            count2 = count2 + 1
            mylist2.append(i)
    print(f'Even Elements in the List : {mylist1}')
    print(f'Even Element Count : {count1}')
    print(f'Odd Elements in the List : {mylist2}')
    print(f'Odd Element Count : {count2}')
odd_even([1,2,3,4,5,6,7,8,9,10])
print('\n----------------------------------------------------------')