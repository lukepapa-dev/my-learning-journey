# Looking inside strings
fruit = 'banana'
print(fruit[1])
print(fruit[0])
print(fruit[2])


# String length
#len() function
print(len(fruit))
print(len('banana'))
x = len(fruit)
print(x)


#looping through strings
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1


# For a different approach, we can use a for loop
fruit = 'banana'
for letter in fruit:
    print(letter)


# Looping and counting
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)


# Slicing strings
s = 'Monty Python'
print(s[0:4])  # characters 0 through 3 - up to but not including 4
print(s[6:7])  # character 6
print(s[6:20]) # character 6 through end of string (20 is beyond the end which is okay)
print(s[:2])   # characters from beginning to 2 (not including 2)
print(s[8:])   # characters from 8 to end
print(s[:])    # the whole string (Not very useful)


