n = int(input('Enter A Number : '))
arm = len(str(n))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** arm
    temp = temp // 10
if sum == n:
    print(f'{n} is Armstrong Number ')
else:
    print(f'{n} is not Armstrong Number ')