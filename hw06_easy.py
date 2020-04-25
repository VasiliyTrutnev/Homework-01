
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
    print("Введено нечисловое значение!")




# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
if __name__ == '__main__':

    import os
    import sys


    def create_folder():
        dir_name = input()
        dir_path = os.path.join(os.getcwd(), dir_name)
        try:
            os.mkdir(dir_path)
            print('директория {} создана'.format(dir_name))
        except FileExistsError:
            print('директория {} уже существует'.format(dir_name))

    create_folder()

    
    def del_folder():
        dir_name = input()
        dir_path = os.path.join(os.getcwd(), dir_name)
        try:
            os.rmdir(dir_path)
            print('директория {} удалена'.format(dir_name))
        except FileNotFoundError:
            print('директория {} не найдена'.format(dir_name))
    del_folder()
# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.
    def list_dir():
        path = os.getcwd()
        print(os.listdir(path))
    list_dir()

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
    def copy_file():
        file_name = input()
        import shutil
        shutil.copy2(os.getcwd(), file_name)
    copy_file()

