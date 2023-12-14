import sys
from datetime import datetime
from validate import valid_inputs
from employee import Employee
from csv_helper import write_employees_csv, read_employees_csv

inputs = sys.argv
filename = "storage.csv"
    
# check if valid input
if not valid_inputs(inputs):
    exit(1)

# create new_employee to a file
if inputs[1] == "create":
    id = inputs[2]
    # check the employee id whether exist
    employees = read_employees_csv(filename)
    employees_id =[]
    for employee in employees:
       employees_id.append(employee.get_employee_id())

    for employee_id in employees_id:
        if id == employee_id:
            print("ERROR: The employee id already exist, please input a valid employee id")
            exit(1)

    new_employee =Employee(inputs[2], inputs[3],inputs[4], inputs[5], inputs[6],inputs[7], inputs[8])
    write_employees_csv(filename, [new_employee])



  