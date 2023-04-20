from Classes.grade import Grade
from Classes.load import Load


student_list = []
teacher_list = []


def menu():
    print()
    print('MENU')
    print('A - Add Record        M - Display Records')
    print('D - Delete Record     S - Search Record')
    print()

    choice = input('Enter Choice: ')
    choice = choice.lower()
    print()

    if choice == 'a':
        print('1 - Student      2 - Teacher')
        print()
        add_choice = input('Enter Choice: ')

        if add_choice == "1":
            addStudent()
        elif add_choice == "2":
            addTeacher()
        else:
            print()
            print('Not a choice.')
            menu()

    elif choice == 'm':
        print('1 - Student      2 - Teacher    3 - All')
        print()
        disp_choice = input('Enter Choice: ')

        if disp_choice == "1":
            displayRecordsStud()
            menu()
        elif disp_choice == "2":
            displayRecordsTeach()
            menu()
        elif disp_choice == "3":
            displayRecordsStud()
            displayRecordsTeach()
            menu()
        else:
            print()
            print('Not a choice.')
            menu()

    elif choice == 'd':
        print('1 - Student      2 - Teacher     3 - Delete All')
        print()
        del_choice = input('Enter Choice: ')

        if del_choice == "1":
            print()
            print('1 - Delete One    2 - Delete All')
            print()
            del_stud_choice = input('Enter Choice: ')

            if del_stud_choice == "1":
                deleteRecordStud()
                menu()
            elif del_stud_choice == "2":
                deleteRecordStudAll()
                menu()
            else:
                print()
                print('Not a choice.')
                menu()

        elif del_choice == "2":
            print()
            print('1 - Delete One    2 - Delete All')
            print()
            del_teach_choice = input('Enter Choice: ')

            if del_teach_choice == "1":
                deleteRecordTeach()
                menu()
            elif del_teach_choice == "2":
                deleteRecordTeachAll()
                menu()
            else:
                print()
                print('Not a choice.')
                menu()

        elif del_choice == "3":
            deleteRecordStudAll()
            deleteRecordTeachAll()
            menu()

        else:
            print()
            print('Not a choice.')
            menu()

    elif choice == 's':
        print('1 - Student      2 - Teacher')
        print()
        add_choice = input('Enter Choice: ')

        if add_choice == "1":
            searchRecordStud()
        elif add_choice == "2":
            searchRecordTeach()
        else:
            print()
            print('Not a choice.')
            menu()

    else:
        print()
        print('Not a choice.')
        menu()


def addStudent():
    while True:
        print()
        
        id = input('Student ID: ')
        first_name = input('First Name: ')
        middle_name = input('Middle Name: ')
        last_name = input('Last Name: ')
        age = input('Age: ')
        type = 'Student'
        course = input('Course: ')
        year = input('Year: ')
        section = input('Section: ')
        print()

        print('Input Grades...')
        math = input('Math: ')
        english = input('English: ')
        science = input('Science: ')
        filipino = input('Filipino: ')
        print()

        stud = Grade(math, science, english, filipino)
        stud.id = id
        stud.last_name = last_name
        stud.first_name = first_name
        stud.middle_name = middle_name
        stud.age = age
        stud.type = type
        stud.course = course
        stud.year = year
        stud.section = section

        student_list.append(stud)

        print()
        ans = input('Enter another? [y/n]: ')

        if ans != 'y':
            break

    menu()


def addTeacher():
    while True:
        print()

        id = input('Teacher ID: ')
        first_name = input('First Name: ')
        middle_name = input('Middle Name: ')
        last_name = input('Last Name: ')
        age = input('Age: ')
        type = 'Teacher'
        department = input('Department: ')
        print()

        print('Input Loads...')
        load_1 = input('Load 1: ')
        load_2 = input('Load 2: ')
        load_3 = input('Load 3: ')
        print()

        teach = Load(load_1, load_2, load_3)
        teach.id = id
        teach.last_name = last_name
        teach.middle_name = middle_name
        teach.first_name = first_name
        teach.age = age
        teach.type = type
        teach.department = department

        teacher_list.append(teach)

        print()
        ans = input('Enter another? [y/n]: ')

        if ans != 'y':
            break

    menu()


def displayRecordsStud():
    print()
    print('Students')
    print('-------------------------------------------------------------------------------')
    i = 0
    for s in student_list:
        print(f'{i} \t | {s.personAttr()} \t | {s.studentAttr()} \t | {s.gradeAttr()}')
        i += 1
    print('-------------------------------------------------------------------------------')


def displayRecordsTeach():
    print()
    print('Teachers')
    print('-------------------------------------------------------------------------------')
    i = 0
    for t in teacher_list:
        print(f'{i} \t | {t.personAttr()} \t | {t.teacherAttr()} \t | {t.loadAttr()}')
        i += 1
    print('-------------------------------------------------------------------------------')


def deleteRecordStud():
    print()
    i = int(input('Enter index: '))
    student_list.pop(i)
    print()
    print('Deleted.')


def deleteRecordTeach():
    print()
    i = int(input('Enter index: '))
    teacher_list.pop(i)
    print()
    print('Deleted.')


def deleteRecordStudAll():
    print()
    confirm = input('This will delete ALL student records. Continue? [y/n]: ')
    confirm = confirm.lower()

    if confirm != "y":
        menu()
    else:
        i = 0
        stud_list_size = len(student_list)
        while i < stud_list_size:
            student_list.pop(0)
            i += 1

    print()
    print('Deleted.')


def deleteRecordTeachAll():
    print()
    confirm = input('This will delete ALL teacher records. Continue? [y/n]: ')
    confirm = confirm.lower()

    if confirm != "y":
        print()
        print('Canceled.')
        menu()
    else:
        i = 0
        teach_list_size = len(teacher_list)
        while i < teach_list_size:
            teacher_list.pop(0)
            i += 1

    print()
    print('Deleted.')


def searchRecordStud():
    i = int(input('Enter index: '))
    print(f'{i} \t {student_list[i].personAttr()} \t | {student_list[i].studentAttr()} \t | {student_list[i].gradeAttr()}')

    menu()


def searchRecordTeach():
    i = int(input('Enter index: '))
    print(f'{i} \t {teacher_list[i].personAttr()} \t | {teacher_list[i].teacherAttr()} \t | {teacher_list[i].loadAttr()}')

    menu()


menu()
