def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")

    choice = input("Enter choice (1/2): ")

    if choice in ['1', '2']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return

        if choice == '1':
            result = add(num1, num2)
            print(f"The result of addition is: {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"The result of subtraction is: {result}")
    else:
        print("Invalid choice. Please select 1 or 2.")

calculator()
