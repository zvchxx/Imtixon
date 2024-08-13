import hashlib
import smtplib

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

