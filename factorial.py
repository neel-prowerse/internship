n = int(input('Enter A Number : '))
fact = 1
if n == 0:
    print('Factorial of 0 is 1 !')
elif n > 0:
    for i in range(2,n+1):
        fact = fact * i
    print(f'Factorial : {fact}')
else:
    print('Enter Number greater than 0 !')    