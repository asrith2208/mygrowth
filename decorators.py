# Decorators in Python
# Decorators are used to modify the behavior of functions without changing their code.
#  Basic Decorator : A decorator is a function that takes another function as input, modifies it, and returns it.
def my_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, Asrith!")

say_hello()

#  Decorators with Arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Asrith")


