s1 = input('Enter String - 1 : ')
s2 = input('Enter String - 2 : ')
list1 = list(s1)
list2 = list(s2)
list1.sort()
list2.sort()
position = 0
matches = True
while position < len(s1) and matches:
    if list1[position] == list2[position]:
        position = position + 1 
    else:
        matches = False
print(f'{s1} and {s2} is {matches}')