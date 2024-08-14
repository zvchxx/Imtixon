from logs import log_decorator
from datetime import datetime

from file_managing import groups_manager
from file_managing import student_manager

all_groups = groups_manager.read()
all_students = student_manager.read()

# @log_decorator
def start_lesson():
    group_name = input("Enter group name: ").strip().lower()
    start = datetime.now()

    for grp in all_groups:
        if group_name == grp['subject']:
            print(f"Start lesson: {start.strftime("%d/%m/%Y %H:%M:%S")}")

    print("""
    1. Finished lesson
    2. Quit

""")
    user_input = input("Enter your choice: ")
    if user_input == "1":
        finish = datetime.now()
        duration = finish - start
        print(f"lesson time: {duration}")
        return "menu"
    elif user_input == "2":
         return "menu"
    else:
        print("\nWrong choice !")
        start_lesson()

start_lesson()


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
    grp_name = input("Enter group name: ").strip().lower()
    for student in all_students:
            if student['group'] == grp_name:
                inf = see_student_list(student)
                print(inf)

    return "menu"