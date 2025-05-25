def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print("Factorial of 5 is:", factorial(5))
def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Only non-negative integers are allowed.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
