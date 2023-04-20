from Classes.person import Person


class Teacher(Person):
    def __init__(self, first_name, middle_name, last_name, age, type, id, department):
        super().__init__(first_name, middle_name, last_name, age, type)
        self.id = id
        self.department = department

    def teacherAttr(self):
        return f'Teacher ID: {self.id}, Department: {self.department}'
