import json
import os

if not os.path.exists('files'):
    os.mkdir('files')

if not os.path.exists('groups'):
    os.mkdir('groups')

if not os.path.exists('messages'):
    os.mkdir('messages')

if not os.path.exists('my_messages'):
    os.mkdir('my_messages')

if not os.path.exists('new_messages'):
    os.mkdir('new_messages')


class JsonManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def _file_exists_and_not_empty(self):
        return os.path.exists(self.file_name) and os.path.getsize(self.file_name) > 0

    def read(self):
        if self._file_exists_and_not_empty():
            with open(self.file_name, 'r') as file:
                return json.load(file)
        return []

    def write_to_simple(self, data):
        new_data = []
        with open(self.file_name, 'w') as file:
            new_data.append(data)
            json.dump(new_data, file, indent=4)


    def write(self, data):
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent=4)


    def add_data(self, data: dict):
        all_data = self.read()
        all_data.append(data)
        self.write(all_data)
        return "Data added successfully"

    def get_active_user(self):
        try:
            for data in self.read():
                if data['is_login']:
                    return data
            return False
        except Exception as e:
            print(f'Error: {e}')
            return False
        

    def update_data(self, manager, identifier, updated_data, identifier_field='name'):
        data = manager.read()
        for index, item in enumerate(data):
            if item[identifier_field] == identifier:
                data[index] = updated_data
                manager.write(data)
                return "Data is updated"
        return "Data not found"


admins_manager = JsonManager("files/admins.json")
teachers_manager = JsonManager("files/teachers.json")
student_manager = JsonManager("files/students.json")
groups_manager = JsonManager("groups/gruops.json")
my_messages_manager = JsonManager("my_messages/messages.json")
new_messages_manager = JsonManager("new_messages/messages.json")
messages_manager = JsonManager("messages/messages.json")