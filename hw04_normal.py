# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    import math
    while n <= m :
        a = int((((1 + math.sqrt(5))/2)**n-((1 - math.sqrt(5))/2)**n)/(math.sqrt(5))) # Формула Бине
        print(a)
        n += 1
    return list(fibonacci(n, m))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for i in range(len(origin_list) - 1):
        for x in range(len(origin_list) - i - 1):
            """Пузырьковый метод. Передвигается больший элемент в конец, путем сравнения"""
            if origin_list[x] > origin_list[x + 1]:
                origin_list[x], origin_list[x + 1] = origin_list[x + 1], origin_list[x]
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def fltr(function, iterable):
    return (item for item in iterable if function(item))
 
 
print(list(fltr(lambda x: True if x % 2 == 0 else False,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))        

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
import math
A1 = input([])
A2 = input([])
A3 = input([])
A4 = input([])
def par(А1, А2, А3, А4):
    A1A2 = math.sqrt(((A2[0] - A1[0]) ** 2) + ((A2[1] - A1[1]) ** 2))
    A3A4 = math.sqrt(((A4[0] - A3[0]) ** 2) + ((A4[1] - A3[1]) ** 2))
    A2A3 = math.sqrt(((A3[0] - A2[0]) ** 2) + ((A3[1] - A2[1]) ** 2))
    A1A4 = math.sqrt(((A4[0] - A1[0]) ** 2) + ((A4[1] - A1[1]) ** 2))
    if A1A2 == A3A4 and A2A3 == A1A4:
        print('parallelogram')
    else:
        print('not parallelogram')

