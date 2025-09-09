# Basic conditional statements in Python

x = 10

# Simple if statement
if x > 5:
    print("x is greater than 5")

# if-else statement
if x < 5:
    print("x is less than 5")
else:
    print("x is not less than 5")

# if-elif-else statement
if x == 5:
    print("x is equal to 5")
elif x > 5:
    print("x is greater than 5")
else:
    print("x is less than 5")

# Exapmle calculating overtime pay using conditional statements
hours_worked = 45
hourly_rate = 20
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * hourly_rate * 1.5
    total_pay = (40 * hourly_rate) + overtime_pay
else:
    total_pay = hours_worked * hourly_rate
print(f"Total pay: ${total_pay:.2f}")

# Demonstrating nested if statements
age = 25
if age >= 18:
    if age < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")  
else:
    print("You are a minor.")

