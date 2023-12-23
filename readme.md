# THIS IS ESTHER FAITH DENNIS T1A3 

## Git repo
[link to git](https://github.com/estherszliu/EstherFaithDennis_T1A3)

## Presentation
[Link to presentation](https://youtu.be/p2Idm8wSP7U)

# App Usage
## Dependencies
This app requires Python 3 to be installed

All other dependency is installed by virtual env. 

## Running the App
The app can be run with these steps
* Navigate to the `/src` directory
* Run the bash script `./run_app.sh`

## Using the App
### Choose a Feature
The app will ask you to choose a feature
* Enter 1 to create a new employee
* Enter 2 to search for employees
* Enter 3 to update an employee
* Enter 4 to delete an employee
* Enter 5 to exit the app

### Create employees
When creating an employee, the app ask to enter some data for the new employee. Enter the data in this format
```
<employee id> <first name> <last name> <phone number> <job title> <salary> <start date>
```

Hear is some examples
```
1001 Esther Dennis 0455456123 Chef 85000 22/07/22
1002 Simon Brown 0455456124 Waiter 65000 15/09/22
```

The app will print a success or fail message depending on the input. If the user succeed it will print the new user to the terminal. 

### Search employees
When searching an employee, the app ask to enter some search field to search the employees. Enter the data in this format.
```
--employee-id     <employee id>
--first-name      <first name>
--last-name       <last name>
--phone-number    <phone number>
--job-title       <job title>
--max-salary      <max salary>
--min-salary      <min salary>
--max-start-date  <max start date>
--min-start-date  <min start date>
```

Enter as many fields as you want to search for. Only users that meet all the search field will be printed to the terminal. 

Hear is some examples
```
Example 1: --employee-id 1001
Example 2: --first-name Esther
Example 3: --min-salary 60000 --max-salary 100000
Example 4: --job-title Chef --max-salary 60000 
```

If you want to see all the employees, don't enter any search fields and just press enter.

### Update employees
When update employee, the app ask to enter the employee id and the fields to be update. 
```
employee update <employee id> 
    --first-name    <first name> 
    --last-name     <last name> 
    --phone-number  <phone number> 
    --job-title     <job title> 
    --salary        <salary> 
    --start-date    <start date> 
```
Hear is some examples
```
1001 --job-title "Senior Chef" --salary 100000
1002 --phone-number 0455456777 
```

The new employee details will be printed to the terminal if the update succeed. Otherwise error message will be printed. 

### Delete employees
When delete employee, the app asks to enter the employee id to be deleted. 
```
<employee id>
```

If the employee id is correct, the app will print a message to the terminal showing the employee that was deleted. 

### Exit
If the user choose 5 to exit, the app will no longer be running. Rerun `./run_app.sh` to choose more commands.

## More Help
Also more help can be read in the `docs/help_readme.md` file. 

# Project Planning
To do the project planning I did these things
* Decide how the user interface for the app
* Set up a trello board for the app
* Create common functions need for all the feature
    * Employee class
    * Csv helper
    * Validation functions
* Write the create feature
* Write the search feature
* Write the update feature
* Write the delete feature
* Write the tests

## Common functionality
These functions and class were important to all features of the app. I wrote them first before start on the main features.
* Create Employee class
    * Priority: High
    * Due Date: 11 Dec 2023 

* reading and writing in csv file
    * Priority: High
    * Due Date: 12 Dec 2023 
* Choose the right feature function for the command that the user chose

### Validate inputs
Validate inputs was very important to avoid errors. There was a lot of inputs from the user to check. These are tasks I made to validate the inputs. 
- [ ] Validate employee ID
    * Priority: High
    * Due Date: 12 Dec 2023 
- [ ] Validate first name
    * Priority: High
    * Due Date: 12 Dec 2023 
- [ ] Validate last name
    * Priority: High
    * Due Date: 12 Dec 2023 
- [ ] Validate phone number
    * Priority: High
    * Due Date: 13 Dec 2023 
- [ ] Validate job title
    * Priority: High
    * Due Date: 13 Dec 2023 
- [ ] Validate salary
    * Priority: High
    * Due Date: 13 Dec 2023 
- [ ] Validate start date
    * Priority: High
    * Due Date: 13 Dec 2023 



## Feature - Create Employee
I will explain a plan for create employee feature

### How it will be implemented
It will be implemented in two parts, validate and run.
  * `def valid_create_inputs(inputs)` for validate 
  * `def create_employee(employee_data)` function to run the feature. 
  
  The input data will be a list of inputs given by the user and will be validate as the first step. The create feature will
  * Read employees from the csv
  * Check if the employee id exist
  * Create a new employee and add to the list
  * Write the employees to the csv 

### Task checklist for create employees
I used these task to implement the feature
- [ ] Validate the number of input
    * Priority: High
    * Due Date: 12 Dec 2023 
- [ ] Validate the input is correct
    * Priority: High
    * Due Date: 13 Dec 2023 
- [ ] Print fail message to the user if the input is incorrect
    * Priority: Medium
    * Due Date: 14 Dec 2023 
- [ ] Write employee data to csv file
    * Priority: High
    * Due Date: 14 Dec 2023 
- [ ] Print fail message to the user if writing to the file is fail
    * Priority: Medium
    * Due Date: 14 Dec 2023 
- [ ] Print success message to the user
    * Priority: Medium
    * Due Date: 14 Dec 2023 

Most the task is high priority because create feature is needed for all other feature to work properly. 


## Feature - Search employee
I will explain a plan for search employee feature

### How it will be implemented
It will be implemented in two parts, validate and run.
  * `def valid_search_inputs(inputs)` for validate 
  * `def search_employee(search_data)` function to run the feature. 
  
  The input data will be a list of inputs given by the user and will be validate as the first step. The search feature will
  * Read employees from the csv
  * Find employees that match the search fields
  * Add those match employee to a list
  * Print all match employee to the terminal

### Task checklist for search employees
I used these task to implement the feature
- [ ] Validate the input is correct
    * Priority: High
    * Due Date: 15 Dec 2023 
- [ ] Print fail message to the user if the input incorrect
    * Priority: Medium
    * Due Date: 15 Dec 2023 
- [ ] Validate the input is match the employee data
    * Priority: High
    * Due Date: 15 Dec 2023 
- [ ] Print fail message to the user if the input can not found in the  employee data
    * Priority: Medium
    * Due Date: 15 Dec 2023 
- [ ] Print the employee data to the user
    * Priority: Medium
    * Due Date: 15 Dec 2023 

Most the task is high priority because search feature is needed for all other feature to work properly. 

## Feature - Update employee
I will explain a plan for update employee feature

### How it will be implemented
It will be implemented in two parts, validate and run.
  * `def valid_update_inputs(inputs)` for validate 
  * `def update_employee(search_data)` function to run the feature. 
  
  The input data will be a list of inputs given by the user and will be validate as the first step. The update feature will
  * Read employees from the csv
  * Find the employee to update using the employee id give by the user
  * Update the emplyee details that match the fields give by the user
  * Write the changed employee back to the csv file

### Task checklist for update employees
I used these task to implement the feature
- [ ] Validate the input is correct
    * Priority: High
    * Due Date: 16 Dec 2023 
- [ ] Print fail message to the user if the input incorrect
    * Priority: Medium
    * Due Date: 16 Dec 2023 
- [ ] Validate the input is match the employee data
    * Priority: High
    * Due Date: 16 Dec 2023 
- [ ] Print fail message to the user if the input can not found in the  employee data
    * Priority: Medium
    * Due Date: 16 Dec 2023 
- [ ] Print the employee data to the user
    * Priority: Medium
    * Due Date: 16 Dec 2023 

Most the task is high priority because update feature is needed for all other feature to work properly. 

## Feature - Delete employee
I will explain a plan for delete employee feature

### How it will be implemented
It will be implemented in two parts, validate and run.
  * `def valid_delete_inputs(inputs)` for validate 
  * `def delete_employee(search_data)` function to run the feature. 
  
  The input data will be a list of inputs given by the user and will be validate as the first step. The update feature will
  * Read employees from the csv
  * Find the employee to delete using the employee id give by the user
  * Remove the employee from the list of employees
  * Write the other employees back to the csv file

### Task checklist for delete employees
I used these task to implement the feature
- [ ] Validate the input is correct
    * Priority: High
    * Due Date: 16 Dec 2023 
- [ ] Print fail message to the user if the input incorrect
    * Priority: Medium
    * Due Date: 16 Dec 2023 
- [ ] Validate the input is match the employee data
    * Priority: High
    * Due Date: 16 Dec 2023 
- [ ] Print fail message to the user if the input can not found in the  employee data
    * Priority: Medium
    * Due Date: 16 Dec 2023 
- [ ] Print the sucessful delete messege to the user
    * Priority: Medium
    * Due Date: 16 Dec 2023 

Most the task is high priority because delete feature is needed for all other feature to work properly. 

# Project mangement:

For the project mangement, I have been using Trello. I used three columns to keep track of the tasks
* To do: Tasks that I have not started yet.
* Doing: The task I am working on now.
* Done: The tasks that already are finished.

Below are some screenshots from doing the project.

![sceenshort1](./docs/image.png)
![sceenshort2](./docs/image-1.png)
![sceenshort3](./docs/image-2.png)
![delete employee](./docs/image-3.png)
![Doing test file](./docs/image-4.png)

# write Unittest for the app
I decided to write automated tests for my testing. This made it easy to check if the app work even after making change. 
* Write unittest test the create feature.
    * Check new user can be created
    * Check multiple new user can be created
    * Check if error when new user has same id as other user. 

* Write unitest test the search feature. 
    * Check if search employee id is working
    * Check if search first name is working
    * Check if search start date is working
    * Check if search salary is working

# Code Style Guide
For code styling, I have chosen to usd PEP 8 – Style Guide for Python Code.Here is the link to [link to PEP8](https://peps.python.org/pep-0008/) (peps.python.org, n.d.) PEP8 helps to organise the code more consistency and help to improve the readerblity. I have been using the autopep8 to auto adjust the code style for me. Here is the link to [link to autopep8](https://pypi.org/project/autopep8/) (Hattori, n.d.) This autopep8 is a auto adjustment of PEP 8, once you download it and excute it, it will change the file style automaticaly.

## Reference
peps.python.org. (n.d.). PEP 8 – Style Guide for Python Code | peps.python.org. [online] Available at: https://peps.python.org/pep-0008/#naming-conventions.

Hattori, H. (n.d.). autopep8: A tool that automatically formats Python code to conform to the PEP 8 style guide. [online] PyPI. Available at: https://pypi.org/project/autopep8/.