def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y


def calculator():
    print("Welcome to the CLI Calculator!")
    print("Operations: + for addition, - for subtraction,")
    print("* for multiplication, / for division")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                result = "Invalid operator"

            print("Result:", result)
        except ValueError:
            print("Invalid input. Please enter numeric values.")

        prompt = "Do you want to perform another calculation? (yes/no): "
        choice = input(prompt)
        if choice.lower() != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break


if __name__ == "__main__":
    calculator()
