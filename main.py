def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed"
    else:
        return x / y

def main():
    print("Welcome to the Python Calculator!")
    while True:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation == '+':
            print(num1, "+", num2, "=", add(num1, num2))
        elif operation == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif operation == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif operation == '/':
            print(num1, "/", num2, "=", divide(num1, num2))
        else:
            print("Invalid operation")

        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()
