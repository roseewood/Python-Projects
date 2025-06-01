import json
import os

EMPLOYEE_FILE = "employees.json"

# Load employees from file
def load_employees():
    if os.path.exists(EMPLOYEE_FILE):
        with open(EMPLOYEE_FILE, "r") as f:
            return json.load(f)
    return {}

# Save employees to file
def save_employees(employees):
    with open(EMPLOYEE_FILE, "w") as f:
        json.dump(employees, f, indent=4)

# Add new employee
def add_employee(employees):
    emp_id = input("Enter employee ID: ")
    if emp_id in employees:
        print("Employee ID already exists.")
        return
    name = input("Enter employee name: ")
    age = input("Enter employee age: ")
    department = input("Enter department: ")
    employees[emp_id] = {
        "name": name,
        "age": age,
        "department": department
    }
    print("Employee added successfully.")

# View all employees
def view_employees(employees):
    if not employees:
        print("No employees found.")
        return
    for emp_id, info in employees.items():
        print(f"\nID: {emp_id}")
        for key, value in info.items():
            print(f"{key.capitalize()}: {value}")

# Search employee by ID
def search_employee(employees):
    emp_id = input("Enter employee ID to search: ")
    if emp_id in employees:
        print(f"\nID: {emp_id}")
        for key, value in employees[emp_id].items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("Employee not found.")

# Update employee
def update_employee(employees):
    emp_id = input("Enter employee ID to update: ")
    if emp_id in employees:
        print("Leave field blank to keep current value.")
        name = input(f"New name ({employees[emp_id]['name']}): ") or employees[emp_id]['name']
        age = input(f"New age ({employees[emp_id]['age']}): ") or employees[emp_id]['age']
        department = input(f"New department ({employees[emp_id]['department']}): ") or employees[emp_id]['department']
        employees[emp_id] = {
            "name": name,
            "age": age,
            "department": department
        }
        print("Employee updated successfully.")
    else:
        print("Employee not found.")

# Delete employee
def delete_employee(employees):
    emp_id = input("Enter employee ID to delete: ")
    if emp_id in employees:
        del employees[emp_id]
        print("Employee deleted.")
    else:
        print("Employee not found.")

# Main loop
def main():
    employees = load_employees()
    
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            view_employees(employees)
        elif choice == '3':
            search_employee(employees)
        elif choice == '4':
            update_employee(employees)
        elif choice == '5':
            delete_employee(employees)
        elif choice == '6':
            save_employees(employees)
            print("Exiting program. Data saved.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
