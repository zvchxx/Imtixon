from group import Group
from logs import log_decorator

from file_managing import groups_manager, teachers_manager

all_teachers = teachers_manager.read()
all_groups = groups_manager.read()

# @log_decorator
def add_group():
    name = input("Enter new group name: ").strip().capitalize()
    input_teacher = input("Enter teacher name: ").strip().capitalize()
    for teacher in all_teachers:
        if teacher['full_name'] != input_teacher:
            print("Not found teacher!")
            add_group()
    max_student = input("Enter max student: ").strip()
    start_time = input("Enter start time: ").strip()
    end_time = input("Enter end time: ").strip()
    status = input("Enter group status(Days of the week): ").strip().lower()

    group = Group(name, input_teacher, max_student, start_time, end_time, status)

    groups_manager.add_data(data=group.__dict__)
    print("\nSaved")
    return "menu"


@log_decorator
def see_group_list(inf):
            inf_list = f""" 
    Name: {inf['name']}
    Teacher: {inf['teacher']}
    Max students: {inf['max_students']} 
    Start time: {inf['start_time']}
    End time: {inf['end_time']}
    Status: {inf['status']}
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
        if name_input in group['name']:
            inf = see_group_list(group)
            print(inf)
    return "menu"


@log_decorator    
def update_group_data():
    name = input("Enter group name: ").strip().capitalize()

    for group in all_groups:
        if group['name'] == name:
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
            groups_manager.update_data(groups_manager, name, update_gruop.__dict__, 'name')
            print("\nGroup updated successfully!")
        else:
            print("\Group not found")
    return "menu"


@log_decorator
def delete_group():
    name = input("Enter group name: ").strip().lower()

    new_groups = []
    for group in all_groups:
        if group['name'].lower() != name.lower():
            new_groups.append(group)
    groups_manager.write(new_groups)
    print('\nGroup deleted successfully!\n')
    return "menu"