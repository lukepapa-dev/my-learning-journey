# Using Functions

# Definitions
def thing():
    print ('I am a thing!')
    print ('Hello!')

thing()
print ('I am outside the thing!')



print()



# Big and Min Functions
big = max(1, 2, 3, 4, 5)
print (big)
tiny = min(1, 2, 3, 4, 5)
print (tiny)

big = max('Hello world!')
print (big)
tiny = min('Hello world!')
print (tiny)



print()



# Type Covertion Functions
x = int(1)
y = int(2.8)
z = int("3")
print (x, y, z)
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print (x, y, z, w)
x = str("s1")
y = str(2)
z = str(3.0)
print (x, y, z)



print()



# Definitions perameter
def add(yeah):
    if yeah == 'es':
        print ('Yes!')
    elif yeah == 'no':
        print ('No!')
    else:
        print ("I don't understand")

add('es')
add('no')
add('maybe')




print()



# Return Value -- return basically ends the function and sends a value back to the caller
def greet(hello):
    if hello == 'en':
        return ('Hello!')
    elif hello == 'es':
        return ('Hola!')
    else:
        return ("Hallo?")

print (greet('en'), 'Jamie')
print (greet('es'), 'Pablo')
print (greet('de'), 'Rebbecca')


print()


# multiple perameters
def addtwo(a, b):
    added = a + b
    return added
print (addtwo(3, 5))