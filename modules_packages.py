# Importing Modules
# Using Built-in Modules
# Python has many built-in modules like math and random.
import math
print(math.sqrt(25))  # Output: 5.0

 # Creating a Custom Module
# You can create your own module and use it in other programs.
# Step 1: Create a module (my_module.py)
def greet(name):
    return f"Hello, {name}!"

pi = 3.14159
# Step 2: Import and Use It (main.py)
import my_module

print(my_module.greet("Asrith"))  # Output: Hello, Asrith!
print(my_module.pi)  # Output: 3.14159

# Importing Specific Functions
# Instead of importing the whole module, import only what you need.
from math import sqrt
print(sqrt(16))  # Output: 4.0

#  Installing External Packages (Using pip)
# pip is used to install external libraries like NumPy, Pandas, etc.