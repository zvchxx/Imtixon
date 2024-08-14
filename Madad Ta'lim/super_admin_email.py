import threading
import smtplib

from file_managing import messages_manager, student_manager
from file_managing import my_messages_manager, new_messages_manager

from users import send_gmail
from message import Message

from logs import log_decorator


@log_decorator
def see_all_users():
    all_users = student_manager.read()
    num = 0
    for user in all_users:
        num += 1
        print(f"""
{num}:
    Full name: {user['full_name']}
    Age: {user['age']}
    Gender: {user['gender']}    
    Email: {user['gmail']}           
    Password: {user['password']}
    Date: {user['date']}
    Active: {user['is_login']}
    """)
    return "menu"
    

                                            # Message
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_sender = "abubakrrahmatullayev1001@gmail.com"
smtp_password = "etsk hbbi kuym flhe"


@log_decorator
def send_gmail(to_user, subject, message):
    n_message = f"Subjet: {subject}\n\n{message}"

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_sender, smtp_password)
        server.sendmail(smtp_sender, to_user, n_message)
        server.quit()
    except smtplib.SMTPException as e:
        print(f"Failed {e}")


@log_decorator
def sent_all():
    all_users = student_manager.read()

    user_subject = input("Subject: ")
    message = input("Message: ")

    for user in all_users:
        user_email = user['gmail']
        full_name = user['full_name']
        age = user['age']
        gender = user['gender']

        m = Message(full_name, age, gender, user_email, message)
        messages_manager.add_data(data=m.__dict__)
        my_messages_manager.add_data(data=m.__dict__)
        new_messages_manager.write(data=m.__dict__)

        t = threading.Thread(target=send_gmail, args=(user_email, user_subject, message,))
        t.start()     
        student_manager.write(all_users)
    print("\nSent")
    return "menu"


@log_decorator
def sent_only_girls():
    all_users = student_manager.read()

    user_subject = input("Subject: ")
    message = input("Message: ")

    for user in all_users:
        if user['gender'] == "Famale":
            user_email = user['gmail']
            full_name = user['full_name']
            age = user['age']
            gender = user['gender']

            m = Message(full_name, age, gender, user_email, message)
            messages_manager.add_data(data=m.__dict__)
            my_messages_manager.add_data(data=m.__dict__)
            new_messages_manager.write(data=m.__dict__)

            t = threading.Thread(target=send_gmail, args=(user_email, user_subject, message,))
            t.start()     
            student_manager.write(all_users)
    print("\nSent")
    return "menu"


@log_decorator
def sent_only_boys():
    all_users = student_manager.read()

    user_subject = input("Subject: ")
    message = input("Message: ")

    for user in all_users:
        if user['gender'] == "Male":
            user_email = user['gmail']
            full_name = user['full_name']
            age = user['age']
            gender = user['gender']

            m = Message(full_name, age, gender, user_email, message)
            messages_manager.add_data(data=m.__dict__)
            my_messages_manager.add_data(data=m.__dict__)
            new_messages_manager.write(data=m.__dict__)

            t = threading.Thread(target=send_gmail, args=(user_email, user_subject, message,))
            t.start()     
            student_manager.write(all_users)
    print("\nSent")
    return "menu"


@log_decorator
def send_message():
    print("""
    1. A message for all users
    2. A message for girls only
    3. A message for boys only
    4. See all message
    4. Quit
    """)
    try:
        user_input = input("Enter your choice: ")
        if user_input == "1":
            sent_all()
        elif user_input == "2":
            sent_only_girls()
        elif user_input == "3":
            sent_only_boys()
        elif user_input == "4":
            see_all_messages()
        elif user_input == "4":
            print("\nThakns for wisit")
            return "menu"
        else:
            print("\nWrong choice !")
            return send_message()
    except KeyboardInterrupt:
        return send_message()
    

@log_decorator
def see_all_messages():
    all_messages = messages_manager.read()
    num = 0
    for message in all_messages:
        num += 1
        print(f"""
{num}:
    Full name: {message['full_name']}
    Age: {message['age']}
    Gender: {message['gender']}    
    Email: {message['email']}           
    Messages: {message}['user_message']
    Date: {message['date']}
    """)
        return "menu"