# Basic Calculatior

print('Welcome to the calculator!')
print('Use (+ - * /) to perform operations')
print('Type "exit" to quit')
print()

while True:
    
    num1 = input('Enter a number: ')
    operator = input('Enter an operator: ')
    num2 = input('Enter another number: ' )

    if operator == '+':
        result = float(num1) + float(num2)
        print('The result is: ', result)
    elif operator == '-':
        result = float(num1) - float(num2)
        print('The result is: ', result)
    elif operator == '*':
        result == float(num1) * float(num2)
        print('The result is: ', result)
    elif operator == '/':
        result = float(num1) / float(num2)
        print('The result is: ', result)
    elif operator == 'exit' or num1 == 'exit' or num2 == 'exit':
        print ('Exiting the calculator, Goodbye!')
        break
    else:
        print('Invalid operator, please try again.')
        continue