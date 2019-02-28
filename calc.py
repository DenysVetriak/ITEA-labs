def welcome_message():
    print(
        '''
********************************
    
Курсовая работа для школы ITEA
Проект калькулятор
Студент: Денис Ветряк
    
********************************
    ''')


# Меню калькулятора
def print_menu():
    print(30 * "-", "Меню программы", 30 * "-")   # Да, учили и такое выделение.
    print("1. Операция прибавления")
    print("2. Операция вычетания")
    print("3. Операция деления")
    print("4. Операция умножения")
    print("5. Модуль числа")
    print("6. Корень числа")
    print("7. Выход из программы")
    print("8. Помощь")
    print(67 * "-")


# Меню справки
def help_menu():
    print(28 * "-", "Подсказка для особо одаренных", 28 * "-")
    print("1. Прибавление - Сочетание двух случайных чисел")
    print("2. Вычитание - Проводит операцию по вычитанию двух чисел")
    print("3. Деление - Действие обратное умножению")
    print("4. Умножение - Умножение двух аргументов")
    print("5. Модуль числа - Расстояние от начала координат до точки х")
    print("6. Корень - Число получаемое при возведении в квадрат")
    print("7. Выход - Для выхода из программы нажмите Y или N и далее enter")
    print("8. Справка - Краткие пояснения")
    print(67 * "-")


# На случай если пользователь ручками будет вводить не то что просят.
def invalid():
    print("Вы ввели несуществующий параметр, выбирите из списка!!!")


result = "null"
# Выводим пользователю меню с операциями калькулятора, отпечатываем преветствие.
while True:
    welcome_message()
    print_menu()

    choice = input("Пожалуйста сделайте Ваш выбор: ")

    # Сложение,
    if choice == '1':
        # Проверка
        if result != "null":
            number_1 = result
        else:
            number_1 = float(input('Введите значение: '))

        # Математика, привел к флоату сразу что бы работать как с целыми так и с отрицательными числами,
        # далее по функциям то же самое.
        number_2 = float(input('Введите другое значение: '))
        print('{} + {} = '.format(number_1, number_2))
        result = number_1 + number_2
        print(number_1 + number_2)

        # Проверим захочет ли пользователь сохранить результат для последующих операций.
        var = input("Хотите ли Вы сохранить результат для последующих операций, если да введите y/n : ").lower()
        if var == 'y':
            print("Продолжаем.")
        if var == 'n':
            result = "null"
            print("")

    # Вычитание
    elif choice == '2':
        # Проверка
        if result != "null":
            number_1 = result
        else:
            number_1 = float(input('Введите уменьшаемое: '))

        # Запуск основной программы
        number_2 = float(input('Введите вычитаемое: '))
        print('{} - {} = '.format(number_1, number_2))
        result = number_1 - number_2
        print(number_1 - number_2)
        if var == 'y':
            print("Продолжаем.")
        # Проверим захочет ли пользователь сохранить резултат для последующих операций
        var = input("Хотите ли Вы сохранить результат для последующих операций, если да введите y/n : ").lower()
        if var == 'n':
            result = "null"
            print("")

    # Деление
    elif choice == '3':
        # Проверка
        if result != "null":
            number_1 = result
        else:
            number_1 = float(input('Введите делимое: '))

        # Запуск основной программы
        number_2 = float(input('Введите делитель: '))
        print('{} / {} = '.format(number_1, number_2))
        result = number_1 / number_2
        print(number_1 / number_2)

        # Проверим захочет ли пользователь сохранить резултат для последующих операций
        var = input("Хотите ли Вы сохранить результат для последующих операций, если да введите y/n : ").lower()
        if var == 'y':
            print("Продолжаем.")
        if var == 'n':
            result = "null"
            print("")

    # Умножение
    elif choice == '4':
        # Проверка
        if result != "null":
            number_1 = result
        else:
            number_1 = float(input('Введите значение 1: '))

        # Заупск основной программы
        number_2 = float(input('Введите множитель: '))
        print('{} * {} = '.format(number_1, number_2))
        result = number_1 * number_2
        print(number_1 * number_2)

        # Проверим захочет ли пользователь сохранить резултат для последующих операций
        var = input("Хотите ли Вы сохранить результат для последующих операций, если да введите y/n : ").lower()
        if var == 'y':
            print("Продолжаем.")
        if var == 'n':
            result = "null"
            print("")

    # Модуль числа
    elif choice == '5':
        # Проверка
        if result != "null":
            number_1 = result
        else:
            number_1 = float(input('Введите значение 1: '))

        # Запуск основной программы
        number_2 = float(input('Введите делитель: '))
        print('{} % {} = '.format(number_1, number_2))
        result = number_1 % number_2
        print(number_1 % number_2)

        # Проверим захочет ли пользователь сохранить резултат для последующих операций
        var = input("Хотите ли Вы сохранить результат для последующих операций, если да введите y/n : ").lower()
        if var == 'y':
            print("Продолжаем.")
        if var == 'n':
            result = "null"
            print("")

    # Корень числа
    elif choice == '6':
        # Проверка
        if result != "null":
            number_1 = result
        else:
            number_1 = float(input('Введите значение 1: '))

        # Запуск осноной программы
        number_2 = float(input('Enter Введите значение 2: '))
        print('{}^{} = '.format(number_1, number_2))
        result = number_1 ** (1 / number_2)
        print(number_1 ** (1 / number_2))

        # Проверим захочет ли пользователь сохранить резултат для последующих операций
        var = input("Хотите ли Вы сохранить результат для последующих операций, если да введите y/n : ").lower()
        if var == 'y':
            print("Продолжаем.")
        if var == 'n':
            result = "null"
            print("")

    # Выход из программы, выход из всего цыкла.
    elif choice == '7':
        var = input("Вы уверены что хотите выйти? Для подтверждения нажмите y/N : ").lower()
        if var == 'y':
            print("Программа завершена.")
            break

        elif var == 'n':
            print("")
    # Справка
    elif choice == '8':
        help_menu()
    # Неправильный ввод от пользователя
    else:
        invalid()