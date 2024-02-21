# # 1 :
# def maxi_mini(ls):
#     minimum = min(ls)
#     maximum = max(ls)
#     print(minimum)
#     print(maximum)
# maxi_mini(['1','12','13','43','98'])

# # 2 :
# def my_list(ls):
#     ls = list(ls)
#     list1=[]
#     list2=[]
#     list3 = len(ls)/2
#     for x in range(0,len(ls)):
#         if ls[x] == len(ls)/2:
#             list1.append(ls[x])
#         else:
#             list2.append(ls[x])
#     print(list1)
#     print(list2)
# my_list([1,2,3,4])

# # 3 :
# def my_list(ls):
#     mylist=[]
#     ls = str(ls)
#     for x in ls:
#         r = ls.strip('')
#     r = list(r)
#     r.append(mylist)
#     print(r)
# my_list([' ','Neel','Abhi'])

# # 4 : 
# def swap_string_list(ls):
#     ls = list(ls)
#     temp = ls[0]
#     ls[0] = ls[-1]
#     ls[-1] = temp
#     print(ls)
# swap_string_list([1,2,3])

# # 5 :  

# # 6 : 

# # 7 :
# def my_list(ls):
#     mylist = [x ** 2 for x in ls]
#     mylist.reverse()
#     print(mylist)
# my_list([1,2,3,4])

# 8 : Remove All Occurence from the given list : 
def del_list(ls):
    ls = list(ls)
    for x in ls:
        if ls in ls:
            ls.remove()
    print(ls)
del_list([1,1,2,3,4,5])

# # 9 :
# def remove_list(ls):
#     ls = list(ls)
#     mylist = [x for x in ls if x]
#     print(mylist)
# remove_list([1,2,3,[],'hello',[]])

# # 9 : 
# def remove_list(ls):
#     ls = list(ls)
#     mylist = []
#     for x in ls:
#         if x:
#             mylist.append(x)
#     print(mylist)
# remove_list([1,2,3,[],'hello',[]])

# # 10 :
# def negative_element(ls):
#     for x in ls:
#         ls = list(ls)
#         if ls[x] <= 0:
#             filter(negative_element,ls)
#         else:
#             print('No Negative Element')
# negative_element([-1,2,3])

# # 11 :
# list1 = []
 

# #  12 : 
# def my_list(ls):
#     count1 = 0
#     count2 = 0
#     mylist1=[]
#     mylist2=[]
#     for x in ls:
#         if x % 2 == 0:
#             mylist1.append(x)
#             count1 = count1 + 1
#         else:
#             mylist2.append(x)
#             count2 = count2 + 1
#     print(f'List You Have Written : {ls}')
#     print(f'Even Elements : {mylist1}')
#     print(f'Odd Elements : {mylist2}')
#     print(f'Count Even Elements : {count1}')
#     print(f'Count Odd Elements : {count2}')
# my_list([1,2,3,4,5,6])
