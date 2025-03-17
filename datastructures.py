# Creating a list
fruits = ["apple", "banana", "cherry", "apple"]
print(fruits)  

# Accessing elements
print(fruits[0])  # First element

# Updating elements
fruits[1] = "blueberry"  

# Adding elements
fruits.append("orange")  
fruits.insert(1, "grape")  

# Removing elements
fruits.remove("cherry")  
deleted = fruits.pop(2)  

# Slicing a list
print(fruits[1:3])  

# List comprehension
squared = [x**2 for x in range(5)]  
print(squared)  

# Output
print(fruits)  
print(deleted)  

# Creating a tuple
coordinates = (10, 20, 30)

# Accessing elements
print(coordinates[1])

# Immutable – Can't change value
# coordinates[1] = 25  # This will throw an error

# Tuple unpacking
x, y, z = coordinates
print(x, y, z)

# Output
print(coordinates)

# Creating a set
numbers = {1, 2, 3, 4, 5}

# Adding elements
numbers.add(6)

# Removing elements
numbers.remove(3)

# Union, Intersection, Difference
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a.union(set_b))       # {1, 2, 3, 4, 5}
print(set_a.intersection(set_b)) # {3}
print(set_a.difference(set_b))   # {1, 2}

# Creating a dictionary
person = {
    "name": "Asrith",
    "age": 21,
    "is_coding": True
}

# Accessing values
print(person["name"])  

# Updating values
person["age"] = 22  

# Adding key-value pair
person["city"] = "Hyderabad"  

# Removing key-value pair
del person["is_coding"]  

# Looping through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# Output
print(person)