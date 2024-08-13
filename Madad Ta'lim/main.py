from users import login, register, logout_all, active_user
from logs import log_settings


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
                admin_menu()
            else:
                show_auth_menu()
        elif user_input == "3":
            print("\nThakns for wisit")
            return
        else:
            print("\nWrong choice !")
            return show_auth_menu()
    except KeyboardInterrupt:
        return show_auth_menu()
    

def super_admin_menu():
    text = """
    1. Admin
    2. Teacher
    3. Send email
    4. Quit
"""
    print(text)
    try:
        user_input = input("Enter your choice: ")
        if user_input == "1":
            extra_s_admin_menu()
        elif user_input == "2":
            extra_s_teacher_menu()
        elif user_input == "4":
            print("\nThakns for wisit")
            logout_all()
        else:
            print("\nWrong choice !")
            return super_admin_menu()
    except KeyboardInterrupt:
        return super_admin_menu()
    

def admin_menu():
    text = """
    1. Grup
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
            logout_all()
        else:
            print("\nWrong choice !")
            return admin_menu()
    except KeyboardInterrupt:
        return admin_menu()
    

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
            logout_all()
        else:
            print("\nWrong choice !")
            return teacher_menu()
    except KeyboardInterrupt:
        return teacher_menu()
    

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
            logout_all()
        else:
            print("\nWrong choice !")
            return student_menu()
    except KeyboardInterrupt:
        return student_menu()
    

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
        pass
    elif choice == "6":
        print("Thinks for visit!")
        logout_all()
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
        logout_all()
    else:
        print("Wrong choice !")
        extra_a_student_menu()


def extra_s_admin_menu():
    print(print_menu())
    choice = input("Enter your choice: ")
    if choice == "1":
        pass
    elif choice == "6":
        print("Thinks for visit!")
        logout_all()
    else:
        print("Wrong choice !")
        extra_a_student_menu()
    

def extra_s_teacher_menu():
    print(print_menu())
    choice = input("Enter your choice: ")
    if choice == "1":
        pass
    elif choice == "6":
        print("Thinks for visit!")
        logout_all()
    else:
        print("Wrong choice !")
        extra_s_teacher_menu()


def log_out():
    if "menu" == logout_all():
        show_auth_menu()


if __name__ == "__main__":
    log_settings()
    log_out()