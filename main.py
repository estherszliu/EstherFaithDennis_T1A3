import sys
import csv
from datetime import datetime
from validate import valid_inputs
from employee import Employee
from csv_helper import write_employees_csv, read_employees_csv
from colored import fg, attr, bg


# create employee function
def create_employee(filename, employee_data):
    id = employee_data[0]
    # check the employee id whether exist
    employees = read_employees_csv(filename)

    for employee in employees:
        if employee.employee_id == id:
            print("    [ERROR]: The employee id already exist, please input a valid employee id")
            return False

    new_employee = Employee(employee_data[0], employee_data[1], employee_data[2], employee_data[3], employee_data[4], employee_data[5], employee_data[6])
    employees.append(new_employee)
    print(f"New employee created: {new_employee}")
    write_employees_csv(filename, employees)
    return True

# search function
def search_employee(filename, search_data):
    employees = read_employees_csv(filename)

    match_employees = []
    for employee in employees:

        is_match = True
        for i in range(0, len(search_data), 2):
            field = search_data[i] 
            value = search_data[i+1]

            if field == '--employee-id' and employee.employee_id != value:
                is_match = False
                break
            
            if field == '--first-name' and employee.first_name != value:
                is_match = False
                break
            
            if field == '--last-name' and employee.last_name != value:
                is_match = False
                break

            if field == '--phone-number' and employee.phone_number != value:
                is_match = False
                break

            if field == '--job-title' and employee.job_title != value:
                is_match = False
                break
            if field == '--max-salary' and employee.salary > int(value):
                is_match = False
                break
            if field == '--min-salary' and employee.salary < int(value):
                is_match = False
                break
            if field == '--max-start-date' and datetime.strptime(employee.start_date, '%d/%m/%y') > datetime.strptime(value, '%d/%m/%y'):
                is_match = False
                break
            if field == '--min-start-date' and datetime.strptime(employee.start_date, '%d/%m/%y') < datetime.strptime(value, '%d/%m/%y'):
                is_match = False
                break
        if is_match:
            match_employees.append(employee)
    
    for employee in match_employees:
        print(employee)

    if len(match_employees) == 0:
        print("No employees match your search")

    return True
      
#update employee data
def update_data(filename, update_employee):
    id = update_employee[0]
    updateData = update_employee[1:]

    employees = read_employees_csv(filename)

    employee = None

    for emp in employees:
        if emp.employee_id == id:
            employee = emp
    
    if  employee == None:
        print("    [ERROR]: Update employee can not found, please input the correct employee id")
        return False
    
    for i in range(0, len(updateData), 2):
        field = updateData[i] 
        value = updateData[i+1]
        if field == '--first-name':
            employee.first_name = value
        elif field == '--last-name':
            employee.last_name = value
        elif field == '--phone-number':
            employee.phone_number = value
        elif field == '--job-title':
            employee.job_title = value
        elif field == '--salary':
            employee.salary = value
        elif field == '--start-date':
            employee.start_date = value
    print(f"Employee updated: {employee}")       
    write_employees_csv(filename, employees)

    return True

# delete employee
def delete_data(filename, delete_employee):
    id = delete_employee

    employees = read_employees_csv(filename)

    employee = None
    for emp in employees:
        if emp.employee_id == id:
            employee = emp

    if  employee == None:
        print("    [ERROR]: Delete employee can not found, please input the existing employee id to delete")
        return False    
    
    print(f"Employee deleted: {employee}")
    employees.remove(employee)
     
    write_employees_csv(filename, employees)    
    return True

def run_app(filename):

    # welcome the user and get input
    print("")
    print("")
    print(f"{fg('black')}{bg('white')}Welcome to the Employee Directory{attr('reset')}")
    
    while(True):
        print("")
        print("Choose from one of these commands")
        print("  Enter 1 to creates a new employee")
        print("  Enter 2 to search for an employee")
        print("  Enter 3 to update the data for one employee")
        print("  Enter 4 to delete one employee")
        print("  Enter 5 to exit")
        print("")
        command = input("Enter your command: ")
        command = command.replace("  ", " ")

        print("")
        user_inputs = None
        if command == "1":
            print("Enter the new employee data in this format")
            print("    <employee-id> <first-name> <last-name> <phone-number> <job-title> <salary> <start-date>")
            print("")
            user_inputs = input("Enter the new employee data: ")
            print("")

        elif command == "2":
            print("Enter the search fields exactly like left column and space follow by the contents you want to find, leave blank if you want to see all users")
            print("    --employee-id     <employee-id>")
            print("    --first-name      <first-name>")
            print("    --last-name       <last-name>")
            print("    --phone-number    <phone-number>")
            print("    --job-title       <job-title>")
            print("    --max-salary      <max-salary>")
            print("    --min-salary      <min-salary>")
            print("    --max-start-date  <max-start-date>")
            print("    --min-start-date  <min-start-date>")

            print("")
            user_inputs = input("Enter the employee search fields: ")
            print("")

        elif command == "3":
            print("Enter the employee id followed by fields you want to update")
            print("    <employee-id> --first-name      <first-name>")
            print("                  --last-name       <last-name>")
            print("                  --phone-number    <phone-number>")
            print("                  --job-title       <job-title>")
            print("                  --max-salary      <max-salary>")
            print("                  --min-salary      <min-salary>")
            print("                  --max-start-date  <max-start-date>")
            print("                  --min-start-date  <min-start-date>")

            print("")
            user_inputs = input("Enter the employee id followed by fields to be updated: ")
            print("")
        elif command == "4":
            print("")
            user_inputs = input("Enter the employee id to be deleted: ")
            print("")
        elif command == "5":
            return
        else:
            print("    [ERROR]: Program needs a valid command")
            continue

        user_inputs = user_inputs.replace("  ", " ")
        inputs = user_inputs.split()

        # check if valid input
        if not valid_inputs(command, inputs):
            continue

        # create new_employee to a file
        if command == "1":
            employee_data = inputs
            create_employee(filename, employee_data)
        elif command =="2":
            search_data = inputs
            search_employee(filename, search_data)
        elif command == "3":
            update_employee = inputs
            update_data(filename, update_employee)
        elif command == "4":
            delete_employee = inputs[0]
            delete_data(filename, delete_employee)


if __name__ == "__main__":
    run_app("storage.csv")

   