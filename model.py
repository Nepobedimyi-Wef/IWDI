import os
from view import display_meny_for_working_with_txt_files, display_for_works_with_employees, display_for_m_r, display_meny_for_tasks, display_for_additional_functions, display_for_log_of_employees
from random import *
import time
import telebot
from telebot import types
import datetime

def new_employee():                             #Lля добавления нового сотрудника
    name = input("Enter the name of new employee, specialty/department, age: ")
    id = (randint(1, 10000))
    for line in open('txt2.txt'):
        while -1 != line.find(str(id),0):
            id = (randint(1,10000))
    file = open('txt2.txt', 'a')
    file.write(f'Id:{id,name}\n')
    print(f'Id:{id,name}\n')



def find_the_employee():                        #Для просмотра сотрудников
    the_name_for_find = input('Enter the employees name: ')
    with open("txt2.txt") as fisier:
        for line in fisier:
            if the_name_for_find in line:
                print(line, end='')

def print_the_list_of_employees():              #Для просмотра списка сотрудников
    list_of_employee = open('txt2.txt', 'r')
    file_contents = list_of_employee.read()
    print('The list employee:')
    print(file_contents)



def delete_an_employee():
    word_to_delete = input('Enter the ID of employee: ')
    # Открытие файла для чтения и чтение всех строк
    with open("txt2.txt", "r") as file:
        lines = file.readlines()
    # Открытие файла для записи и запись строк, кроме той, которую нужно удалить
    with open("txt2.txt", "w") as file:
        for line in lines:
            if word_to_delete not in line:
                file.write(line)
    file = open('remote_workers.txt', 'a')
    file.write(f'Id of remote worker: {word_to_delete}\n')


def change_password():
    password = input("Enter your password, please: ")
    with open("password.txt") as fisier:
        for line in fisier:
            if '' == line.replace(password, ''):
                new_password = input('Enter a new password: ')
                file = open('password.txt', 'w')
                file.write(new_password)
                return 1
            else:
                print('The wrong password was entered!')
                return 0

def products_reports():
        try:
            quantity_of_different_products = int(input('The number of different products: '))
            for i in range(quantity_of_different_products):
                seller = input('The company/seller who sold the product: ')
                product = input('Product name: ')
                product_quantity = input('Quantity of products: ')
                date = input('Date: ')
                file = open('products.txt', 'a')
                file.write(
                    f'Seller:{seller}, Product: {product}, Quantity of products:{product_quantity}, Date: {date}\n')
                print(f'Seller:{seller}, Product: {product}, Quantity of products:{product_quantity}, Date: {date}\n')

        except ValueError:
            print('Enter your answer correctly!')



def enter_the_monthly_report():
    sum_of_salary = 0
    sum_of_profit = 0
    # Открываем файл для чтения
    with open("txt2.txt", "r") as file:
        for line in file:
            print(line)  # Выводим имя сотрудника
            try:
                salary = int(input("Enter the employee's salary above: "))
                profit = int(input("Enter the employee's profit for the company: "))
                sum_of_salary += salary
                sum_of_profit += profit
            except ValueError:
                print("Enter the number correctly!")

    month = input("Enter the month: ")
    year = input("Enter the year: ")
    print("Calculating the company's profit:", sum_of_profit - sum_of_salary, " (", month, ".", year,".)")  #выводим прибыль
    file = open('monthly_report.txt', 'a')
    file.write(f'{month}.{year} = {sum_of_profit - sum_of_salary}\n') #Записываем прибыль в ткст файл


def print_the_list_of_monthly_report_about_profit():
    list_of_employee = open('monthly_report.txt', 'r')
    file_contents = list_of_employee.read()
    print('The list of monthly_report:')
    print(file_contents)

def print_the_list_of_monthly_report_about_products():
    list_of_products = open('products.txt', 'r')
    file_contents = list_of_products.read()
    print('The list of monthly reports of products:')
    print(file_contents)

def print_the_list_of_remote_workers():
    list_of_remote_workers = open('remote_workers.txt', 'r')
    file_contents = list_of_remote_workers.read()
    print('The list of monthly reports of products:')
    print(file_contents)

def work_with_monthly_reports():
    while True:
        display_for_m_r()
        action = input("Enter action: ")
        if action == '1':
            print_the_list_of_monthly_report_about_profit()
        elif action == '2':
            enter_the_monthly_report()
        elif action == '3':
            print_the_list_of_monthly_report_about_products()
        elif action == '4':
            products_reports()
        elif action == '5':
            print_the_list_of_remote_workers()
        elif action == '6':
            break

        else:
            print('Enter your choose correctly, please.')

def close_my_business():
    password = input("Enter your password, please: ")
    with open("password.txt") as fisier:
        for line in fisier:
            if '' == line.replace(password, ''):
                with open("txt2.txt", 'w') as txt2:
                    txt2.write("")
                with open("monthly_report.txt", 'w') as txt2:
                    txt2.write("")
                with open("password.txt", 'w') as txt2:
                    txt2.write("1234")
                with open('products.txt', 'w') as txt2:
                    txt2.write('')
                with open('tasks.txt', 'w') as txt2:
                    txt2.write('')
                with open('employee_attendance.txt', 'w') as txt2:
                    txt2.write('')
                with open('New_employees.txt', 'w') as txt2:
                    txt2.write('')
                with open('remote_workers.txt', 'w') as txt2:
                    txt2.write('')
                print('All business data has been deleted and the password has been changed to 1234!')
                return 1
            else:
                print('The wrong password was entered!')
                return 0




