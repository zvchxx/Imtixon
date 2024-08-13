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