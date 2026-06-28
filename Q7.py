# Create a lambda function to calculate the square of a number
# Add lambda function program
square = lambda x: x * x

try:
    # Generate numbers from 1 to 20
    numbers = range(1, 21)

    # Store the squares in a list using the lambda function
    squares = list(map(square, numbers))

    # Display all square values
    print("Squares of numbers from 1 to 20:")
    print(squares)

    # Print only the even squares
    print("\nEven Squares:")
    for num in squares:
        if num % 2 == 0:
            print(num, end=" ")

# Handle any unexpected errors
except Exception as e:
    print("An error occurred:", e)