def working_with_txt_files():                          #MAIN
    while True:
        display_meny_for_working_with_txt_files()
        choose = input('Yor choose: ')
        if choose == '1':
            os.system('txt2.txt')
        elif choose == '2':
            os.system('monthly_report.txt')
        elif choose == '3':
            os.system('tasks.txt')
        elif choose == '4':
            os.system('products.txt')
        elif choose == '5':
            os.system('remote_workers.txt')
        elif choose == '6':
            os.system('employee_attendance.txt')
        elif choose == '7':
            os.system('New_employees.txt')
        elif choose == '8':
            break
        else:
            print('Enter your choose correctly, please')

def print_the_list_os_almost_new_employees():
    file = open('New_employees.txt', 'r')
    print(file.read())

def employees():
    while True:
        display_for_works_with_employees()
        choose = input('Enter your choice, please: ')
        if choose == '1':
            new_employee()
        elif choose == '2':
            find_the_employee()
        elif choose == '3':
            print_the_list_of_employees()
        elif choose == '4':
            delete_an_employee()
        elif choose == '5':
            print_the_list_os_almost_new_employees()
        elif choose == '6':
            break
def create_new_task():
    id_of_employee = input('Enter an ID of employee:  ')
    task_for_employee = input('Enter a task for the employee: ')
    file = open('tasks.txt', 'a')
    file.write(f'ID, {id_of_employee}, Task: {task_for_employee}\n')
    print(f'Id:{id_of_employee}, Task: {task_for_employee}\n')

def print_the_list_of_tasks_for_employy():
    list_of_tasks = open('tasks.txt', 'r')
    list_of_tasks = list_of_tasks.read()
    print('The list of tasks:')
    print(list_of_tasks)

def delete_a_task():
    word_to_delete = input('Enter the ID of employee: ')
    # Открытие файла для чтения и чтение всех строк
    with open("tasks.txt", "r") as file:
        lines = file.readlines()
    # Открытие файла для записи и запись строк, кроме той, которую нужно удалить
    with open("tasks.txt", "w") as file:
        for line in lines:
            if word_to_delete not in line:
                file.write(line)
def tasks():
    while True:
        display_meny_for_tasks()
        choice = input('Enter your choice: ')
        if choice == '1':
            create_new_task()
        elif choice == '2':
            print_the_list_of_tasks_for_employy()
        elif choice == '3':
            delete_a_task()
        elif choice == '4':
            break
        else:
            print('Enter your choice correctly, please!')

def mark_the_time():
    try:
        timer = int(input('Enter time: '))
        timer = timer * 60
        print(f'Ok, wait {timer // 60} minute/s.')
        time.sleep(timer)
        os.system('alarm__clock.m4r')
    except ValueError:
        print('Enter your answer correctly!')
def telebot_for_employees():
    TOKEN = 'ТОКЕН'

    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start'])
    def welcome(message):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add()
        item1 = types.KeyboardButton("Apply to join the company")
        item2 = types.KeyboardButton("Find out about my assignments")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Hello, choose your case, please!',
                         reply_markup=markup
                         )

    @bot.message_handler(content_types=['text'])
    def talk(message):

        print("[log]: ", message.text)
        if message.text == 'Apply to join the company':
            bot.send_message(message.chat.id,
                             'Enter your first name, last name and phone number/email address, please.')
            bot.send_message(message.chat.id, 'Example of the application form: application, Mary Jones, +1**********')

        elif "application" in message.text:
            file = open('New_employees.txt', 'a')
            file.write(f'{message.text}\n')
            bot.send_message(message.chat.id, 'The application has been successfully submitted!')

        elif message.text == 'Find out about my assignments':
            bot.send_message(message.chat.id, 'Enter the word "ID", and your ID')
            bot.send_message(message.chat.id, 'Example: ID, 123456')

        elif "ID" in message.text:
            with open("tasks.txt") as fisier:
                for line in fisier:
                    if message.text in line:
                        bot.send_message(message.chat.id, line)

        else:
            bot.send_message(message.chat.id, 'Sorry, i dont understand it.')

    bot.polling(none_stop=True)

def additional_functions():
    while True:
        display_for_additional_functions()
        choice = input('Enter your choice:')
        if choice == '1':
            change_password()
        elif choice == '2':
            print('Do you want to enable a telegram bot?')
            print(' If you want to return to the main menu later, you will have to restart the application.')
            while True:
                choice_2 = input('Your choice(+ or -):  ')
                if choice_2== '+':
                    telebot_for_employees()
                elif choice_2 == '-':
                    break
                else:
                    print('Enter your choice correctly, please.')
        elif choice == '3':
            mark_the_time()
        elif choice == '4':
            break
        else:
            print('Enter your choice correctly, please.')

def log_attendance(employee_id, date, time):
    with open('employee_attendance.txt', 'a') as file:
        file.write(f"Id: {employee_id}, Logs: {date},{time}\n")
        print(f"Id: {employee_id},Logs: {date},{time}\n")

def enter_log_of_employees():
    try:
        n = int(input('How many employees do you want to mark: '))
        for i in range(n):
            employee_id = input('Enter id of employee: ')
            current_date = datetime.date.today()
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            log_attendance(employee_id, current_date, current_time)
    except:
        print('The answer was entered incorrectly!')

def print_logs_of_employees():
    file = open('employee_attendance.txt', 'r')
    print(file.read())

def find_logs():
    the_name_for_find = input('Enter the employees ID: ')
    with open("employee_attendance.txt") as fisier:
        for line in fisier:
            if the_name_for_find in line:
                print(line, end='')

def log_of_employees():
    while True:
        display_for_log_of_employees()
        choice = input('Enter your choice: ')
        if choice == '1':
            enter_log_of_employees()
        elif choice == '2':
            print_logs_of_employees()
        elif choice == '3':
            find_logs()
        elif choice == '4':
            break
