#  Creating a Generator
# A generator is defined just like a normal function, but instead of return, we use yield.
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()  # Creating generator object
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

# Generator vs Normal Function : A normal function executes completely when called, while a generator pauses and resumes:
def normal_function():
    return [1, 2, 3]

print(normal_function())  # [1, 2, 3]
# But with a generator:
def generator_function():
    yield 1
    yield 2
    yield 3

gen = generator_function()
print(next(gen))  # 1
print(next(gen))  # 2

# Generator with Loop : Instead of using next(), we can loop through a generator
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)  

# Using yield with Expressions: Generators can also return values dynamically
def squares(n):
    for i in range(n):
        yield i * i

gen = squares(5)
print(list(gen))  # [0, 1, 4, 9, 16]

# Generator Expressions (Shorter Way)
# Instead of defining a generator function, we can create generators like list comprehensions:
gen_exp = (x * x for x in range(5))
print(list(gen_exp))  # [0, 1, 4, 9, 16]

