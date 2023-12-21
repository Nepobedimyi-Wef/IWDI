from view import display_menu
from model import close_my_business, work_with_monthly_reports, working_with_txt_files, employees, tasks, additional_functions, log_of_employees
while True:
    password = input("Enter your password, please: ")
    with open("password.txt") as fisier:
        for line in fisier:
            if '' == line.replace(password,''):
                print("Hello, manager")
                while True:
                    display_menu()
                    choose = input('Enter your case: ')
                    if choose == '1':
                        employees()
                    elif choose == '2':
                        working_with_txt_files()
                    elif choose == '3':
                        work_with_monthly_reports()
                    elif choose == '4':
                        close_my_business()
                        break
                    elif choose == '5':
                        tasks()
                    elif choose == '6':
                        additional_functions()
                    elif choose == '7':
                        log_of_employees()
                    elif choose == '8':
                        print('Goodbye!')
                        break  # Останавливаем цикл
                    else:
                        print('Enter your case correctly, please!')
            else:
                print("Wrong password!")
