from Classes.student import Student


class Grade(Student):
    def __init__(self, math, english, science, filipino) -> None:
        self.math = math
        self.english = english
        self.science = science
        self.filipino = filipino

    def gradeAttr(self):
        return f'Math: {self.math}, English: {self.english}, Science: {self.science}, Filipino: {self.filipino}'
