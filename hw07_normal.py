# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class People:
    def __init__(self, surname, name, father_name):
        self.surname = surname
        self.name = name
        self.father_name = father_name

    def full_name(self):
        return f"{self.surname} {self.name} {self.father_name}"

    def short_name(self):
        return f"{self.surname} {self.name[0].upper()} {self.father_name[0].upper()}"


class Student(People):
    def __init__(self, surname, name, father_name, mom, dad, class_room):
        super().__init__(surname, name, father_name)
        self.class_room = class_room
        self.mom = mom
        self.dad = dad

    def get_class_room(self):
        return self.class_room

    def get_parents(self):
        return f"Мама: {self.mom.full_name()}, Папа: {self.dad.full_name()}"


class Teacher(People):
    def __init__(self, surname, name, father_name, rooms, subject):
        super().__init__(surname, name, father_name)
        self.subject = subject
        self.rooms = rooms

    def get_subject(self):
        return self.subject

    def get_classes(self):
        return self.rooms

if __name__ == '__main__':
    class_rooms = ['5 А', '4 В', '8 Б']
    parents = [People("Сидоров", "Иван", "Игоревич"),
               People("Сидорова", "Татьяна", "Максимовна"),
               People("Иванов", "Игорь", "Александрович"),
               People("Иванова", "Ирина", "Александровна"),
               People("Петров", "Николай", "Александрович"),
               People("Петрова", "Светлана", "Николаевна")]
    students = [Student("Иванов", "Александр", "Игоревич", parents[3], parents[2], class_rooms[0],),
                Student("Сидоров", "Петр", 'Иванович', parents[1], parents[0], class_rooms[2]),
                Student("Петров", "Иван", 'Николаевич', parents[5], parents[4], class_rooms[1])]
    teachers = [Teacher("Сидоров", "Иван", "Игоревич", [class_rooms[0], class_rooms[1]], 'Математика'),
                Teacher("Иванов", "Игорь", "Александрович", [class_rooms[2], class_rooms[1]], 'История'),
                Teacher("Петров", "Николай", "Александрович", [class_rooms[0], class_rooms[2]], 'Английский')]

# Получить полный список всех классов школы
st = [i.get_class_room() for i in students]
print(st)

# Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
cl_room = '4 В'
st_list = [i.short_name() for i in students if i.get_class_room() == cl_room]
print(st_list)

# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
student = students[0]
t_list = [i for i in teachers if student.get_class_room() in i.get_classes()]

t_names = [i.full_name() for i in t_list]
subj = [i.get_subject() for i in t_list]
print(f"{student.full_name()} {' --> '} {student.get_class_room()} {' --> '} {t_names} {' --> '} "
      f"{subj}")


# 4. Узнать ФИО родителей указанного ученика
his_parents = student.get_parents()
print(his_parents)

# 5. Получить список всех Учителей, преподающих в указанном классе
teach_list = [i.full_name() for i in teachers if cl_room in i.get_classes()]
print(teach_list)





