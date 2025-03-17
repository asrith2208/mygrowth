# Control Flow: if-else, loops, and functions

# If-else statement
def check_number(num):
    if num > 0:
        print(f"{num} is a positive number.")
    elif num < 0:
        print(f"{num} is a negative number.")
    else:
        print("Number is zero.")

# For loop
def print_numbers(n):
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

# While loop
def countdown(n):
    while n > 0:
        print(n, end=" ")
        n -= 1
    print()

# Function with return value
def square(num):
    return num * num

# Function call examples
check_number(5)
check_number(-3)
check_number(0)

print_numbers(5)
countdown(5)

result = square(4)
print(f"Square of 4 is: {result}")