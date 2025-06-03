from multipledispatch import dispatch

# Greet a person by name
@dispatch(str)
def greet(name):
    print(f"Hello, {name}! Welcome.")

# Greet a group by number
@dispatch(int)
def greet(count):
    print(f"Hello, group of {count} people! Welcome.")

# Test calls
greet("Alice")     # Output: Hello, Alice! Welcome.
greet(5)           # Output: Hello, group of 5 people! Welcome.
