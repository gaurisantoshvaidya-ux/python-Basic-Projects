# Import the math module
# Add unique word program
import math

try:
    # Take a sentence as input
    sentence = input("Enter a sentence: ")

    # Split the sentence into words
    words = sentence.split()

    # Store unique words in a set
    unique_words = set(words)

    # Sort the unique words

    sorted_words = sorted(unique_words)

    # Display the unique words
    print("\nUnique Words in Sorted Order:")
    for word in sorted_words:
        print(word)

    # Count the number of unique words
    count = len(unique_words)

    # Print the square of the count using the math module
    print("\nTotal Unique Words:", count)
    print("Square of Total Unique Words:", math.pow(count, 2))

# Handle unexpected errors
except Exception as e:
    print("An error occurred:", e)