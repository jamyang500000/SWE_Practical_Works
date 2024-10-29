from collections import defaultdict
import time

# Recursive Fibonacci
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Modified Iterative Fibonacci to return a list of Fibonacci numbers up to n
def fibonacci_iterative(n):
    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n + 1]

# Test the modified iterative function
n = 10
print(f"Fibonacci sequence up to F({n}): {fibonacci_iterative(n)}")

# Function to find the index of the first Fibonacci number that exceeds a given value
def find_fibonacci_exceeding(value):
    a, b = 0, 1
    index = 1
    while b <= value:
        a, b = b, a + b
        index += 1
    return index

# Test the function
value = 50
print(f"Index of the first Fibonacci number exceeding {value}: {find_fibonacci_exceeding(value)}")

# Function to determine if a given number is a Fibonacci number
def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num or num == 0

# Test the function
test_number = 21
print(f"Is {test_number} a Fibonacci number? {is_fibonacci(test_number)}")

# Function to calculate the ratio of consecutive Fibonacci numbers
def fibonacci_ratios(limit):
    ratios = []
    a, b = 0, 1
    for _ in range(limit - 1):
        if a != 0:  # To avoid division by zero
            ratios.append(b / a)
        a, b = b, a + b
    return ratios

# Test the ratio function and observe the approach to the golden ratio
limit = 10
ratios = fibonacci_ratios(limit)
print(f"Ratios of consecutive Fibonacci numbers (limit {limit}): {ratios}")
print(f"The ratio approaches: {ratios[-1]:.5f} (approaching the golden ratio)")

# Memoized Fibonacci function
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]

# Measure execution time function
def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

# Compare recursive and memoized function execution time for a large Fibonacci number
n = 30
recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
memoized_result, memoized_time = measure_time(fibonacci_memoized, n)

print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")
