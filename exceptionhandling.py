# Basic Try-Except
# If an error occurs inside try, Python jumps to except.
try:
    x = 10 / 0  # This will cause a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

 # Handling Multiple Exceptions
try:
    num = int(input("Enter a number: "))  
    result = 10 / num  
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")

# Using finally
# The finally block always executes, even if there is an error.
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Error: File not found!")
finally:
    print("Closing program...")  # Runs no matter what
