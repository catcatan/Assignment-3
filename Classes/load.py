from Classes.teacher import Teacher


class Load(Teacher):
    def __init__(self, load_1, load_2, load_3) -> None:
        self.load_1 = load_1
        self.load_2 = load_2
        self.load_3 = load_3

    def loadAttr(self):
        return f'Class Loads: {self.load_1}, {self.load_2}, {self.load_3}'