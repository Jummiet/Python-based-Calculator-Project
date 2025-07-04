# calculator.py

def add(a, b):
    """
    This task Adds two numbers together.

    Parameters:
        a (float): The first number
        b (float): The second number

    Returns:
        float: The sum of a and b
    """
    return a + b


def subtract(a, b):
    """
    This task Subtracts the second number from the first.

    Parameters:
        a (float): The first number
        b (float): The second number

    Returns:
        float: The result of a - b
    """
    return a - b


def divide(a, b):
    """
    Divides the first number by the second.

    Parameters:
        a (float): The numerator
        b (float): The denominator

    Returns:
        float: The result of a / b

    Raises:
        ValueError: If division by zero is attempted
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


# If you want to allow command-line interaction:
if __name__ == "__main__":
    print("Simple Calculator")
    print("Operations: 1) Add  2) Subtract  3) Divide")

    try:
        op = int(input("Choose operation (1/2/3): "))
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if op == 1:
            print("Result:", add(x, y))
        elif op == 2:
            print("Result:", subtract(x, y))
        elif op == 3:
            print("Result:", divide(x, y))
        else:
            print("Invalid operation selected.")
    except ValueError as e:
        print("Error:", e)
