import smtplib
import threading
import random

from users import People
from logs import log_decorator

from file_managing import admins_manager, teachers_manager


                                        # Admin
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


@log_decorator
def add_admin():
    full_name = input("Enter new admin full name: ").strip().capitalize()
    phone_number = input("Enter new admin phone number: ").strip()
    if len(phone_number) < 7 and "+" in phone_number:
        print("Incorrect gender!")
        add_admin()
    gender = input("Enter new admin gender (Famale/Male): ").strip().capitalize()
    if gender != "Famale" and gender != "Male":
        print("Incorrect gender!")
        add_admin()
    age = input("Enter new admin age: ").strip().capitalize()
    gmail = input("Enter new admin gmail: ").strip().lower()
    if not "@gmail.com" in gmail:
        print("Incorrect gmail!")
        add_admin()
    password = input("Enter your password: ").strip()
    confirm_password = input("Enter your confirm password: ").strip()

    person = People(full_name, phone_number, gender, age, gmail, password)
    if not person.check_password(confirm_password):
        print("Passwords do not match")
        return add_admin()

    person.password = People.hash_password(password)
    admins_manager.add_data(data=person.__dict__)
    print("\nSaved")
    return "menu"


@log_decorator
def see_admin_list(inf):
            inf_list = f""" 
    Full name: {inf['full_name']}
    Phone number: {inf['phone_number']}
    Gender: {inf['gender']} 
    Age: {inf['age']}
    Gmail: {inf['gmail']}
    Password: {inf['password']}
    Date: {inf['date']}
    Active: {inf['is_login']}
"""  
            return inf_list


@log_decorator
def see_all_admin():
    all_admins = admins_manager.read()
    num = 0
    for admin in all_admins:
        num += 1
        inf = see_admin_list(admin)
        f"""
{print(num)}:
    {print(inf)}
"""
    return "menu"


@log_decorator    
def search_admin():
    admin_input: str = input('Enter should admin phone number: ').strip()
    all_admins = admins_manager.read()

    for admin in all_admins:
        if admin_input in admin['phone_number']:
            inf = see_admin_list(admin)
            print(inf)
    return "menu"


@log_decorator    
def update_admin_data():
    phone_number = input("Enter admin phone number: ")
    all_admins = admins_manager.read()
    for admin in all_admins:
        if admin['phone_number'] == phone_number:
            new_phone_number = input("Enter admin's new phone number: ").strip()
            if len(new_phone_number) < 7 and "+" in new_phone_number:
                print("Incorrect gender!")
                update_admin_data()
            new_full_name = input("Enter admin's new full name: ").capitalize().strip()
            new_gender = input("Enter admin's new genderFamale/Male): ").capitalize().strip()
            if new_gender != "Famale" and new_gender != "Male":
                print("Incorrect gender!")
                update_admin_data()
            new_age = input("Enter admin's new age: ").strip()
            new_gmail = input("Enter admin's new gmail: ").strip()
            if not "@gmail.com" in new_gmail:
                print("Incorrect gmail!")
                update_admin_data()
            new_password = input("Enter admin's new password: ").strip()
            password = People.hash_password(new_password)
            update_admin = People(new_full_name, new_phone_number, new_gender, new_age, new_gmail, password)
            admins_manager.update_data(admins_manager, phone_number, update_admin.__dict__, 'phone_number')
            print("\nAdmin updated successfully!")
        else:
            print("\nAdmin not found")
    return "menu"


@log_decorator
def delete_admin():
    phone_number = input("Enter admin phone number: ").strip().lower()
    all_admin = admins_manager.read()
    new_admins = []
    for admin in all_admin:
        if admin['phone_number'].lower() != phone_number.lower():
            new_admins.append(admin)
    admins_manager.write(new_admins)
    print('\nAdmin deleted successfully!\n')
    return "menu"


                                            # Teacher
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


