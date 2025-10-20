while True:
    choice= input("Select operation ([1] Addition, [2] Subtraction, [3] Multiplication, [4] Division, [5] Quit): ")
    
    if choice == "5":
        print("Exiting the calculator. Goodbye!")
        break
    elif choice in ("1", "2", "3", "4"):
        while True:
            try:
                num1=float(input("Enter first number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        while True:
            try:
                num2=float(input("Enter second number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        if choice == "4" and num2 == 0:
            print("Error: Division by zero is not allowed.")
            continue                
        if choice == "1":
            print("You selected Addition")
            result= num1 + num2
            print("Result: ", result)
        elif choice == "2":
            print("You selected Subtraction")
            result= num1 - num2
            print("Result: ", result)
        elif choice == "3":
            print("You selected Multiplication")
            result= num1 * num2
            print("Result: ", result)
        elif choice == "4":
            print("You selected Division")
            result= num1 / num2
            print("Result: ", result)    
    else:
        print("Invalid choice. Please select a valid operation.")