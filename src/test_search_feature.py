import unittest
import sys
import io
import os
from unittest.mock import patch
from main import run_app

test_filename = "test_storage.csv"


def create_users():
    file = open(test_filename, "w")

    file.write(
        "employee_id,first_name,last_name,phone_number,job_title,salary,start_date\n")
    file.write("1001,FirstName1,LastName,0411111111,barista,65000,01/01/23\n")
    file.write("1002,FirstName2,LastName,0411111112,chef,85000,01/01/21\n")
    file.write("1003,FirstName3,LastName3,0411111113,programmer,150000,01/01/20\n")
    file.write("1004,FirstName4,LastName4,0411111114,driver,75000,01/01/18\n")
    file.write("1005,FirstName5,LastName5,0411111115,farmer,95000,01/01/19\n")
    file.write("1006,FirstName6,LastName6,0411111116,barista,65000,01/01/21\n")

    file.close()


class Test_inputs(unittest.TestCase):
    @patch('builtins.input')
    def test_search_employee_id(self, mocked_input):
        create_users()
        mocked_input.side_effect = [
            "2",  # search command
            "--employee-id 1001",
            "5"  # exit
        ]

        saved_stdout = sys.stdout

        out = io.StringIO()
        sys.stdout = out

        run_app(filename=test_filename)

        output = out.getvalue().strip()

        sys.stdout = saved_stdout

        print("#######")
        print(output)
        print("#######")

        expected_output = "1001 FirstName1 LastName 0411111111 barista 65000 01/01/23"

        result = False
        if expected_output in output:
            print("id good")
            result = True
        else:
            print("id doesn't work")

        os.remove(test_filename)
        self.assertTrue(result)

    @patch('builtins.input')
    def test_search_employee_lastname(self, mocked_input):
        create_users()
        mocked_input.side_effect = [
            "2",  # search command
            "--last-name  LastName",
            "5"  # exit
        ]

        saved_stdout = sys.stdout

        out = io.StringIO()
        sys.stdout = out

        run_app(filename=test_filename)

        output = out.getvalue().strip()

        sys.stdout = saved_stdout

        print("#######")
        print(output)
        print("#######")

        expected_output1 = "1001 FirstName1 LastName 0411111111 barista 65000 01/01/23"
        expected_output2 = "1002 FirstName2 LastName 0411111112 chef 85000 01/01/21"

        result = False
        if expected_output1 and expected_output2 in output:
            print("last name ok")
            result = True
        else:
            print("last name does not work")

        os.remove(test_filename)
        self.assertTrue(result)

    @patch('builtins.input')
    def test_search_employee_date(self, mocked_input):
        create_users()
        mocked_input.side_effect = [
            "2",  # search command
            "--max-start-date  01/01/20",
            "5"  # exit
        ]

        saved_stdout = sys.stdout

        out = io.StringIO()
        sys.stdout = out

        run_app(filename=test_filename)

        output = out.getvalue().strip()

        sys.stdout = saved_stdout

        print("#######")
        print(output)
        print("#######")

        expected_output1 = "1003 FirstName3 LastName3 0411111113 programmer 150000 01/01/20"
        expected_output2 = "1004 FirstName4 LastName4 0411111114 driver 75000 01/01/18"
        expected_output3 = "1005 FirstName5 LastName5 0411111115 farmer 95000 01/01/19"
        result = False
        if expected_output1 and expected_output2 and expected_output3 in output:
            print(" date is good")
            result = True
        else:
            print("date doesn't work")

        # os.remove(test_filename)
        self.assertTrue(result)

    @patch('builtins.input')
    def test_search_employee_salary(self, mocked_input):
        create_users()
        mocked_input.side_effect = [
            "2",  # search command
            "--min-salary  75000",
            "5"  # exit
        ]

        saved_stdout = sys.stdout

        out = io.StringIO()
        sys.stdout = out

        run_app(filename=test_filename)

        output = out.getvalue().strip()

        sys.stdout = saved_stdout

        print("#######")
        print(output)
        print("#######")

        expected_output1 = "1002 FirstName2 LastName 0411111112 chef 85000 01/01/21"
        expected_output2 = "1004 FirstName4 LastName4 0411111114 driver 75000 01/01/18"
        expected_output3 = "1005 FirstName5 LastName5 0411111115 farmer 95000 01/01/19"
        expected_output4 = "1003 FirstName3 LastName3 0411111113 programmer 150000 01/01/20"
        result = False
        if expected_output1 and expected_output2 and expected_output3 and expected_output4 in output:
            print("salary is good")
            result = True
        else:
            print("salary doesn't work")

        os.remove(test_filename)
        self.assertTrue(result)

    


if __name__ == "__main__":
    unittest.main()
