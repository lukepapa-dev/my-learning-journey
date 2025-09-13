# Manipulating Strings

# Sting concatentation
a = "Hello"
b = "World"
c = a + " " + b # Concatenate with space in between
print(c)  # Output: Hello World


# Using n as a logical operator
fruit = 'banana'
if 'a' in fruit:
    print("Found an 'a' in", fruit)

'n' in fruit  # Evaluates to True
'z' not in fruit  # Evaluates to True


# String comparison
if 'apple' < 'banana': # True because 'a' comes before 'b'
    print('apple is less than banana')
if 'apple' == 'Apple': # False because of case sensitivity
    print('apple is equal to Apple')
if 'apple' > 'Apple': # True because lowercase letters have higher ASCII values than uppercase
    print('apple is greater than Apple')
if 'apple' < 'Banana': # False because 'a' comes after 'B' in ASCII
    print('apple is less than Banana')


# String methods
greet = 'Hello Bob'
zap = greet.lower()  # Converts to lowercase
print(zap)  # Output: hello bob
print(greet)  # Original string remains unchanged: Hello Bob
print('Hi There'.lower())  # Output: hi there
print('Hello Bob'.upper())  # Output: HELLO BOB
print('Hello Bob'.isupper())  # Output: False
print('HELLO BOB'.isupper())  # Output: True
print('Hello Bob'.startswith('H'))  # Output: True
print('Hello Bob'.startswith('h'))  # Output: False


# if you use dir() function on a string, it will show you all the methods available for string objects
# For example:
print(dir(greet))
# They are - lower, upper, isupper, startswith, endswith, find, replace, split, join, strip, etc.


# String find method
fruit = 'banana'
pos = fruit.find('na')  # Finds the first occurrence of 'na'
print(pos)  # Output: 2
pos = fruit.find('z')  # 'z' is not found
print(pos)  # Output: -1


# Searching and replacing
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')  # Replaces 'Bob' with 'Jane'
print(nstr)  # Output: Hello Jane
nstr = greet.replace('o', 'x')  # Replaces all 'o' with 'x'
print(nstr)  # Output: Hellx Bxb
# Note: The original string remains unchanged


# Stripping whitespace
greet = '   Hello Bob   '
print(greet.lstrip())  # Removes leading whitespace: 'Hello Bob   '
print(greet.rstrip())  # Removes trailing whitespace: '   Hello Bob'
print(greet.strip())   # Removes both leading and trailing whitespace: 'Hello Bob'


# Prefixing strings
line = 'Please have a nice day'
if line.startswith('Please'):
    print('Yes, the line starts with "Please"') # Output: Yes, the line starts with "Please"
if line.startswith('p'):
    print('Yes, the line starts with "p"')
else:
    print('No, the line does not start with "p"') # Output: No, the line does not start with "p"
# Note: startswith is case-sensitive

# Parsing and Extracting Data
data = 'From randomemail@gmail.com Sat Jan 5 09:14:16 2008'
atpos = data.find('@')  # Find position of '@'
sppos = data.find(' ', atpos)  # Find position of first space after '@'
host = data[atpos+1 : sppos]  # Extract substring between '@' and the next space
print(host)  # Output: gmail.com   
# This is a simple way to parse and extract specific parts of a string based on known patterns.

