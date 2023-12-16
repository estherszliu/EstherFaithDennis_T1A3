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

# valid search 
def valid_search_inputs(inputs):
    if len(inputs) > 20 or len(inputs) % 2 != 0:
        print("ERROR: Not a valid number of inputs")
        return False
    
    fields = inputs[2:]
    # see how many search field
    fields_number = int((len(inputs) - 2) / 2)
    
    seen = set()
    
    for i in range(0, fields_number * 2, 2):
        field = fields[i]
        value = fields[i+1]
     
        if (field in seen):
            print("ERROR: Don't use same field twice")
            return False

        seen.add(field)

        if field == "--employee-id":
            if (not valid_number(value)):
                print("ERROR: employee-id is not valid")
                return False    
        elif field == "--first-name":
            if (not valid_name(value)):
                print("ERROR: first-name is not valid")
                return False     
        elif field == "--last-name":
            if (not valid_name(value)):
                print("ERROR: last-name is not valid")
                return False 
        elif field == "--phone-number":
            if (not valid_number(value)):
                print("ERROR: phone-number is not valid")
                return False
        elif field == "--job-title ":
            if (not valid_name(value)):
                print("ERROR: job-title is not valid")
                return False
        elif field == "--max-salary":
            if (not valid_number(value)):
                print("ERROR: max-salary is not valid")
                return False
        elif field == "--min-salary":
            if (not valid_number(value)):
                print("ERROR: min-salary is not valid")
                return False
        elif field == "--max-start-date":
            if (not valid_date(value)):
                print("ERROR: max-start-date is not valid")
                return False
        elif field == "--min-start-date":
            if (not valid_date(value)):
                print("ERROR: min-start-date is not valid")
                return False
        else:
            print("ERROR: Invalid field is given")
            return False 
    return True

# valid update 
def valid_update_inputs(inputs):
    if len(inputs) > 15 or len(inputs) % 2 != 1:
        print("ERROR: Not a valid number of inputs")
        return False
    
    if len(inputs) < 5:
        print("ERROR: Not enough inputs")
        return False
    
    employee_id = inputs[2]
    if (not valid_number(employee_id)):
        print("ERROR: Not a valid employee id")
        return False

    
    fields = inputs[3:]
    # see how many search field
    fields_number = int((len(inputs) - 2) / 2)
    
    seen = set()
    
    for i in range(0, fields_number * 2, 2):
        field = fields[i]
        value = fields[i+1]
     
        if (field in seen):
            print("ERROR: Don't use same field twice")
            return False

        seen.add(field)
    
        if field == "--first-name":
            if (not valid_name(value)):
                print("ERROR: first-name is not valid")
                return False     
        elif field == "--last-name":
            if (not valid_name(value)):
                print("ERROR: last-name is not valid")
                return False 
        elif field == "--phone-number":
            if (not valid_number(value)):
                print("ERROR: phone-number is not valid")
                return False
        elif field == "--job-title ":
            if (not valid_name(value)):
                print("ERROR: job-title is not valid")
                return False
        elif field == "--salary":
            if (not valid_number(value)):
                print("ERROR: salary is not valid")
                return False
        elif field == "--start-date":
            if (not valid_date(value)):
                print("ERROR: start-date is not valid")
                return False
        else:
            print("ERROR: Invalid field is given")
            return False 
    return True
    

# validate delete
def valid_delete_inputs(inputs):
    if len(inputs) != 3:
        print("ERROR: Not a valid number of inputs, if you wish to delete an employee, please input delete follow by employee id")
        return False
    if not valid_number(inputs[2]):
        print("ERROR: The employee id should be a digital number, please input a correct employee to delete.")
        return False
    return True

def valid_inputs(inputs):
    
    # check if command correct
    if (len(inputs) < 2 or not valid_command(inputs[1])):
        print("ERROR: Program needs a valid command")
        return False

    if inputs[1] == "create":
        return valid_create_inputs(inputs)
    elif inputs[1] == "search":
        return valid_search_inputs(inputs)
    elif inputs[1] == "update":
        return valid_update_inputs(inputs)
    elif inputs[1] == "delete":
        return valid_delete_inputs(inputs)