
# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
def avg(a, b):

    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    return (a * b) ** 0.5

try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = avg(a, b)
    print("Среднее геометрическое = {:.2f}".format(c))
except ValueError:
    print("Введено не числовое значение!")

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import sys

dir_1 = 'c:/Users/Василий и Настенька/Desktop/Домашка BE/dir_1'
dir_9 = 'c:/Users/Василий и Настенька/Desktop/Домашка BE/dir_9'
def create_folder():
    try:
        os.mkdir(dir_1)
        os.mkdir(dir_9)
    except OSError:
        print ("Создать директорию %s не удалось" % dir_1, dir_9)
    else:
        print ("Успешно создана директория %s " % dir_1, dir_9)
def del_folder():
    try:
        os.rmdir(dir_1)
        os.rmdir(dir_9)
    except OSError:
        print ("Удалить директорию %s не удалось" % dir_1, dir_9)
    else:
        print ("Успешно удалена директория %s " % dir_1, dir_9)

# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.
def list_dir():
    path = 'c:/Users/Василий и Настенька/Desktop/Домашка BE'
    print(os.listdir(path))

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_file():
    import shutil
    shutil.copy2("c:/Users/Василий и Настенька/Desktop/Домашка BE/hw06_easy.py", "c:/Users/Василий и Настенька/Desktop/Домашка BE/hw06_easy(1).py")
