while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        result = num1 / num2
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    else:
        print("Result of division is:", result)
        break
