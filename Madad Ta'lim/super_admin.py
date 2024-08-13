import smtplib
import threading
import random

from users import People
from logs import log_decorator

from file_managing import admins_manager


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
            updated_group = People(new_full_name, new_phone_number, new_gender, new_age, new_gmail, password)
            admins_manager.update_data(phone_number, updated_group.__dict__, 'phone_number')
            print("\nGroup updated successfully!")
        else:
            print("\nGroup not found")
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