import sys


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x*y


if __name__ == "__main__":
    operation = sys.argv[1]
    num1 = int(sys.argv[2])
    num2 = int(sys.argv[3])

    if operation == "add":
        print(add(num1, num2))
    elif operation == "subtract":
        print(subtract(num1, num2))
    elif operation == "multiply":
        print(multiply(num1, num2))
