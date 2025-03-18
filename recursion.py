# Recursive function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Recursive function to calculate Fibonacci series
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = fibonacci(n - 1)
        fib.append(fib[-1] + fib[-2])
        return fib

# Test cases
num = 5
print(f"Factorial of {num}: {factorial(num)}")

terms = 10
print(f"Fibonacci series ({terms} terms): {fibonacci(terms)}")
