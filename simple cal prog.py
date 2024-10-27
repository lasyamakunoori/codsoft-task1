def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."
def main():
    print("-----------------------------------")
    print("|        Simple Calculator        |")
    print("-----------------------------------")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /): ")

        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
        else:
            result = "Invalid operation.choose +, -, *, or /."
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
if __name__ == "__main__":
    main()
