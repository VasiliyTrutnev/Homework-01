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
except ValueError:
    print("Введено нечисловое значение!")


print("Среднее геометрическое = {:.2f}".format(c))

# Задача-2:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
if __name__ == '__main__':
    import sys
    from hw06_easy import create_folder
    from hw06_easy import del_folder
    from hw06_easy import list_dir

    print('sys.argv =', sys.argv)


    def validate_dir_name():
        if not dir_name:
            raise ValueError("Необходимо указать имя директории вторым параметром")
        
    def print_help():
        print("help - получение справки")
        print("mkdir <dir_name> - создание директории")
        print("rmdir <dir_name> - удалить директорию")
        print("open_folder <dir_name> - перейти в директорию")
        print("list_dir - содержимое текущей папки")
    def open_folder():
        dir_name = input()
        os.chdir(dir_name)
    do = dict(open=open_folder(), help=print_help(), list=list_dir(), mkdir=create_folder(), rmdir=del_folder())

    try:
        dir_name = sys.argv[2]
    except IndexError:
        dir_name = None

    try:
        key = sys.argv[1]
    except IndexError:
        key = None


    if key:
        do_func = do.get(key, None)
        if do_func is not None:
            do_func()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")