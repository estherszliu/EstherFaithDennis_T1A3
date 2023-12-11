import csv

file_name = "directory.csv"

try:

    employeeDict = open(file_name, "r")
    employeeDict.close()
    print("trying")

except FileNotFoundError:
    employeeDict = open(file_name, "w")
    employeeDict.write("employee-id, first-name, last-name, phone-number, job-title, salary, start-date\n" )
    employeeDict.close()
    print("create file")