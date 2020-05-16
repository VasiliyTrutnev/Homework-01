"""Предметная область - предприятие. Разработать класс Enterprise, описывающий работу с предприятием.
Разработать класс People, описывающий человека, человек характеризуется параметрами: фамилия, имя, отчество,
 дата рождения, телефон. Разработать класс Employees на базе класса People, сотрудник характеризуется следующими
  параметрами: уникальный идентификатор сотрудника, код отдела, заработная плата."""


class Enterprise(object):
    def production(self):
        pass
    def sales(self, price, amount):
        pass

class Wood_department(Enterprise):
    def production(self):
        return 'Wooden boxes'
    def sales(self, price, amount):
        try:
            int(price)
            int(amount)
            return price * amount
        except ValueError:
            return "Integral numbers only!"


class Plastic_department(Enterprise):
    def production(self):
        return 'Plastic parts'
    def sales(self, price, amount):
        try:
            int(price)
            int(amount)
            return price * amount
        except ValueError:
            return "Integral numbers only!"


class Metal_department(Enterprise):
    def production(self):
        return 'Metal parts'
    def sales(self, price, amount):
        try:
            int(price)
            int(amount)
            return price * amount
        except ValueError:
            return "Integral numbers only!"


class Logistic(object):
    def split_parts(self, name):
        pass


class Enterprise_Logistic(Logistic):
    def split_parts(self, name):
        if name == Wood_department:
            return Wood_department()
        if name == Plastic_department:
            return Plastic_department()
        if name == Metal_department:
            return Metal_department()


class People:
    def (self, surname, name, father_name, birth_date, telephone_number):
        self.surname = surname
        self.name = name
        self.father_name = father_name
        self.birth_date = birth_date
        self.telephone_number = telephone_number

    def full_name(self):
        return f"{self.surname} {self.name} {self.father_name}"

    def short_name(self):
        return f"{self.surname} {self.name[0].upper()} {self.father_name[0].upper()}"

class MixinPep:
    def department_code(self):
        pass


class Employees(MixinPep, People):
    def (self, ID, code, salary):
        self.ID = ID
        self.code = code
        self.salary = salary

    def salary_list(self):
        return self.salary

    def department_code(self):
        if self.code == 1:
            return 'Wood_department'
        if self.code == 2:
            return 'Plastic_department'
        if self.code == 3:
            return 'Metal_department'




