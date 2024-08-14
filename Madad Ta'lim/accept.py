from datetime import datetime

now = datetime.now()


class Group:
    def __init__(self, name, phone_number, dept, total_price):
        self.name = name
        self.phone_number = phone_number
        self.dept = dept
        self.total_price = total_price
        self.date = now.strftime("%d/%m/%Y %H:%M:%S")