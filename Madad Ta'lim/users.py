import hashlib
import smtplib
import threading
import random

from datetime import datetime
from file_managing import users_manager


now = datetime.now()

admin_username = "00"
admin_gmail = "00"
admin_password = "00"
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_sender = "abubakrrahmatullayev1001@gmail.com"
smtp_password = "etsk hbbi kuym flhe"

now = datetime.now()

admin_gmail = "admin@gmail.com"
admin_password = "00"

class People:
    def __init__(self, full_name, phone_number, gender, age, gmail, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.gender = gender
        self.age = age
        self.gmail = gmail
        self.password = password
        self.date = now.strftime("%d/%m/%Y %H:%M:%S")
        self.is_login = False
    

    def check_password(self, confirm_password):
        return confirm_password == self.password

    @staticmethod
    def hash_password(student_password):
        return hashlib.sha256(student_password.encode()).hexdigest()


def send_gmail(to_user, subject, message):
    code = f"Subjet: {subject}\n\n{message}"

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_sender, smtp_password)
        server.sendmail(smtp_sender, to_user, code)
        server.quit()
    except smtplib.SMTPException as e:
        print(f"Failed {e}")


def register():
    full_name = input("Enter your full name: ").strip().capitalize()
    phone_number = input("Enter your phone number: ").strip().capitalize()
    gender = input("Enter your gender (Famale/Male): ").strip().capitalize()
    if gender != "Famale" and gender != "Male":
        print("Incorrect gender!")
        register()
    age = input("Enter your age: ").strip().capitalize()
    gmail = input("Enter your gmail: ").strip().lower()
    if not "@gmail.com" in gmail:
        print("Incorrect gmail!")
        register()
    password = input("Enter your password: ").strip()
    confirm_password = input("Enter your confirm password: ").strip()

    person = People(full_name, phone_number, gender, age, gmail, password)
    if not person.check_password(confirm_password):
        print("Passwords do not match")
        return register()
    
    user_email = gmail
    user_subject = "Register Code"
    user_message = str(random.randint(0000, 9999))

    t = threading.Thread(target=send_gmail, args=(user_email, user_subject, user_message,))
    t.start()
    print("Email is sent")

    result_code = input("Enter please code: ")
    if result_code != user_message:
        print("Incorrect code!")
        register()

    person.password = People.hash_password(password)
    users_manager.add_data(data=person.__dict__)
    print("\nSaved")
    return "menu"


def login():
    phone_number = input("Enter your phone number: ").capitalize().strip()
    gmail = input("Enter your gmail: ")
    password = input("Enter your password: ")
 
    if phone_number == admin_username and gmail == admin_gmail and password == admin_password:
        return "admin"
    
    hashed_password = People.hash_password(password)

    all_users = users_manager.read()

    index = 0
    while index < len(all_users):
        if all_users[index]['phone_number'] == phone_number and all_users[index]['password'] == hashed_password and all_users[index]['gmail'] == gmail:
            all_users[index]['is_login'] = True
            users_manager.write(all_users)
            return "menu"
        index += 1
    users_manager.write(all_users)
    print("User name not found, or password is incorrect")
    return "back"