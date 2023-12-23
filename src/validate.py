from datetime import datetime
from colored import fg, attr, bg


def print_error(message):
    print(f"    {fg('red')}{bg('black')}[ERROR]: {message}{attr('reset')}")


# validate command function
def valid_command(cmd):
    if (cmd == "1" or cmd == "2" or cmd == "3" or cmd == "4" or cmd == "5"):
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
def valid_date(date):
    date_format = "%d/%m/%y"

    try:
        datetime.strptime(date, date_format)
        return True
    except ValueError:
        return False


# valid command
def valid_create_inputs(inputs):

    # validate the number of input
    if len(inputs) != 7:
        print_error("Incorrect number of arguments given, please input format with space seperate as create employee_id first_name last_name phone_number job_title salary start_date")
        return False

    # validate_ employee id - value
    if not valid_number(inputs[0]):
        print_error("The employee id should be a digital number.")
        return False

    # validate first name as alpha input
    if not valid_name(inputs[1]):
        print_error("The first name is invalid, please input a valid name.")
        return False

    # validate last name as alpha input
    if not valid_name(inputs[2]):
        print_error("The last name is invalid, please input a valid name.")
        return False

    # validate phone number as all digit
    if not valid_number(inputs[3]):
        print_error("The phone number should be a digital number.")
        return False

    # validate job title as all alpha
    if not valid_name(inputs[4]):
        print_error(
            "The job title is invalid, please input an alpha name for job title.")
        return False

    # validate salary as all digit
    if not valid_number(inputs[5]):
        print_error("The salary should be a digital and a whole number.")
        return False

    # validate start date
    if not valid_date(inputs[6]):
        print_error("Invalid start date, please input format as dd/mm/yy.")
        return False

    return True


# valid search
def valid_search_inputs(inputs):
    if len(inputs) > 18 or len(inputs) % 2 != 0:
        print_error("Not a valid number of inputs.")
        return False

    fields = inputs[0:]
    # see how many search field
    fields_number = int((len(inputs)) / 2)

    seen = set()

    for i in range(0, fields_number * 2, 2):
        field = fields[i]
        value = fields[i + 1]

        if (field in seen):
            print_error("Don't use same field twice.")
            return False

        seen.add(field)

        if field == "--employee-id":
            if (not valid_number(value)):
                print_error("employee-id is not valid.")
                return False
        elif field == "--first-name":
            if (not valid_name(value)):
                print_error("first-name is not valid.")
                return False
        elif field == "--last-name":
            if (not valid_name(value)):
                print_error("last-name is not valid.")
                return False
        elif field == "--phone-number":
            if (not valid_number(value)):
                print_error("phone-number is not valid.")
                return False
        elif field == "--job-title ":
            if (not valid_name(value)):
                print_error("job-title is not valid.")
                return False
        elif field == "--max-salary":
            if (not valid_number(value)):
                print_error("max-salary is not valid.")
                return False
        elif field == "--min-salary":
            if (not valid_number(value)):
                print_error("min-salary is not valid.")
                return False
        elif field == "--max-start-date":
            if (not valid_date(value)):
                print_error("max-start-date is not valid.")
                return False
        elif field == "--min-start-date":
            if (not valid_date(value)):
                print_error("min-start-date is not valid.")
                return False
        else:
            print_error("Invalid field is given.")
            return False
    return True


# valid update
def valid_update_inputs(inputs):
    if len(inputs) > 13 or len(inputs) % 2 != 1:
        print_error("Not a valid number of inputs.")
        return False

    if len(inputs) < 3:
        print_error("Not enough inputs.")
        return False

    employee_id = inputs[0]
    if (not valid_number(employee_id)):
        print_error("Not a valid employee id.")
        return False

    fields = inputs[1:]
    # see how many search field
    fields_number = int((len(fields)) / 2)

    seen = set()

    for i in range(0, fields_number * 2, 2):
        field = fields[i]
        value = fields[i + 1]

        if (field in seen):
            print_error("Don't use same field twice.")
            return False

        seen.add(field)

        if field == "--first-name":
            if (not valid_name(value)):
                print_error("first-name is not valid.")
                return False
        elif field == "--last-name":
            if (not valid_name(value)):
                print_error("last-name is not valid.")
                return False
        elif field == "--phone-number":
            if (not valid_number(value)):
                print_error("phone-number is not valid.")
                return False
        elif field == "--job-title":
            if (not valid_name(value)):
                print_error("job-title is not valid.")
                return False
        elif field == "--salary":
            if (not valid_number(value)):
                print_error("salary is not valid.")
                return False
        elif field == "--start-date":
            if (not valid_date(value)):
                print_error("start-date is not valid.")
                return False
        else:
            print_error("Invalid field is given.")
            return False
    return True


# validate delete
def valid_delete_inputs(inputs):
    if len(inputs) != 1:
        print_error(
            "Not a valid number of inputs, if you wish to delete an employee, please enter 4 then type the employee id.")
        return False
    if not valid_number(inputs[0]):
        print_error(
            "The employee id should be a digital number, please input a correct employee to delete.")
        return False
    return True


def valid_inputs(command, inputs):

    if command == "1":
        return valid_create_inputs(inputs)
    elif command == "2":
        return valid_search_inputs(inputs)
    elif command == "3":
        return valid_update_inputs(inputs)
    elif command == "4":
        return valid_delete_inputs(inputs)
