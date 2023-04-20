from Classes.person import Person
from Classes.student import Student
from Classes.grade import Grade
from Classes.teacher import Teacher
from Classes.load import Load

print()
print("Person Class")
p = Person("Loren", "Catcatan", 20, "Person")
print(p.personAttr())
print()

print("Student Class")
s = Student("Rick", "Sanchez", 30, "Student", 6969)
print(s.personAttr())
print(s.studentAttr())
print()

print("Grade Class")
g = Grade("Morty", "Chauncey", 18, "Student", 1010, 95, 93, 94)
print(g.personAttr())
print(g.studentAttr())
print(g.gradeAttr())
print()

print("Teacher Class")
t = Teacher("Josh", "Lorilla", 25, "Teacher", 452378)
print(t.personAttr())
print(t.teacherAttr())
print()

print("Load Class")
l = Load("Dave", "Galas", 25, "Teacher", 123456, "BSCS", "BSIS", "BLISS")
print(l.personAttr())
print(l.teacherAttr())
print(l.loadAttr())
