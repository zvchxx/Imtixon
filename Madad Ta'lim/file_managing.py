import json
import os

if not os.path.exists('files'):
    os.mkdir('files')


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
        

    def update_data(self, identifier, updated_data, identifier_field='name'):
        data = admins_manager.read()
        for index, item in enumerate(data):
            if item[identifier_field] == identifier:
                data[index] = updated_data
                admins_manager.write(data)
                return "Data is updated"
        return "Data not found"


users_manager = JsonManager("files/users.json")
admins_manager = JsonManager("files/admins.json")
teachers_manager = JsonManager("files/teachers.json")