@log_decorator
def add_teacher():
    full_name = input("Enter new teacher full name: ").strip().capitalize()
    phone_number = input("Enter new teacher phone number: ").strip()
    if len(phone_number) < 7 and "+" in phone_number:
        print("Incorrect gender!")
        add_teacher()
    gender = input("Enter new teacher gender (Famale/Male): ").strip().capitalize()
    if gender != "Famale" and gender != "Male":
        print("Incorrect gender!")
        add_teacher()
    age = input("Enter new teacher age: ").strip().capitalize()
    gmail = input("Enter new teacher gmail: ").strip().lower()
    if not "@gmail.com" in gmail:
        print("Incorrect gmail!")
        add_teacher()
    password = input("Enter your password: ").strip()
    confirm_password = input("Enter your confirm password: ").strip()

    person = People(full_name, phone_number, gender, age, gmail, password)
    if not person.check_password(confirm_password):
        print("Passwords do not match")
        return add_teacher()

    person.password = People.hash_password(password)
    teachers_manager.add_data(data=person.__dict__)
    print("\nSaved")
    return "menu"


@log_decorator
def see_teacher_list(inf):
            inf_list = f""" 
    Full name: {inf['full_name']}
    Phone number: {inf['phone_number']}
    Gender: {inf['gender']} 
    Age: {inf['age']}
    Gmail: {inf['gmail']}
    Password: {inf['password']}
    Date: {inf['date']}
    Active: {inf['is_login']}
"""  
            return inf_list


@log_decorator
def see_all_teacher():
    all_teachers = teachers_manager.read()
    num = 0
    for teacher in all_teachers:
        num += 1
        inf = see_teacher_list(teacher)
        f"""
{print(num)}:
    {print(inf)}
"""
    return "menu"


@log_decorator
def add_teacher():
    full_name = input("Enter new teacher full name: ").strip().capitalize()
    phone_number = input("Enter new teacher phone number: ").strip()
    if len(phone_number) < 7 and "+" in phone_number:
        print("Incorrect gender!")
        add_teacher()
    gender = input("Enter new teacher gender (Famale/Male): ").strip().capitalize()
    if gender != "Famale" and gender != "Male":
        print("Incorrect gender!")
        add_teacher()
    age = input("Enter new teacher age: ").strip().capitalize()
    gmail = input("Enter new teacher gmail: ").strip().lower()
    if not "@gmail.com" in gmail:
        print("Incorrect gmail!")
        add_teacher()
    password = input("Enter your password: ").strip()
    confirm_password = input("Enter your confirm password: ").strip()

    person = People(full_name, phone_number, gender, age, gmail, password)
    if not person.check_password(confirm_password):
        print("Passwords do not match")
        return add_teacher()

    person.password = People.hash_password(password)
    teachers_manager.add_data(data=person.__dict__)
    print("\nSaved")
    return "menu"


@log_decorator    
def search_teacher():
    teachers_input: str = input('Enter should teacher phone number: ').strip()
    all_teachers = teachers_manager.read()

    for teachers in all_teachers:
        if teachers_input in teachers['phone_number']:
            inf = see_admin_list(teachers)
            print(inf)
    return "menu"


@log_decorator    
def update_teachers_data():
    phone_number = input("Enter teachers phone number: ")
    all_teachers = teachers_manager.read()
    for teacher in all_teachers:
        if teacher['phone_number'] == phone_number:
            new_phone_number = input("Enter teacher's new phone number: ").strip()
            if len(new_phone_number) < 7 and "+" in new_phone_number:
                print("Incorrect gender!")
                update_teachers_data()
            new_full_name = input("Enter teacher's new full name: ").capitalize().strip()
            new_gender = input("Enter teacher's new genderFamale/Male): ").capitalize().strip()
            if new_gender != "Famale" and new_gender != "Male":
                print("Incorrect gender!")
                update_teachers_data()
            new_age = input("Enter teacher's new age: ").strip()
            new_gmail = input("Enter teacher's new gmail: ").strip()
            if not "@gmail.com" in new_gmail:
                print("Incorrect gmail!")
                update_teachers_data()
            new_password = input("Enter teacher's new password: ").strip()
            password = People.hash_password(new_password)
            update_teacher = People(new_full_name, new_phone_number, new_gender, new_age, new_gmail, password)
            teachers_manager.update_data(teachers_manager,phone_number, update_teacher.__dict__, 'phone_number')
            print("\nTeacher updated successfully!")
        else:
            print("\nTeacher not found")
    return "menu"


@log_decorator
def delete_teacher():
    phone_number = input("Enter teacher phone number: ").strip().lower()
    all_teacher = teachers_manager.read()
    new_teachers = []
    for teacher in all_teacher:
        if teacher['phone_number'].lower() != phone_number.lower():
            new_teachers.append(teacher)
    teachers_manager.write(new_teachers)
    print('\nAdmin deleted successfully!\n')
    return "menu"