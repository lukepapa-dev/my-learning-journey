# Loops and Iterations

# Example of a while loop
# This loop counts down from 5 to 1 and then prints "Blastoff!"
# Finally, it prints the value of n after the loop ends
n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff!")
print(n)


# Example of using break in a infinate loop
while True:
    line = input("> ")
    if line == "done":
        break
    print(line)
print("Done!")

# Using continue in an infinate loop
while True:
    line = input("> ")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("Done!")


# Definate loops
for i in [5, 4, 3, 2, 1]:
    print(i)
print("Blastoff!")

# Can also be used as strings
fruit = "bananas", "apples", "cherrys"
for eat in fruit:
    print("I like to eat", eat)  
print("Done!")


# Finding the largest value
largest_so_far = -1 # Can also use None but need to handle it in the loop, see "Finding the smallest value" example below
print("Before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print("After", largest_so_far)


# Finding the smallest value
smallest_so_far = None
print("Before", smallest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if smallest_so_far is None:
        smallest_so_far = the_num
    elif the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print("After", smallest_so_far)


# Loop Idioms
# Counting in a loop
count = 0
for thing in [9, 41, 12, 3, 74, 15]:
    count = count + 1
print("Count:", count)

# Summing in a loop
total = 0
for thing in [9, 41, 12, 3, 74, 15]:
    total = total + thing
print("Total:", total)

# Finding the average in a loop
count = 0
sum = 0
for thing in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + thing
print("Count:", count, "Total:", total, "Average:", total / count)

# Filtering in a loop
print("Before")
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print("Large number", value)
print("After")

# Search using a boolean variable
found = False
print("Before", found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
        # Could add a break here if we wanted to stop after finding the first instance
    print(found, value)
print("After", found)


# This small programem finds the largest and smallest number in a series of user inputs
# It handles invalid inputs and stops when the user types "done"
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    
    try:
        fnum = int(num)
    
    except:
        print("Invalid input")
        continue
      
    if largest is None:
        largest = fnum
    elif fnum > largest:
        largest = fnum
    
    if smallest is None:
        smallest = fnum
    elif fnum < smallest:
        smallest = fnum

print("Maximum is", largest)
print("Minimum is", smallest)