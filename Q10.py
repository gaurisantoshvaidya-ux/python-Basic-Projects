# Smart Calculator & Data Manager
# Add Smart Calculator project

# Import required modules
import math
import random
from datetime import datetime

# Dictionary to store calculation history
history = {}


# Function for basic arithmetic operations
def basic_arithmetic():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nChoose Operation")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            result = num1 + num2
        elif choice == 2:
            result = num1 - num2
        elif choice == 3:
            result = num1 * num2
        elif choice == 4:
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            print("Invalid choice!")
            return None

        print("Result:", result)
        return result

    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")

    return None


# Function for scientific calculations
def scientific_calculation():
    try:
        print("\nScientific Operations")
        print("1. Square Root")
        print("2. Power")
        print("3. Factorial")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            num = float(input("Enter a number: "))
            result = math.sqrt(num)

        elif choice == 2:
            base = float(input("Enter base: "))
            exponent = float(input("Enter exponent: "))
            result = math.pow(base, exponent)

        elif choice == 3:
            num = int(input("Enter an integer: "))
            result = math.factorial(num)

        else:
            print("Invalid choice!")
            return None

        print("Result:", result)
        return result

    except ValueError:
        print("Invalid input!")
    except Exception as e:
        print("Error:", e)

    return None


# Function to generate random numbers
def generate_random():
    try:
        count = int(input("How many random numbers to generate? "))
        random_list = []

        for i in range(count):
            random_list.append(random.randint(1, 100))

        print("Random Numbers:", random_list)
        return random_list

    except ValueError:
        print("Invalid input!")
        return None


# Main program
while True:

    print("\n===== Smart Calculator & Data Manager =====")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculations")
    print("3. Generate Random Numbers")
    print("4. Store Result")
    print("5. View History")
    print("6. Exit")

    try:
        option = int(input("Enter your choice: "))

        if option == 1:
            last_result = basic_arithmetic()

        elif option == 2:
            last_result = scientific_calculation()

        elif option == 3:
            last_result = generate_random()

        elif option == 4:
            if 'last_result' in locals() and last_result is not None:
                # Store result with current timestamp
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                history[timestamp] = str(last_result)
                print("Result stored successfully.")
            else:
                print("No result available to store.")

        elif option == 5:
            if len(history) == 0:
                print("No history available.")
            else:
                print("\n----- Calculation History -----")
                for time, result in history.items():
                    print(time, "->", result)

        elif option == 6:
            print("Thank you for using Smart Calculator!")
            break

        else:
            print("Invalid choice! Please select between 1 and 6.")

    except ValueError:
        print("Please enter a valid numeric choice.")