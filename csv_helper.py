import csv
from employee import Employee

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

# to read the employees
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
