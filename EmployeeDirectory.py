import csv
import sys
from datetime import datetime

inputs = sys.argv


# validate command function
def valid_command(cmd):
    if (cmd == "create" or cmd == "update" or cmd == "search" or cmd == "delete"):
        return True
    return False

# validate whether is number function
def valid_number(num_as_string):
    if num_as_string.isdigit():
        return True
    return False

# validate whether name is alpha function
def valid_name(name):
    if name.isalpha():
        return True
    return False

# validate date function
date_formet = "%d/%m/%y"

def valid_date(date, date_formet):
    try:
        datetime.strptime(date, date_formet)
        return True
    except ValueError:
        return False

 # validate_command line oparators   
if not valid_command(inputs[1]):
    print("ERROR: Invalid command: Enter either create, update or search")
    exit(1)

# validate the number of input
if len(inputs) != 16:
    print("ERROR: Incorrect number of arguments given")
    exit(1)

# validate_employee_id - key whether is sting
if inputs[2] != "employee_id" :
    print("The employee id should be input as employee_id")
    exit(1)

# validate_ employee id - value
if not valid_number(inputs[3]):
    print("ERROR: The employee id should be a digital number.")
    exit(1)

# validate first name as a key
if inputs[4] != "first_name":
    print("ERROR: First name has to input as first_name")
    exit(1)

# validate first name as alpha input
if not valid_name(inputs[5]):
    print("ERROR: The first name is invalid, please input a valid name")

# validate last name key
if inputs[6] != "last_name":
    print("ERROR: The last name has to input as last_name")
    exit(1)

# validate last name as alpha input
if not valid_name(inputs[7]):
    print("ERROR: The last name is invalid, please input a valid name")
    exit(1)

# validate phone number key
if inputs[8] != "phone_number":
    print("ERROR: The phone number should input as phone_number")
    exit(1)

# validate phone number as all digit
if not valid_number(inputs[9]):
    print("ERROR: The phone number should be a digital number.")
    exit(1)

# validate job title key
if inputs[10] != "job_title":
    print("ERROR: The job title should input as job_title.")
    exit(1)  

# validate job title as all alpha
if not valid_name(inputs[11]):
    print("ERROR: The job title is invalid, please input an alpha name for job title.")
    exit(1)

# validate salary key
if inputs[12] != "salary":
    print("ERROR: Wrong input, please input salary as salary." )
    exit(1)

# validate salary as all digit
if not valid_number(inputs[13]):
    print("ERROR: The salary should be a digital and a whole number.")
    exit(1)

# validate start date key
if inputs[14] != "start_date":
    print("ERROR: Wrong input, please input start date as start_date." )
    exit(1)

# validate start date
if not valid_date(inputs[15], date_formet):
    print("ERROR: Invalid start date, please input format as dd/mm/yy")






filename = "storage.csv"

class Employee:
    # Constructor
    def __init__(self, employee_id, first_name, last_name, phone_number, job_title, salary, start_date):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.job_title = job_title
        self.salary = salary
        self.start_date = start_date
    # print data from employee
    def __str__(self):
        return str(self.employee_id)  + " " + \
            self.first_name           + " " + \
            self.last_name            + " " + \
            self.phone_number         + " " + \
            self.job_title            + " " + \
            str(self.salary)          + " " + \
            self.start_date

    # get an employee as a list
    def get_as_list(self):
        return [
            str(self.employee_id),
            self.first_name,
            self.last_name,
            self.phone_number,
            self.job_title,
            str(self.salary),
            self.start_date
        ]
    
# write employee to file function
def write_employees_csv(filename, employees):
    
    header = ["employee_id", "first_name", "last_name", "phone_number", "job_title", "salary","start_date"]
    employee_data = []
    
    for employee in employees:
        employee_data.append(employee.get_as_list())
      

    with open (filename, "w") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(employee_data)

def read_employees_csv(filename):
    try:
        employees = []
        with open(filename, "r") as file:
            reader =csv.DictReader(file)
            for row in reader:
                employees.append(
                    Employee(
                        row["employee_id"],
                        row["first_name"], 
                        row["last_name"], 
                        row["phone_number"], 
                        row["job_title"], 
                        row["salary"], 
                        row["start_date"]
                    )
                )        
        return(employees)

    except FileNotFoundError:
        return []

# create new_employee to a file
if inputs[1] == "create":
    new_employee =Employee(inputs[3], inputs[5],inputs[7], inputs[9], inputs[11],inputs[13], inputs[15])
    print( new_employee)
    write_employees_csv(filename, [new_employee])
employees = read_employees_csv(filename)
print(employees)

# check the employee whether exist

# for the employee in Employee
    # if the the input_employee_id == employee[employee_id]
    #print (employee id already exist, please input a valid employee id)
    # return turn
    # return false



