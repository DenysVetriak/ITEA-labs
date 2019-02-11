# 1. Пользователь вводит два числа a и b. Тип чисел может быть как int(), так и float();
# 2. Выведите сумму всех натуральных чисел от меньшего до большего (включительно);
# 3. Рекомендую строго соблюдать определние "натуральное число".

# Пишем функцию где просим пользователя ввести случайное число.
def type_first_number():
    ATTEMPTS = 2  # Ставлю колчичество попыток на воод 2, делали на уроке, решил добавить.
    while ATTEMPTS:
        ATTEMPTS -= 1
        # Присваеваем флоат что бы работать с целыми и вещественными числами.
        number_one = float(input("Type please first natural number: "))
        # Контролировать ввод пользователя еще не научились так как не работали с исключениями, других сппособов не знаю
        if number_one >= 0:
            return number_one
        else:
            ValueError(print("Number, {}, is not natural number".format(number_one)))  # Форматируем
    else:
        exit("Your attempts are finished, try to reload program")


# Повторяем все то же самое для второго числа:
def type_second_number():
    ATTEMPTS = 2
    while ATTEMPTS:
        ATTEMPTS -= 1
        number_two = float(input("Type please second natural number: "))
        if number_two >= 0:
            return number_two
        else:
            ValueError(print("Number, {}, is not natural number".format(number_two)))  # Форматируем
    else:
        exit("Your attempts are finished, try to reload program")


# Считаем сумму введенных натуральных чисел:
def sum_natural():
    x1 = None
    x2 = None
    ATTEMPTS = 3
    while ATTEMPTS:  # Убедимся что числа введены правильно и первое число меньше второго.
        ATTEMPTS -= 1
        x1 = type_first_number()
        x2 = type_second_number()
        if x1 <= x2:
            break
        else:
            print("Number {} more than {}, wrong format".format(x1, x2))  # Форматируем
    else:
        exit(" You typed wrong numbers for 3 times")

    # Приводим левую часть к натуральному числу
    first_natural = x1 % 1
    if first_natural == 0:
        first_natural = int(x1)
    else:
        first_natural = int(x1 + 1)

    #  Тут же делаем со второй то же самое.
    second_natural = x2 % 1
    second_natural = int(x2 - second_natural)

    # Высчитываем сумму чисел от меньшего до большего:
    result = 0
    while first_natural <= second_natural:
        result += first_natural
        first_natural += 1
    print("Sum of all natural numbers from [{},{}] equals {}".format(x1, x2, result))   # Форматируем и выводим


sum_natural()
