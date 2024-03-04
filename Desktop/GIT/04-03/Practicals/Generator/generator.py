# Generator :  They are a powerful tool in Python that allows you to generate values on the fly without having to store them all in the memory at once. You can create a generator using a generator function, which is a function that contains one or more 'yield' statements. Generators are useful for iterating over large or infinite sequences without having to store all of the values in memory at once. 
#1. 
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
for value in simpleGeneratorFun():
    print(value)
print('\n---------------------COUNT TO TEN--------------------------')


#2. 
def count_to_ten():
    for i in range(10):
        yield i
gen = count_to_ten()
for i in gen:
    print(i)
print('\n-----------------------Prime Numbers-----------------------')


#3.
def primes():
    yield 2
    n = 3
    while True:
        for i in range(2, int(n**0.5)+1):
            if n % i:
                break
            else:
                yield n
            n = n +2
gen = primes()
for i in gen:
    if i > 100:
        break
    print(i)
