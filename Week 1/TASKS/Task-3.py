a = int(input('Enter Value of Number-1 : '))
b = int(input('Enter Value of Number-2 : '))
c = input('Enter a operation you want to do (+,-,*,/,%,**,//) : ')
if c == '+':
    d = a + b
    print('Addtion of Numbers is  : ',d)
elif c == '-':
    e = a - b
    print('Subtraction of Numbers is : ',e)
elif c == '*':
    f = a * b
    print('Multiplication of Numbers is  : ',f)
elif c == '/':
    g = a / b
    print('Division of Numbers is  : ',g)
elif c == '%':
    h = a % b
    print('Multiplication of Numbers is  : ',h)
elif c == '**':
    i = a ** b 
    print('Power of Number is : ',i)
elif c == '//':
    j = a // b
    print('Floor Division of Number is : ',j)
else : 
    print('Invalid Input !!!')