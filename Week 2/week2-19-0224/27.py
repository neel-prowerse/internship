# 27. String Formatting 
# String Formatting using the format() Method : 
myCode = 1110
myName = "Neelraj"
myStr = 'Code of {} is {}'.format(myName,myCode)
print(myStr)
print('\n----------STRING FORMATTING USING .format() WITH POSITIONAL ARGUMENT ----------')
# String Formatting using the format() with positional arguments : 
myId = 110
myName = 'Neelraj'
myVar = 12345
myStr = 'Variable is {2} and code of {0} is {1}'.format(myName,myId,myVar)
print(myStr)
print('\n--------------NUMBER FORMATTING USING FORMAT()----------------')
myNum = -1234
myStr = 'Number is : {}'.format(myNum) 
myStr2 = 'Left Aligned Number with length 10 is {:<10}.'.format(myNum)
myStr3 = 'Right Aligned Number with length 10 is {:>10}.'.format(myNum)
myStr4 = 'Center Aligned Number with length 10 is {:^10}.'.format(myNum)
print(myStr)
print(myStr2)
print(myStr3)
print(myStr4)
print('\n--------TRUNCATING STRING USING FORMAT() IN PYTHON-------------')
myString = 'Neelraj'
myStr = 'Truncated String with length 3 is :  {:.3}'.format(myString)
print(myStr)
print('\n--------PADDING STRING USING THE FORMAT()---------------')
myString = 'Hello World!'
myStr5 = "Padded String with string on left and length 20 is : {:*<20}".format(myString)
myStr6 = "Padded String with string on right and length 20 is : {:*>20}".format(myString)
myStr7 = "Padded String with string on center and length 20 is : {:*^20}".format(myString)
print(myStr5)
print(myStr6)
print(myStr7)
print('\n------------FORMATTING CLASS MEMBER USING THE FORMAT()-------------------')
class Website:
    def __init__(self):
        self.name = "Neel"
website = Website()
myStr8 = 'Padded Website name with name on center and length 20 is : {:*^20}'.format(website.name)
print(myStr8)
print('\n------------   dynamic formatting using format()--------------------------')
myString = 'Neel'
length = 20
myStr = "Dynamically Right Aligned String is: {:>{}}.".format(myString, length)
print(myStr)
myStr = "Dynamically Center Aligned String is: {:^{}}.".format(myString, length)
print(myStr)
myStr = "Dynamically Padded String with input on left is: {:*<{}}.".format(myString, length)
print(myStr)
myStr = "Dynamically Padded string with input on right is: {:*>{}}.".format(myString, length)
print(myStr)
myStr = "Dynamically Padded string with input on center is: {:*^{}}.".format(myString, length)
print(myStr)
myStr = "Dynamically truncated String with output length 3 is: {:.{}}.".format(myString, 3)
print(myStr)



