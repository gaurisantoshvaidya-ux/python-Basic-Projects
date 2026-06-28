# Class to store Employee details
# Add Employee class program
class Employee:

    # Constructor to initialize employee details
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name

        # Store department and salary as a tuple
        self.details = (department, salary)

    # Method to display employee information
    def show_details(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.details[0])
        print("Salary:", self.details[1])
        print("------------------------")


# Create a dictionary to store Employee objects
employees = {}

# Add 3 employee objects to the dictionary
employees[101] = Employee(101, "Rahul", "HR", 35000)
employees[102] = Employee(102, "Priya", "IT", 50000)
employees[103] = Employee(103, "Amit", "Finance", 45000)

# Display all employee details using a loop
print("----- Employee Details -----")

for emp_id, employee in employees.items():
    employee.show_details()