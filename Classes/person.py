class Person:
    def __init__(self, first_name, middle_name, last_name, age, type):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.age = age
        self.type = type

    def personAttr(self):
        return f'Name: {self.last_name}, {self.first_name} {self.middle_name}, Age: {self.age}, Type: {self.type}'
