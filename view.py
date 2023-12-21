def my_decorator(say_hello):
    def wrapper():
        print("______________________________")
        say_hello()
        print("______________________________")
    return wrapper

@my_decorator
def display_menu():
    print('1 - Section - "Employees"')
    print('2 - Section - "Working with txt files"')
    print('3 - Section - "Actions with profit reports"')
    print('4 - Section - "Close my business"')
    print('5 - Section - "Tasks"')
    print('6 - Section - "Additional functions"')
    print('7 - Section - "Employee attendance"')
    print('8 - Leave')

@my_decorator
def display_meny_for_working_with_txt_files():
    print('1 - Employee (txt2.txt)')
    print('2 - Monthly reports (monthly_report.txt)')
    print('3 - Tasks for employees (tasks.txt)')
    print('4 - Reports of products (products.txt)')
    print('5 - The history of remote workers (remote_workers.txt)')
    print('6 - Employee attendance (employee_attendance.txt)')
    print('7 - New employees (New_employees.txt)')
    print('8 - Leave')

@my_decorator
def display_for_m_r():
    print('1 - View a list of all reports about profit.')
    print('2 - Add a new report about profit.')
    print('3 - View a list of all reports about products.')
    print('4 - Add a new report about products.')
    print('5 - The history of dismissal of employees')
    print('6 - Leave.')

@my_decorator
def display_for_works_with_employees():
    print('1 - Add a new employee')
    print('2 - Find out information about the employee/employees')
    print('3 - Print the list of employees')
    print('4 - Delete an employee')
    print('5 - Print the list of almost new employees')
    print('6 - Leave')

@my_decorator
def display_meny_for_tasks():
    print('1 - Add a new task for employee')
    print('2 - Print the list of tasks')
    print('3 - Delete task')
    print('4 - Leave')
@my_decorator
def display_for_additional_functions():
    print('1 - Change the password')
    print('2 - Enable the telegram bot')
    print('3 - Timer')
    print('4 - Leave')

@my_decorator
def display_for_log_of_employees():
    print('1 - Add a new logs')
    print('2 - Print the list of logs')
    print('3 - Find employee attendance by ID')
    print('4 - Leave')
