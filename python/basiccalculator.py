def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a* b
def div(a, b):
    if b == 0 :
        return "Error: Divide by zero"
    return a / b

def get_numbers():
    """Prompt until two valid numbers are entered."""
    while True:
        try:
            a = float(input("Enter first number:"))
            b = float(input("Enter second nummber:"))
            return a, b
        except ValueError:
            print("Please enter valid numbers.")
def calculator():
    menu = {
        "1": ("Addition", add),
        "2": ("Subtraction", sub),
        "3": ("Multiplication", mul),
        "4": ("Division", div),
        "5": ("Exit", None)
    }      

    while True:                         
        print("\n--- Basic Calculator ---")
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")
        choice = input("Choose an option: ").strip()

        if choice not in menu:          
            print("Invalid option, try again.")
            continue
        if choice == "5":
            print("Goodbye!")
            break

        x, y = get_numbers()
        op_func = menu[choice][1]
        print("Result:", op_func(x, y))

if __name__ == "__main__":
    calculator()          