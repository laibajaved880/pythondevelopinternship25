def calculator():
    print("Simple Calculator")
    print("Available operations: +, -, *, /")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                return "Error: Division by zero!"
        else:
            return "Invalid operator!"

        return f"Result: {result}"
    except ValueError:
        return "Invalid input! Please enter numbers."

print(calculator())
