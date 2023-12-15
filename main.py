import sys
from datetime import datetime
from validate import valid_inputs
from employee import Employee
from csv_helper import write_employees_csv, read_employees_csv

inputs = sys.argv
filename = "storage.csv"

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
    write_employees_csv(filename, employees)
    
# check if valid input
if not valid_inputs(inputs):
    exit(1)

# create new_employee to a file
if inputs[1] == "create":
    employee_data = inputs[2:]
    create_employee(employee_data)



  