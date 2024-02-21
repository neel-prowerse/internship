import re 
text = '''Alan Turing was a pioneer of theoritical computer science and artificial intelligence. He was born on 23 June 1912 in Maida Vale, London'''
res = re.search('^Alan.*London$',text)
if(res):
    print('We have a Match!')
else:
    print('We don\'t have a match')
import re
text = '''Alan Turing was born on 23 June 1912 in London.'''
# Example for \A
res = re.findall('\AAlan',text)
print("Result for \A = ", res)
print("-"*79)
# Example for \b
res = re.findall(r'\bLon',text)
print("Result for \\b = ", res)
print("-"*79)
# Example for \b
res = re.findall(r'ring\b',text)
print("Result for \\b = ", res)
print("-"*79)
# Example for \B
res = re.findall('\Bon',text)
print("Result for \B = ", res)
print("-"*79)
# Example for \d
res = re.findall('\d',text)
print("Result for \d = ", res)
print("-"*79)
# Example for \D
res = re.findall('\D',text)
print("Result for \D = ", res)
print("-"*79)
# Example for \s
res = re.findall('\s',text)
print("Result for \s = ", res)
print("-"*79)
# Example for \S
res = re.findall('\S',text)
print("Result for \S = ", res)
print("-"*79)
# Example for \w
res = re.findall('\w',text)
print("Result for \w = ", res)
print("-"*79)
# Example for \W
res = re.findall('\W',text)
print("Result for \W = ", res)
print("-"*79)
# Example for \Z
res = re.findall('London.\Z',text)
print("Result for \Z = ", res)
'''
Output:
Result for \A =  ['Alan']
Result for \b =  ['Lon']
Result for \b =  ['ring']
Result for \B =  ['on', 'on']
Result for \d =  ['2', '3', '1', '9', '1', '2']
Result for \D =  ['A', 'l', 'a', 'n', ' ', 'T', 'u', 'r', 'i', 'n', 'g', ' ', 'w', 'a', 's', ' ', 'b', 'o', 'r', 'n', ' ', 'o', 'n', ' ', ' ', 'J', 'u', 'n', 'e', ' ', ' ', 'i', 'n', ' ', 'L', 'o', 'n', 'd', 'o', 'n', '.']
Result for \s =  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
Result for \S =  ['A', 'l', 'a', 'n', 'T', 'u', 'r', 'i', 'n', 'g', 'w', 'a', 's', 'b', 'o', 'r', 'n', 'o', 'n', '2', '3', 'J', 'u', 'n', 'e', '1', '9', '1', '2', 'i', 'n', 'L', 'o', 'n', 'd', 'o', 'n', '.']
Result for \w =  ['A', 'l', 'a', 'n', 'T', 'u', 'r', 'i', 'n', 'g', 'w', 'a', 's', 'b', 'o', 'r', 'n', 'o', 'n', '2', '3', 'J', 'u', 'n', 'e', '1', '9', '1', '2', 'i', 'n', 'L', 'o', 'n', 'd', 'o', 'n']
Result for \W =  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.']
Result for \Z =  ['London.']
'''
print('\n------------------------findall()------------------------------')
import re
text = '''Alan Turing was a pioneer of theoretical computer science and artificial intelligence. He was born on 23 June 1912 in Maida Vale, London'''
res = re.findall('Turing',text)
print("Result = {}".format(res))
# Output: Result = ['Turing']
print('\n------------------------search()------------------------------')
import re
text = '''Alan Turing was a pioneer of theoretical computer science and artificial intelligence. He was born on 23 June 1912 in Maida Vale, London'''
res = re.search('Turing',text)
print("Result = {} and start,end position = {}".format(res,res.span()))
# Output: Result = <re.Match object; span=(5, 11), match='Turing'> and start,end position = (5, 11)
print('\n------------------------split()------------------------------')
import re
text = '''Alan Turing was a pioneer of theoretical computer science and artificial intelligence. He was born on 23 June 1912 in Maida Vale, London'''
res = re.split("a", text)
print("Result = {}".format(res))
# Output: Result = ['Al', 'n Turing w', 's ', ' pioneer of theoretic', 'l computer science ', 'nd ', 'rtifici', 'l intelligence. He w', 's born on 23 June 1912 in M', 'id', ' V', 'le, London']
print('\n----------------------sub()------------------------')
import re
text = '''Alan Turing was a pioneer of theoretical computer science and artificial intelligence. He was born on 23 June 1912 in Maida Vale, London'''
res = re.sub('theoretical','practical',text)
print("Result = {}".format(res))
# Output: Result = Alan Turing was a pioneer of practical computer science and artificial intelligence. He was born on 23 June 1912 in Maida Vale, London
print('\n----------------------Match Object--------------------------------')
import re
text = '''Alan Turing was a pioneer of theoretical computer science and artificial intelligence. He was born on 23 June 1912 in Maida Vale, London'''
# Searches the pattern in the string.
res = re.search('computer',text)
print("Match object = {}".format(res))
print("--"*30)
print("group method output = ",res.group())
print("--"*30)
print("start method output = ",res.start()) 
print("--"*30)
print("end method output = ",res.end())
print("--"*30)
print("span method output = ",res.span()) 
print("--"*30)
print("re attribute output = ",res.re)
print("--"*30)
print("string attribute output = ",res.string)
print("--"*30)
# Example of using r as prefix.
# Searching for \\ in the following string
text = r'search \\ in this string'
# searching using r as prefix
res = re.search(r"\\",text)
print("With r as prefix = ",res)
'''
Output:
Match object = <re.Match object; span=(41, 49), match='computer'>
group method output =  computer
start method output =  41
end method output =  49
span method output =  (41, 49)
re attribute output =  re.compile('computer') 
string attribute output =  Alan Turing was a pioneer of theoretical computer science and artificial intelligence. He was born on 23 June 1912 in Maida Vale, London
With r as prefix =  <re.Match object; span=(7, 8), match='\\'>
'''
