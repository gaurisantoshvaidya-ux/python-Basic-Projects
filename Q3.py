# Function to manage student marks
# manage marks program
def manage_marks():
    marks = []  # List to store subject marks

    print("Enter marks for 5 subjects:")

    # Take input for 5 subjects
    while len(marks) < 5:
        try:
            mark = float(input(f"Enter mark for Subject {len(marks) + 1}: "))
            marks.append(mark)
        except ValueError:
            # Handle invalid (non-numeric) input
            print("Invalid input! Please enter a numeric value.")

    # Calculate average
    average = sum(marks) / len(marks)

    # Find highest and lowest marks
    highest = max(marks)
    lowest = min(marks)

    # Sort marks in descending order
    marks.sort(reverse=True)

    # Display results
    print("\n----- Result -----")
    print("Marks:", marks)
    print("Average Marks:", average)
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)
    print("Marks in Descending Order:", marks)


# Call the function
manage_marks()