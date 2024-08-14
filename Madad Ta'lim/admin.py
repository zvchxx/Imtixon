import random

from group import Group
from logs import log_decorator

from file_managing import groups_manager, teachers_manager, student_manager
from student import Student

all_teachers = teachers_manager.read()
all_groups = groups_manager.read()
all_student = student_manager.read()
random_password = str(random.randint(00000, 99999))


                                    #Group
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


@log_decorator
def add_group():
    name = input("Enter new group name: ").strip().lower()
    input_teacher = input("Enter teacher name: ").strip().capitalize()
    for teacher in all_teachers:
        if teacher['full_name'] != input_teacher:
            print("Not found teacher!")
            add_group()
    max_student = input("Enter max student: ").strip()
    start_time = input("Enter start time: ").strip()
    end_time = input("Enter end time: ").strip()
    status: int = input("Enter group status(month, pleace enter int): ").strip().lower()
    price: int = input("Enter group price(pleace enter int): ")

    group = Group(name, input_teacher, max_student, start_time, end_time, status, price)

    groups_manager.add_data(data=group.__dict__)
    print("\nSaved")
    return "menu"


@log_decorator
def see_group_list(inf):
            inf_list = f""" 
    Subject: {inf['subject']}
    Teacher: {inf['teacher']}
    Max students: {inf['max_students']} 
    Have students: {inf['have_students']}
    Start time: {inf['start_time']}
    End time: {inf['end_time']}
    Status: {inf['status']}
    Active: {inf['active']}
    Date: {inf['date']}
"""  
            return inf_list


@log_decorator
def see_all_group():
    num = 0
    for group in all_groups:
        num += 1
        inf = see_group_list(group)
        f"""
{print(num)}:
    {print(inf)}
"""
    return "menu"


@log_decorator    
def search_group():
    name_input: str = input('Enter should group name: ').strip().capitalize()

    for group in all_groups:
        if name_input in group['subject']:
            inf = see_group_list(group)
            print(inf)
    return "menu"


@log_decorator    
def update_group_data():
    name = input("Enter group name: ").strip().capitalize()

    for group in all_groups:
        if group['subject'] == name:
            new_name = input("Enter group's new name: ").strip()
            new_teacher = input("Enter group's new teacher: ").capitalize().strip()
            for teacher in all_teachers:
                if teacher['full_name'] != new_teacher:
                    print("Not found teacher!")
                    update_group_data()
            new_max_student = input("Enter group's new max student: ").strip()
            new_start_time = input("Enter group's new start time: ").strip()
            new_end_time = input("Enter group's new end time: ").strip()
            new_status = input("Enter group's new status: ").strip()


            update_gruop = Group(new_name, new_teacher, new_max_student, new_start_time, new_end_time, new_status)
            groups_manager.update_data(groups_manager, name, update_gruop.__dict__, 'subject')
            print("\nGroup updated successfully!")
        else:
            print("\nGroup not found")
    return "menu"


@log_decorator
def delete_group():
    name = input("Enter group name: ").strip().lower()

    new_groups = []
    for group in all_groups:
        if group['subjecte'].lower() != name.lower():
            new_groups.append(group)
    groups_manager.write(new_groups)
    print('\nGroup deleted successfully!\n')
    return "menu"


                                        # Student
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


@log_decorator
def add_student():
    name = input("Enter new full name: ").strip().capitalize()
    phone_number = input("Enter phone number: ").strip().capitalize()
    if len(phone_number) < 7 and "+" in phone_number:
        print("Incorrect phone number!")
        add_student()
    gender = input("Enter new admin gender (Famale/Male): ").strip().capitalize()
    if gender != "Famale" and gender != "Male":
        print("Incorrect gender!")
        add_student()
    age = input("Enter new admin age: ").strip().capitalize()
    gmail = input("Enter new admin gmail: ").strip().lower()
    if not "@gmail.com" in gmail:
        print("Incorrect gmail!")
        add_student()
    password = random_password
    print(f"Student password: {password}")

    student = Student(name, phone_number, gender, age, gmail, password)
    if not student.check_password(password):
        print("Passwords do not match")
        add_student()

    student.password = Student.hash_password(password)
    student_manager.add_data(data=student.__dict__)
    print("\nSaved")
    return "menu"


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
def see_all_students():
    num = 0
    for student in all_student:
        num += 1
        inf = see_student_list(student)
        f"""
{print(num)}:
    {print(inf)}
"""
    return "menu"


@log_decorator    
def search_student():
    phone_input: str = input('Enter should student phone number: ').strip()

    for student in all_student:
        if phone_input in student['phone_number']:
            inf = see_student_list(student)
            print(inf)
    return "menu"


@log_decorator    
def update_student_data():
    phone_number= input("Enter student phone number: ").strip().capitalize()

    for student in all_student:
        if student['phone_number'] == phone_number:
            new_name = input("Enter student full name: ").strip()
            new_phone_number = input("Enter student phone number: ").strip()
            if len(new_phone_number) < 7 and "+" in new_phone_number:
                print("Incorrect phone number!")
                update_student_data()
            new_gender = input("Enter new admin gender (Famale/Male): ").strip().capitalize()
            if new_gender != "Famale" and new_gender != "Male":
                print("Incorrect gender!")
                add_student()
            new_age = input("Enter new admin age: ").strip()
            new_gmail = input("Enter new admin gmail: ").strip().lower()
            if not "@gmail.com" in new_gmail:
                print("Incorrect gmail!")
                add_student()
            new_password = random_password
            print(f"Student password: {new_password}")

            new_password = Student.hash_password(new_password)

            update_student = Student(new_name, new_phone_number, new_gender, new_age, new_gmail, new_password)
            student_manager.update_data(student_manager, phone_number, update_student.__dict__, 'phone_number')
            print("\nStudent updated successfully!")
        else:
            print("\nStudent not found")
    return "menu"


@log_decorator
def delete_student():
    phone_number = input("Enter student phone number: ").strip()

    new_students = []
    for student in all_student:
        if student['phone_number'] != phone_number:
            new_students.append(student)
    student_manager.write(new_students)
    print('\nStudent deleted successfully!\n')
    return "menu"


                                        # View the list of students by group
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


@log_decorator
def add_student_for_group():
    try:
        student_id = int(input("Enter student ID: "))
        group_name = input("Enter group name: ") 
        
        for grp in all_groups:
            if grp['subject'] == group_name:
                grp['max_students'] = grp['max_students'] - 1
                grp['have_students'] = grp['have_students'] + 1
                groups_manager.write(grp)
        groups_manager.write(grp)
        for student in all_student:
            if student['student_id'] == student_id:
                student['group'] = student['group'] = group_name
                student_manager.write(all_student)
        student_manager.write(student)
        print("\nSaved")
        return "menu"
    except ValueError:
        print("Error input")
        add_student_for_group()


                                    # Accept
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


@log_decorator
def add_accept():
    try: 
        student_id = int(input("Enter student ID: "))
        price = int(input("Enter amount (pleace enter int): "))
        for student in all_student:
            if student['student_id'] == student_id:
                student['students_price'] = price
                student_manager.write(all_student)
        student_manager.write(student)
        print("\nSaved")
        return "menu"
    except ValueError:
        print("Error input")
        add_accept()