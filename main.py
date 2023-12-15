import sys
import csv
from datetime import datetime
from validate import valid_inputs
from employee import Employee
from csv_helper import write_employees_csv, read_employees_csv

inputs = sys.argv
filename = "storage.csv"

# create employee function
def create_employee(employee_data):
    id = employee_data[0]
    # check the employee id whether exist
    employees = read_employees_csv(filename)

    for employee in employees:
        if employee.employee_id == id:
            print("ERROR: The employee id already exist, please input a valid employee id")
            return False

    new_employee = Employee(employee_data[0], employee_data[1], employee_data[2], employee_data[3], employee_data[4], employee_data[5], employee_data[6])
    employees.append(new_employee)
    print(f"New employee created: {new_employee}")
    write_employees_csv(filename, employees)
    return True

# search function
def search_employee(search_data):
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

            if field == '--max-salary' and employee.salary > int(value):
                is_match = False

            if field == '--min-salary' and employee.salary < int(value):
                is_match = False

            if field == '--max-start-date' and datetime.strptime(employee.start_date, '%d/%m/%y') < datetime.strptime(value, '%d/%m/%y'):
                is_match = False

            if field == '--min-start-date' and datetime.strptime(employee.start_date, '%d/%m/%y') > datetime.strptime(value, '%d/%m/%y'):
                is_match = False
        
        if is_match:
            match_employees.append(employee)
        
    for employee in match_employees:
        print(employee)

    return True       
#update employee data
def update_data(update_employee):
    id = update_employee[0]
    updateData = update_employee[1:]

    employees = read_employees_csv(filename)

    employee = None

    for emp in employees:
        if emp.employee_id == id:
            employee = emp
    
    if  employee == None:
        print("ERROR: Update employee can not found, please input the correct employee id")
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
# check if valid input
if not valid_inputs(inputs):
    exit(1)

# create new_employee to a file
if inputs[1] == "create":
    employee_data = inputs[2:]
    create_employee(employee_data)

if inputs[1] =="search":
    search_data = inputs[2:]
    search_employee(search_data)

if inputs[1] == "update":
    update_employee = inputs[2:]
    update_data(update_employee)

  