def add(a, b):
    """
    Adds two numbers together.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b

def subtract(a, b):
    """
    Subtracts the second number from the first.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The difference of the two numbers.
    """
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers together.
    Args:
        a (int): The first number.
        b (int): The second number.
    Returns:
        int: The product of the two numbers.
    """
    return a * b

def divide(a, b):
    """
    Divides the first number by the second.
    Args:
        a (int): The first number.
        b (int): The second number.
    Returns:
        float: The quotient of the two numbers.
    Raises:
        ZeroDivisionError: If the second number is zero.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def main():
    """
    Main function to demonstrate the calculator operations.
    """
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter your choice (1-4): ")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '1':
        print(f"{a} + {b} = {add(a, b)}")
    elif choice == '2':
        print(f"{a} - {b} = {subtract(a, b)}")
    elif choice == '3':
        print(f"{a} * {b} = {multiply(a, b)}")
    elif choice == '4':
        try:
            print(f"{a} / {b} = {divide(a, b)}")
        except ZeroDivisionError as e:
            print(e)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()