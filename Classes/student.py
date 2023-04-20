from Classes.person import Person


class Student(Person):
    def __init__(self, first_name, middle_name, last_name, age, id, type, course, year, section):
        super().__init__(first_name, middle_name, last_name, age, type)
        self.id = id
        self.course = course
        self.year = year
        self.section = section

    def studentAttr(self):
        return f'Student ID: {self.id}, Course: {self.year} / {self.course} / {self.section}'
