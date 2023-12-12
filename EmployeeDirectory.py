import csv
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
    # try:
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

employee1 = Employee(1, "Esther", "Dennis", "035424445", "barista", "65000", "01/08/2022" )
write_employees_csv(filename, [employee1, employee1, employee1])
read_employees_csv(filename)

print(read_employees_csv(filename))




