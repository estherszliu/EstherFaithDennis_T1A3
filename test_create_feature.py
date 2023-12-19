import unittest
import os
from unittest.mock import patch
from main import run_app

test_filename = "test_storage.csv"

def check_csv(expected_employees):
    file = open(test_filename, "r")

    header = file.readline()

    if header != "employee_id,first_name,last_name,phone_number,job_title,salary,start_date\n":
        file.close()
        return False
    
    i = 0
    for data in file:
        if data.strip() != expected_employees[i]:
            print("Error, employee data not match")
            file.close()
            return False
        i += 1

    file.close()
    if i == len(expected_employees):
        return True
    else:
        return False


class Test_inputs(unittest.TestCase):
    @patch('builtins.input')
    def test_create_new_employee(self, mocked_input):
        mocked_input.side_effect = [
            "1", # create command
            "1234 Esther Dennis 0455111222 Barista 65000 01/01/23", 
            "5" # exit
        ]
        run_app(filename = test_filename)

        result = check_csv([
            "1234,Esther,Dennis,0455111222,Barista,65000,01/01/23"
        ])
        os.remove(test_filename)
        self.assertTrue(result)

    @patch('builtins.input')
    def test_create_many_new_employee(self, mocked_input):
        mocked_input.side_effect = [
            "1", # create command
            "1234 Esther Dennis 0455111222 Chef 165000 01/01/22", 
            "1", # create command
            "1235 James Dee 0455111223 Barista 65000 01/01/23", 
            "1", # create command
            "1236 Esther Liu 0455111224 Cook 95000 01/01/23", 
            "5" # exit
        ]
        run_app(filename = test_filename)

        result = check_csv([
            "1234,Esther,Dennis,0455111222,Chef,165000,01/01/22",
            "1235,James,Dee,0455111223,Barista,65000,01/01/23",
            "1236,Esther,Liu,0455111224,Cook,95000,01/01/23"
        ])
        os.remove(test_filename)
        self.assertTrue(result)

    @patch('builtins.input')
    def test_create_exist_new_employee(self, mocked_input):
        mocked_input.side_effect = [
            "1", # create command
            "1234 Esther Dennis 0455111222 Barista 65000 01/01/23",
            "1", # create command
            "1234 Adam LastName 0455111225 Chef 85000 25/01/22",  
            "5" # exit
        ]
        run_app(filename = test_filename)

        result = check_csv([
            "1234,Esther,Dennis,0455111222,Barista,65000,01/01/23"
        ])
        os.remove(test_filename)
        self.assertTrue(result)   

if __name__ == "__main__":
    unittest.main()