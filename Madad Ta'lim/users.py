import hashlib
import smtplib
import threading
import random

from datetime import datetime
from file_managing import admins_manager, teachers_manager, student_manager

from logs import log_decorator


now = datetime.now()
student_id: str = random.randint(0000, 1111)

smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_sender = "abubakrrahmatullayev1001@gmail.com"
smtp_password = "etsk hbbi kuym flhe"

now = datetime.now()

super_admin_phone_number = "9999"
super_admin_gmail = "admin@gmail.com"
super_admin_password = "admin"

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
    

class Student(People):
    def __init__(self,full_name, phone_number, gender, age, gmail, password):
        super().__init__(full_name, phone_number, gender, age, gmail, password)
        self.student_id = student_id
        self.students_price = 0
        self.gruop = False


@log_decorator
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


@log_decorator
def register():
    full_name = input("Enter your full name: ").strip().capitalize()
    phone_number = input("Enter your phone number: ").strip()
    if len(phone_number) < 7 and "+" in phone_number:
        print("Incorrect gender!")
        register()
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

    person = Student(full_name, phone_number, gender, age, gmail, password)
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

    person.password = Student.hash_password(password)
    student_manager.add_data(data=person.__dict__)
    print("\nSaved")
    return "menu"


@log_decorator
def login():
    phone_number = input("Enter your phone number: ").capitalize().strip()
    gmail = input("Enter your gmail: ")
    password = input("Enter your password: ")
 
    if phone_number == super_admin_phone_number and gmail == super_admin_gmail and password == super_admin_password:
        return "admin"
    
    hashed_password = Student.hash_password(password)

    all_students = student_manager.read()
    all_admins = admins_manager.read()
    all_teachers = teachers_manager.read()


    index_a = 0
    while index_a < len(all_admins):
        if all_admins[index_a]['phone_number'] == phone_number and all_admins[index_a]['password'] == hashed_password and all_admins[index_a]['gmail'] == gmail:
            all_admins[index_a]['is_login'] = True
            admins_manager.write(all_admins)
            return "simple_admin"
        index_a += 1
        
    admins_manager.write(all_admins)
        
    index_t = 0

    while index_a < len(all_teachers):
        if all_teachers[index_t]['phone_number'] == phone_number and all_teachers[index_t]['password'] == hashed_password and all_teachers[index_t]['gmail'] == gmail:
            all_teachers[index_t]['is_login'] = True
            teachers_manager.write(all_teachers)
            return "simple_teacher"
        index_t += 1

    teachers_manager.write(all_teachers)

    index = 0
    while index < len(all_students):
        if all_students[index]['phone_number'] == phone_number and all_students[index]['password'] == hashed_password and all_students[index]['gmail'] == gmail:
            all_students[index]['is_login'] = True
            student_manager.write(all_students)
            return "menu"
        index += 1

    student_manager.write(all_students)
    
    print("Phone number not found, or password is incorrect")
    return "back"


@log_decorator
def logout_all():
    all_users = student_manager.read()
    index = 0
    while index < len(all_users):
        all_users[index]['is_login'] = False
        index += 1
    student_manager.write(all_users)
    return "menu"


def active_user():
    students = student_manager.read()
    for student in students:
        if student['is_login']:
            return student
    return False