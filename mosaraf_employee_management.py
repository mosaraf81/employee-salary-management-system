# File name where employee records will be stored
FILE_NAME = "employees.txt"


def format_employee_record(name, emp_id, salary):
    """Reusable helper function to format employee details using parameters and return."""
    return f"{name} | {emp_id} | {salary}\n"


def add_employee(name, emp_id, salary):
    """Takes employee details as parameters, saves them to the file, and returns status."""
    record = format_employee_record(name, emp_id, salary)
    
    # Open the file in append mode ('a') to add new records without erasing old ones
    with open(FILE_NAME, "a") as file:
        file.write(record)
        
    return "Employee Added Successfully"


def view_employees():
    """Reads all employee records from the file and returns them as a list."""
    try:
        # Open the file in read mode ('r') to fetch stored records
        with open(FILE_NAME, "r") as file:
            records = file.readlines()
        return records
    except FileNotFoundError:
        # Return an empty list if the file has not been created yet
        return []

def display_menu():
    """Displays the menu options and returns the user's choice."""
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Exit")
    choice = input("\nChoose Option: ").strip()
    return choice

def main():
    """Main function to run the Employee Salary Management System."""
    while True:
        choice = display_menu()

        if choice == "1":
            # Take employee details from user input
            name = input("\nEnter Name: ").strip()
            emp_id = input("Enter ID: ").strip()
            salary = input("Enter Salary: ").strip()

            # Call add_employee with parameters and print the returned confirmation
            message = add_employee(name, emp_id, salary)
            print(f"\n{message}")

        elif choice == "2":
            # Call view_employees to read records from employees.txt
            records = view_employees()
            print("\n--- Employee Records ---")
            if not records:
                print("No employee records found.")
            else:
                for line in records:
                    print(line.strip())
        
        elif choice == "3":
            print("\nExiting program. Goodbye!")
            break

        else:
            print("\nInvalid option. Please enter 1, 2, or 3.")


# Run the program
if __name__ == "__main__":
    main()

            