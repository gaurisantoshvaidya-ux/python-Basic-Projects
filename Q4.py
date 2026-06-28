# Class to store and manage student details
class Student:

    # Constructor to initialize student details
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []

    # Method to add a mark with validation
    def add_mark(self, mark):
        try:
            mark = float(mark)

            # Check if the mark is within the valid range
            if mark < 0 or mark > 100:
                raise ValueError("Marks should be between 0 and 100.")

            self.marks_list.append(mark)

        except ValueError as e:
            print("Invalid mark:", e)

    # Method to calculate the average marks
    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)

    # Method to display student information
    def display_info(self):
        print("\n----- Student Information -----")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks_list)
        print("Average Marks:", self.get_average())


# Take student details from the user
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Create a Student object
student = Student(name, roll_no)

# Take marks for 5 subjects
print("\nEnter marks for 5 subjects:")

for i in range(5):
    mark = input(f"Subject {i + 1}: ")
    student.add_mark(mark)

# Display student details
student.display_info()