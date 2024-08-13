from datetime import datetime

now = datetime.now()


class Message:
    def __init__(self, full_name, age, gender, email, user_message):
        self.full_name = full_name
        self.age = age
        self.gender = gender
        self.email = email
        self.user_message = user_message
        self.date = now.strftime("%d/%m/%Y %H:%M:%S")