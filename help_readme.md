# How to use Employee Directory

You can run the run_app.sh by type in temnial `./run_app.sh` it will download the feature you need to run the program. And run_tests.sh is for test the program by type in the terminal `./run_tests.sh`

# run_tests.sh
The run_tests.sh is to run the test, when you run this file, it will test the program. If type ./run_tests.sh it will return the result, if type ./run_tests.sh -v it will print the result and the detail of test. 

# run_app.sh
* python3 -m venv .venv (downloadn virtual environment)
* source .venv/bin/activate (activate the source)
* pip3 install --disable-pip-version-check --quiet -r requirements.txt (download colored, the color store in requirements.txt)
* python3 main.py (python3 to run the main.py)

to run that ,  you need to type: ./run_app.sh it will check whether you already download python and colore and creat virtual emvironment for you if you have download in the file. 

Once you run that, it will print a welcome message to you, and ask you to choose from one of the commands. 
```
Welcome to the Employee Directory

Choose from one of these commands
  Enter 1 to creates a new employee
  Enter 2 to search for an employee
  Enter 3 to update the data for one employee
  Enter 4 to delete one employee
  Enter 5 to exit

Enter your command: 
``````

You can enter the option such as 1 to created or 2 to search by enter just the number. 

### 1
Enter 1 will print the messout to show you the format you need to input for create new employee. If the employee file has not been create, it will auto create a file name `storage.csv`, then store the employee data in the file. If the file already exist, it will create a new employee inside of the file. Before create it, the program will check whether the employee id is exist, avoid duplicate employee id. Once it check it is not exsit, it will write in the file. Below it is the example for how it show on the command line,

```
Enter the new employee data in this format
    <employee-id> <first-name> <last-name> <phone-number> <job-title> <salary> <start-date>

Enter the new employee data: 
```

Then you can input the new employee data according to the format with the space, for example, 
```
1001 Dave Jone 04004000 manager 85000 01/02/22
```

After input that, will have a message to show the new employee has been created, and ask you to choose one of the commands again, until you enter 5 to exit. For example,
```
New employee created: 1001 Dave Jone 04004000 manager 85000 01/01/22

Choose from one of these commands
  Enter 1 to creates a new employee
  Enter 2 to search for an employee
  Enter 3 to update the data for one employee
  Enter 4 to delete one employee
  Enter 5 to exit

Enter your command: 
```

### 2

Enter 2 for search, after enter 2, it will print some messages to show you how to search the employee data. As below,
```
Enter the search fields exactly like left column and space follow by the contents you want to find, leave blank if you want to see all users
    --employee-id     <employee-id>
    --first-name      <first-name>
    --last-name       <last-name>
    --phone-number    <phone-number>
    --job-title       <job-title>
    --max-salary      <max-salary>
    --min-salary      <min-salary>
    --max-start-date  <max-start-date>
    --min-start-date  <min-start-date>

Enter the employee search fields: 

```
You can choose the field which you want to search, for example, if you want to search employee by id, could type it, --employee-id 1001, below as this example,
```

Enter the search fields exactly like left column and space follow by the contents you want to find, leave blank if you want to see all users
    --employee-id     <employee-id>
    --first-name      <first-name>
    --last-name       <last-name>
    --phone-number    <phone-number>
    --job-title       <job-title>
    --max-salary      <max-salary>
    --min-salary      <min-salary>
    --max-start-date  <max-start-date>
    --min-start-date  <min-start-date>

Enter the employee search fields: --employee-id 1001
```
after enter it, it will show the employee if it is found, for if the employee id not exist, it will show a message says, No employees match your search. Again, after the search result, it will have the message ask you to choose one of the commands, until you enter 5 to exit.

### 3

Enter 3 to update the employee data. Once you enter 3, it will have the message to show you how to input the field which you want to update. You need to input the employee id space field then space new data. For example, 1001 --last-name Dennis
```
Enter the employee id followed by fields to be updated: 1001 --last-name Dennis

Employee updated: 1001 Dave Dennis 04004000 manager 85000 01/01/22

Choose from one of these commands
  Enter 1 to creates a new employee
  Enter 2 to search for an employee
  Enter 3 to update the data for one employee
  Enter 4 to delete one employee
  Enter 5 to exit

Enter your command: 
```
After input the update data, it will change according the input to the correct field. Again, it will ask you to enter your next command if you still have done your enquire. 

### 4

Enter 4 to delete employee. After enter 4, it will have ask you to enter the employee id which you want to delete. 
```
Enter your command: 4


Enter the employee id to be deleted: 1001

Employee deleted: 1001 Dave Dennis 04004000 manager 85000 01/01/22

Choose from one of these commands
  Enter 1 to creates a new employee
  Enter 2 to search for an employee
  Enter 3 to update the data for one employee
  Enter 4 to delete one employee
  Enter 5 to exit

Enter your command: 
```
After you input the employee id, it will print a message to you show you the deleted employee details. Again, you can enter the next command after this. 

### 5
Enter 5 to exit the program. 