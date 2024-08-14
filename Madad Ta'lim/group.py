from datetime import datetime

now = datetime.now()


class Group:
    def __init__(self, name, teacher, max_students, start_time, end_time, status, price):
        self.name = name
        self.teacher = teacher
        self.max_students = int(max_students)
        self.have_students = 0
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.price = price
        self.active = False
        self.date = now.strftime("%d/%m/%Y %H:%M:%S")