# 1. Check if a Given Key Already Exists in Dictionary : 
mydict = {'first_name':'Neelraj','age':20,'height':5.8,'gender':'Male'}
def check_key(ds):
    if ds in mydict:
        print('YES, It\'s already exists in dictionary.')
    else:
        print('NO!, It\'s not present in dictinary.')
check_key('first_name')
check_key('weight')

# 2. Handle Missing Keys in Dictionary : 
mydict = {'first_name':'Neelraj','age':20,'height':5.8,'gender':'Male'}
print(mydict.get('name','Not Present'))
print(mydict.get('first_name','Not Present'))

# 3. Extract Unique Values in a Given Dictionary  :
mydict = {
            'list1':[1,2,3,4,5],
            'list2':[6,7,8,9,10],
            'list3':[15,14,13,12,11],
            'list4':[20,19,18,17,16]
         }
uniqueval = list(sorted({j for i in mydict.values() for j in i}))
print('The Unique Values are : ',uniqueval)

# 4. Print the sum of the key values pairs in a Given Dictionary : 
mydict = {2:8,5:20,3:15}
sum_dict = []
for key in mydict:
    sum_dict.append(key + mydict[key])
print('Sum of the Key-Values pair in Dictionary : ',list(sum_dict))

# 5. Replace Dictionary Values From Other Dictionary : 
mydict = {'first_name':'Neelraj','age':19,'height':5.8,'gender':'Male'}
mydict2 = {'age':20,'city':'Ahmedabad'}
for key in mydict:
    if key in mydict2:
        mydict[key] = mydict2[key]
print('The Original Dictionary : ' + str(mydict))
print('The Updated Dictionary : ' + str(mydict2))

# 6. Update or Change the Keys in A Given Dictionary : 
# 1. Using Assignment Operator.
# 2. Using pop() method.
# 3. Usingb zip() method.
mydict={'first_name':'Neelraj','age':20,'height':5.8,'gender':'Male'}
print('The Original Dictionary : ', mydict)
# Using Assignment Operator : 
mydict['height']=mydict['age']
del mydict['height']
print('Dictionary After Changing Key Using Assignment Operator : ',str(mydict))
# Using Pop() Method : 
mydict['first_name']=mydict.pop('age')
print('Dictionary After Changing Key Using Pop Method : ',str(mydict))
# Using Zip() Method :
new_key=['last_name','weight','college']
final_dict=dict(zip(new_key,list(mydict.values())))
print('Dictionary After Changing All Keys Using Zip() Method : ',str(final_dict))

# 7. Delete a List Keys in a Given Dictionary : 
mydict = {'Neel':20,'Bhagyaraj':18,'Abhi':22}
keys = ['Neel','Bhagyaraj']
for k in keys:
    mydict.pop(k)
print(mydict)

# 8. Change the Value of a Key in Nested Dictionary  :
mydict = {'emp1':{'name':'Neel','age':20,'job':'Python Developer'},
          'emp2':{'name':'Abhi','age':22,'job':'Python Developer'}, 
          'emp3':{'name':'Bhagyaraj','age':18,'job':'Student'}
         } 
print("Original Employees Dictionary : ",mydict)
mydict['emp2']['age'] = 20
print('Updated Employee Dictionary : ',mydict)

# 9. Map Two Lists into a Dictionary  : 
keys = ['first_name','age','height']
values = ['Neel',20,5.8]
mydict=dict(zip(keys,values))
print(mydict)

# 10. Check if the Given Dictionary is Empty or not : 
mydict={}
if mydict=={}:
    print('The Dictiopnary is Empty')
else:
    print('The Dictionary is Not Empty')

# 11. Get Keys with Maximum and Minimum Values in a Dictionary : 
mydict={'Neel':20,'Abhi':22,'Bhagyaraj':18}
print('The Maximum Value of the given Dictionary : ',max(mydict.values()))
print('The Minimum Value of the Given Dictionary : ',min(mydict.values()))

# 12. Check if the substring matches any key in a dictionary : 
mydict = {'Neelraj':20,'Abhi Pro':22,'Bhagyaraj':18}
search_string = 'Pro'
print('The Actual Dictionary : ',str(mydict))
search_str = dict(filter(lambda item:search_string in item[0],mydict.items()))
print('The Key-Value Pair For Search Keys : ',str(search_str))

# 13. Get a Key From Value in a Dictionary : 
mydict={'Neel':20,'Abhi':22,'Bhagyaraj':18}
def get_key(dict_value):
   for dict_key, value in mydict.items():
        if dict_value == value:
            return(dict_key)
   return ('Key doesn\'st Exist')
print('Get Key of Value 40 : ',get_key(40))
print('Get Key Of Value 20 : ',get_key(20))

# 14. Sort a Given Dictionary by keys :
mydict={'Neel':20,'Abhi':22,'Bhagyaraj':18}
sorted_dict = sorted(mydict.values())
print(sorted_dict)
