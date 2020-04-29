# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры
from math import sqrt
class Triangle:
    def __init__(self, a1, a2, b1, b2, c1, c2):
        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2
        self.c1 = c1
        self.c2 = c2

    def S(self):
        x = ((self.b1 - self.a1) * (self.c2 - self.a2)) - ((self.c1 - self.a1) * (self.b2 - self.a2))
        s = abs(x) / 2
        return s

    def height(self):
        def S(self):
            x = ((self.b1 - self.a1) * (self.c2 - self.a2)) - ((self.c1 - self.a1) * (self.b2 - self.a2))
            s = abs(x) / 2
            return s
        def S2(fn, x):
            from math import sqrt
            return fn * x
        bc = sqrt(((self.c1 - self.b1) ** 2) + ((self.c2 - self.b2)**2))
        h = S2(S(self), 2) / bc
        return h

    def P(self):
        ab = sqrt(((self.b1 - self.a1) ** 2) + ((self.b2 - self.a2)**2))
        bc = sqrt(((self.c1 - self.b1) ** 2) + ((self.c2 - self.b2)**2))
        ac = sqrt(((self.c1 - self.a1) ** 2) + ((self.c2 - self.a2)**2))
        p = ab + bc + ac
        return p


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
class Trapeze:
    def __init__(self, a1, a2, b1, b2, c1, c2, d1, d2):
        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2
        self.c1 = c1
        self.c2 = c2
        self.d1 = d1
        self.d2 = d2

    def equilateral(self):
        ac = sqrt(((self.c1 - self.a1) ** 2) + ((self.c2 - self.a2) ** 2))
        bd = sqrt(((self.d1 - self.b1) ** 2) + ((self.d2 - self.b2) ** 2))
        if ac == bd:
            print('Равнобокая')
        else:
            print('Неравнобокая')

    def len_sides(self):
        bc = sqrt(((self.c1 - self.b1) ** 2) + ((self.c2 - self.b2) ** 2))
        ad = sqrt(((self.d1 - self.a1) ** 2) + ((self.d2 - self.a2) ** 2))
        ab = sqrt(((self.b1 - self.a1) ** 2) + ((self.b2 - self.a2) ** 2))
        cd = sqrt(((self.d1 - self.c1) ** 2) + ((self.d2 - self.c2) ** 2))
        return bc, ad, ab, cd

    def P(self):
        bc = sqrt(((self.c1 - self.b1) ** 2) + ((self.c2 - self.b2) ** 2))
        ad = sqrt(((self.d1 - self.a1) ** 2) + ((self.d2 - self.a2) ** 2))
        ab = sqrt(((self.b1 - self.a1) ** 2) + ((self.b2 - self.a2) ** 2))
        cd = sqrt(((self.d1 - self.c1) ** 2) + ((self.d2 - self.c2) ** 2))
        p = bc + ad + ab + cd
        return p

    def S(self):
        bc = sqrt(((self.c1 - self.b1) ** 2) + ((self.c2 - self.b2) ** 2))
        ad = sqrt(((self.d1 - self.a1) ** 2) + ((self.d2 - self.a2) ** 2))
        ab = sqrt(((self.b1 - self.a1) ** 2) + ((self.b2 - self.a2) ** 2))
        cd = sqrt(((self.d1 - self.c1) ** 2) + ((self.d2 - self.c2) ** 2))
        s = (((bc+ad) / 2) * sqrt((ab**2) - (((((ad-bc)**2) + (ab**2) - (cd**2))/(2*(ad-bc)))**2)))
        return s




