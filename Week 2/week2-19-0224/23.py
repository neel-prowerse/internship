# 23. Iterators : 
# iter() : 
mySecret = ['My','Name','is','Neelraj']
myiter = iter(mySecret)
print(myiter)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print('\n-----------------------LOOPING THROUGH AN ITERATOR-------------------------------')
nums = [1,2,3,4,5]
for i in nums : 
    print(i)
print('\n------------------------CREATE AN ITERATOR-------------------------------')
class Myiter:
    def __init__(self, max = 0):
        self.max = max
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n <= self.max:
            result = self.n % 2
            self.n +=1
            return result
        else:
            raise StopIteration
numbers = Myiter(3)
i = iter(numbers)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print('\n-------------------------PYTHON INFINTE ITERATORS---------------------------')
class InfiniteIterator:
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        result = self.n * 2
        self.n += 1
        return result
multipleOfTwo = InfiniteIterator()
i = iter(multipleOfTwo)
print('Multiple of two are : ')
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))