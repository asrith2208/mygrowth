# Python Collections: Lists, Tuples, Sets, Dictionaries (Advanced Use Cases)

# 👉 List Example: Sort, Reverse, and Filter
numbers = [10, 5, 8, 3, 2, 7, 4, 6]
numbers.sort()
print("Sorted List:", numbers)

numbers.reverse()
print("Reversed List:", numbers)

# Filtering even numbers using list comprehension
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even Numbers:", even_numbers)

# 👉 Tuple Example: Indexing and Counting
coordinates = (10, 20, 30, 10, 40)
print("Index of 30:", coordinates.index(30))
print("Count of 10:", coordinates.count(10))

# 👉 Set Example: Set Operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union, Intersection, Difference
print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
print("Difference:", set_a.difference(set_b))

# 👉 Dictionary Example: Keys, Values, and Nested Dictionaries
person = {
    "name": "Asrith",
    "age": 21,
    "skills": {
        "programming": ["Python", "Java"],
        "sports": ["Cricket", "Football"]
    }
}

# Accessing nested dictionary
print("Skills:", person["skills"]["programming"])
print("Keys:", person.keys())
print("Values:", person.values())