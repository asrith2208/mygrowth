def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

# Take user input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    print(f"Result: {add(a, b)}")
elif operation == "-":
    print(f"Result: {subtract(a, b)}")
elif operation == "*":
    print(f"Result: {multiply(a, b)}")
elif operation == "/":
    print(f"Result: {divide(a, b)}")
else:
    print("Invalid operation")