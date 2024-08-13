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