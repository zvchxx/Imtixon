from users import login, register, logout_all
from logs import log_settings

from super_admin import delete_admin, update_admin_data
from super_admin import add_admin, see_all_admin, search_admin

from super_admin import delete_teacher, update_teachers_data
from super_admin import add_teacher, see_all_teacher, search_teacher


from super_admin_email import see_all_users, send_message
from admin import delete_group, update_group_data

from admin import add_group, see_all_group, search_group


def show_auth_menu():
    text = """
    1. Register      
    2. Login
    3. Quit
"""
    print(text)
    try:
        user_input = input("Enter your choice: ")
        if user_input == "1":
            if register():
                show_auth_menu()
        elif user_input == "2":
            log = login()
            if "menu" == log:
                student_menu()
            elif "admin" == log:
                super_admin_menu()
            elif "simple_admin" == log:
                admin_menu()
            else:
                show_auth_menu()
        elif user_input == "3":
            print("\nThakns for wisit")
            logout_all()
        else:
            print("\nWrong choice !")
            show_auth_menu()
    except KeyboardInterrupt:
        show_auth_menu()
    

def super_admin_menu():
    text = """
    1. Admin
    2. Teacher
    3. Message
    4. See all users
    5. Quit
"""
    print(text)
    try:
        user_input = input("Enter your choice: ")
        if user_input == "1":
            extra_s_admin_menu()
        elif user_input == "2":
            extra_s_teacher_menu() 
        elif user_input == "3":
            if "menu" == send_message():
                super_admin_menu()
        elif user_input == "4":
            if "menu" == see_all_users():
                super_admin_menu()
        elif user_input == "5":
            print("\nThakns for wisit")
            show_auth_menu()
        else:
            print("\nWrong choice !")
            super_admin_menu()
    except KeyboardInterrupt:
        super_admin_menu()
    

def admin_menu():
    text = """
    1. Group
    2. Student
    3. Add studdent for grup
    4. Search 
    5. Accept payment
    6. Quit
"""
    print(text)
    try:
        user_input = input("Enter your choice: ")
        if user_input == "1":
            extra_a_group_menu()
        elif user_input == "2":
            extra_a_student_menu()
        elif user_input == "6":
            print("\nThakns for wisit")
            show_auth_menu()
        else:
            print("\nWrong choice !")
            admin_menu()
    except KeyboardInterrupt:
        admin_menu()
    

def teacher_menu():
    text = """
    1. See a list of all groups
    2. View the list of students by group
    3. Start lesson 
    4. Quit
"""
    print(text)
    try:
        user_input = input("Enter your choice: ")
        if user_input == "1":
            pass
        elif user_input == "4":
            print("\nThakns for wisit")
            show_auth_menu()
        else:
            print("\nWrong choice !")
            teacher_menu()
    except KeyboardInterrupt:
        teacher_menu()
    

def student_menu():
    text = """
    1. Show all groups
    2. View the balance amount
    3. The ability to change personal data
    4. Quit
"""
    print(text)
    try:
        user_input = input("Enter your choice: ")
        if user_input == "1":
            pass
        elif user_input == "4":
            print("\nThakns for wisit")
            show_auth_menu()
        else:
            print("\nWrong choice !")
            student_menu()
    except KeyboardInterrupt:
        student_menu()
    

def print_menu():
    return f"""
    1. Add 
    2. Search
    3. Show all
    4. Delete 
    5. Update
    6. Back
    """


def extra_a_group_menu():
    print(print_menu())
    choice = input("Enter your choice: ")
    if choice == "1":
        if "menu" == add_group():
            extra_a_group_menu()
    elif choice == "2":
        if "menu" == search_group():
            extra_a_group_menu()
    elif choice == "3":
        if "menu" == see_all_group():
            extra_a_group_menu()
    elif choice == "4":
        if "menu" == delete_group():
            extra_a_group_menu()
    elif choice == "5":
        if "menu" == update_group_data():
            extra_a_group_menu()
    elif choice == "6":
        print("Thinks for visit!")
        admin_menu()
    else:
        print("Wrong choice !")
        extra_a_group_menu()


def extra_a_student_menu():
    print(print_menu())
    choice = input("Enter your choice: ")
    if choice == "1":
        pass
    elif choice == "6":
        print("Thinks for visit!")
        admin_menu()
    else:
        print("Wrong choice !")
        admin_menu()


def extra_s_admin_menu():
    print(print_menu())
    choice = input("Enter your choice: ")
    if choice == "1":
        if "menu" == add_admin():
            extra_s_admin_menu()
    elif choice == "2":
        if "menu" == search_admin():
            extra_s_admin_menu()
    elif choice == "3":
        if "menu" == see_all_admin():
            extra_s_admin_menu()
    elif choice == "4":
        if "menu" == delete_admin():
            extra_s_admin_menu()
    elif choice == "5":
        if "menu" == update_admin_data():
            extra_s_admin_menu()
    elif choice == "6":
        print("Thinks for visit!")
        super_admin_menu()
    else:
        print("Wrong choice !")
        extra_a_student_menu()
    

def extra_s_teacher_menu():
    print(print_menu())
    choice = input("Enter your choice: ")
    if choice == "1":
        if "menu" == add_teacher():
            extra_s_teacher_menu()
    elif choice == "2":
        if "menu" == search_teacher():
            extra_s_teacher_menu()
    elif choice == "3":
        if "menu" == see_all_teacher():
            extra_s_teacher_menu()
    elif choice == "4":
        if "menu" == delete_teacher():
            extra_s_teacher_menu()
    elif choice == "5":
        if "menu" == update_teachers_data():
            extra_s_teacher_menu()
    elif choice == "6":
        print("Thinks for visit!")
        super_admin_menu()
    else:
        print("Wrong choice !")
        super_admin_menu()


def log_out():
    if "menu" == logout_all():
        show_auth_menu()


if __name__ == "__main__":
    log_out()
    log_settings()