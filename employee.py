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

    def get_employee_id(self):
        return self.employee_id