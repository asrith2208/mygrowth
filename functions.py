# Function with no arguments and no return value
def greet():
    print("Hello, welcome to Python!")

# Function with arguments and return value
def add(a, b):
    return a + b

# Lambda function (one-line function)
multiply = lambda x, y: x * y

# Function call
greet()
result = add(5, 3)
print(f"Sum of 5 and 3: {result}")

product = multiply(4, 5)
print(f"Product of 4 and 5 using lambda: {product}")