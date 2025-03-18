# Function to calculate the sum of two numbers
def add_numbers(a, b):
    return a + b

# Function with default parameters
def greet(name="Asrith"):
    print(f"Hello, {name}!")

# Function with keyword arguments
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

# Function with variable-length arguments (*args)
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

# Function with variable-length keyword arguments (**kwargs)
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Test the functions
print(add_numbers(5, 3))
greet()
greet("Python")
display_info(age=21, name="Asrith")
print(sum_numbers(1, 2, 3, 4, 5))
print_details(name="Asrith", age=21, language="Python")
