from datetime import datetime

now = datetime.now()


class Group:
    def __init__(self, name, teacher, max_students, start_time, end_time, status):
        self.name = name
        self.teacher = teacher
        self.max_students = max_students
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.date = now.strftime("%d/%m/%Y %H:%M:%S")