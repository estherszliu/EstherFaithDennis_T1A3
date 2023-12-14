from datetime import datetime

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
    if len(inputs) != 9:
        print("ERROR: Incorrect number of arguments given, please input format with space seperate as create employee_id first_name last_name phone_number job_title salary start_date")
        return False

    # validate_ employee id - value
    if not valid_number(inputs[2]):
        print("ERROR: The employee id should be a digital number.")
        return False

    # validate first name as alpha input
    if not valid_name(inputs[3]):
        print("ERROR: The first name is invalid, please input a valid name")
        return False

    # validate last name as alpha input
    if not valid_name(inputs[4]):
        print("ERROR: The last name is invalid, please input a valid name")
        return False

    # validate phone number as all digit
    if not valid_number(inputs[5]):
        print("ERROR: The phone number should be a digital number.")
        return False

    # validate job title as all alpha
    if not valid_name(inputs[6]):
        print("ERROR: The job title is invalid, please input an alpha name for job title.")
        return False
    
    # validate salary as all digit
    if not valid_number(inputs[7]):
        print("ERROR: The salary should be a digital and a whole number.")
        return False

    # validate start date
    if not valid_date(inputs[8]):
        print("ERROR: Invalid start date, please input format as dd/mm/yy")
        return False
    
    return True

def valid_inputs(inputs):
    
    # check if command correct
    if (len(inputs) < 2 or not valid_command(inputs[1])):
        print("ERROR: Program needs a valid command")
        return False

    if inputs[1] == "create":
        return valid_create_inputs(inputs)