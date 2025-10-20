def print_menu():
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")
    print("[5] Quit")

def get_number(prompt):
    while True:
        try:
            value= float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate(choice, a, b):
    if choice == "1":
        return a + b
    elif choice == "2":
        return a - b
    elif choice == "3":
        return a * b
    elif choice == "4":
        if b == 0:
            print("Error: Division by zero is not allowed.")
            return None
        return a / b
    else:
        print("Unknown operation.")
        return None
    
def main():
    while True:
        print_menu()
        choice= input("Select an operation: ").strip().lower()    
        if choice == "5":
            print("Exiting the calculator. Goodbye!")
            break
        elif choice in ("1", "2", "3", "4"):
            a= get_number("Enter first number: ")
            b= get_number("Enter second number: ")
            result=calculate(choice, a, b)
            if result is not None:
                print("Result: ", result)
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()