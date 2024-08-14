from logs import log_decorator
from datetime import datetime

from file_managing import groups_manager

now = datetime.now()

@log_decorator
def start_lesson(start):

    print("""
    1. Finished lesson
    2. Quit

""")
    user_input = input("Enter your choice: ")
    if user_input == "1":
        finish = now.strftime("%d/%m/%Y %H:%M:%S")
        result = finish - start
        print(f"lesson time: {result}")




@log_decorator 
def select_group():
    group_name = input("Enter group name: ")
    all_groups = groups_manager.read()

    for grp in all_groups:
        if group_name in grp['name']:
            start = now.strftime("%d/%m/%Y %H:%M:%S")
            start_lesson(start)
    select_group()

select_group