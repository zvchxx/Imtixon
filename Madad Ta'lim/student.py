import random

from users import People
from logs import log_decorator

from file_managing import student_manager


student_id: str = random.randint(0000, 1111)
all_student = student_manager.read()


class Student(People):
    def __init__(self,full_name, phone_number, gender, age, gmail, password):
        super().__init__(full_name, phone_number, gender, age, gmail, password)
        self.student_id = student_id
        self.students_price = 0
        self.gruop = False


@log_decorator
def see_student_list(inf):
            inf_list = f""" 
    Full name: {inf['full_name']}
    Phone number: {inf['phone_number']}
    Gender: {inf['gender']} 
    Age: {inf['age']}
    Gmail: {inf['gmail']}
    Password: {inf['password']}
    ID: {inf['student_id']}
    Group: {inf['group']}
    Price: {inf['students_price']}
"""  
            return inf_list


@log_decorator    
def view_student():
    for student in all_student:
            if student['is_login'] == True:
                inf = see_student_list(student)
                print(inf)
    return "menu"