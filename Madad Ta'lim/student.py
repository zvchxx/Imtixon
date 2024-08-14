import random

from users import People


student_id: str = random.randint(0000, 1111)


class Student(People):
    def __init__(self,full_name, phone_number, gender, age, gmail, password, students_price):
        super().__init__(full_name, phone_number, gender, age, gmail, password)
        self.student_id = student_id
        self.gruop = False
        self.students_price = students_price