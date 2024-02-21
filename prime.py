n = int(input('Enter A Number : '))
if n > 1:
    for i in range(2, int(n/2)+1):
        if(n % i) == 0:
            print(f'{n} is Not Prime Number')
            break
        else:
            print(f'{n} is Prime Number')
else:
    print(f'{n} is not Prime Number')
