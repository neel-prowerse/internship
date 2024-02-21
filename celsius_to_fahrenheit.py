user = input('Enter C or F : ')
user1 = user.upper()
if (user1 == 'C'):
    c = int(input('Enter Celsius :  '))
    f = (9/5 * c) + 32
    print(f'Fahrenheit : {f}')
elif (user1 == 'F'):
    f = int(input('Enter Fahrenheit : '))
    c = (f - 32) * 5/9 
    print(f'Celsius : {c}')
else:
    print("Invalid Input Write Either C or F Only ! ")