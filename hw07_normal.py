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
        return self.class_rooms







