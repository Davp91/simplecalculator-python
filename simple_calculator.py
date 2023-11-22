def add(x, y):
    """Function to add two numbers."""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers."""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers."""
    return x * y

def divide(x, y):
    """Function to divide two numbers. Returns 'Undefined' for division by zero."""
    if y == 0:
        return "Undefined (division by zero)"
    return x / y

def main():
    # Main function to run the calculator
    while True:
        # Display the options to the user
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'quit' to end the program")
        user_input = input(": ")

        # Check if the user wants to quit the program
        if user_input == "quit":
            break

        # Check if the operation is valid
        if user_input in ("add", "subtract", "multiply", "divide"):
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))

            # Call the appropriate function based on the operation
            if user_input == "add":
                print("Result:", add(x, y))
            elif user_input == "subtract":
                print("Result:", subtract(x, y))
            elif user_input == "multiply":
                print("Result:", multiply(x, y))
            elif user_input == "divide":
                print("Result:", divide(x, y))
        else:
            # Inform the user of invalid input
            print("Invalid Input")

# Check if the script is run directly (not imported)
if __name__ == "__main__":
    main()
