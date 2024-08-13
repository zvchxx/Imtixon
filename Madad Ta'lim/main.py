from users import register, login, logout_all


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
                pass
        elif user_input == "2":
            if "menu" == login():
                pass
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
    1. Show all users
    2. Show all posts
    3. Search with keywords   
    4. Quit
"""
    print(text)
    try:
        user_input = input("Enter your choice: ")
        if user_input == "1":
            pass
        elif user_input == "4":
            print("\nThakns for wisit")
            super_admin_menu()
        else:
            print("\nWrong choice !")
            return super_admin_menu()()
    except KeyboardInterrupt:
        return super_admin_menu()()
    

def admin_menu():
    text = """
    1. Show all users
    2. Show all posts
    3. Search with keywords   
    4. Quit
"""
    print(text)
    try:
        user_input = input("Enter your choice: ")
        if user_input == "1":
            pass
        elif user_input == "4":
            print("\nThakns for wisit")
            pass
        else:
            print("\nWrong choice !")
            return admin_menu()
    except KeyboardInterrupt:
        return admin_menu()