# Import required modules

import random
import math

# Create an empty set to store unique numbers
numbers = set()

print("Enter 10 numbers:")

try:
    # Take 10 numbers as input
    for i in range(10):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.add(num)   # Store only unique numbers

    # Convert the set into a tuple
    numbers_tuple = tuple(numbers)

    print("\nUnique Numbers (Set):", numbers)
    print("Tuple:", numbers_tuple)

    # Check if there are at least 3 unique numbers
    if len(numbers_tuple) >= 3:
        # Select 3 random numbers from the tuple
        random_numbers = random.sample(numbers_tuple, 3)
        print("3 Random Numbers:", random_numbers)
    else:
        print("Not enough unique numbers to select 3 random values.")

    # Calculate the sum of tuple elements
    total = sum(numbers_tuple)

    # Print the square root of the sum
    print("Sum of Tuple Elements:", total)
    print("Square Root of Sum:", math.sqrt(total))

# Handle invalid (non-numeric) input
except ValueError:
    print("Invalid input! Please enter only numeric values.")

# Handle math errors (if sum is negative)
except ValueError as e:
    print("Math Error:", e)

# Handle any other unexpected errors
except Exception as e:
    print("An unexpected error occurred:", e)