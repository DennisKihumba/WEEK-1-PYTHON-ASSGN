#we are creating a calculator that will add, subtract, multiply and find the quotient
# Basic Calculator Program

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operation (+, -, *, /): ")

# Perform calculation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Cannot divide by zero.")
        result = None10
else:
    print("Error: Invalid operator.")
    result = None

# Display result
if result is not None:
    print(f"{num1} {operator} {num2} = {result}")
