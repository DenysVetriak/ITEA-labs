# 1. Пользователь вводит два числа a и b. Тип чисел может быть как int(), так и float();
# 2. Выведите сумму всех натуральных чисел от меньшего до большего (включительно);
# 3. Рекомендую строго соблюдать определние "натуральное число".

# Даем 3 попытки на ввод, просто что бы показать что выучили.
def type_number():
    attempts = 3
    while attempts:
        attempts -= 1
        number = input("Type some number: ").strip().lstrip('+')
        number_ = number.lstrip('-').replace('.', '', 1).isdigit()
        if number_:
            number = float(number)
            return number
        else:
            print("You wrote not a number")
    else:
        exit("Yours 3 attempts is gone")


# Высчитываем сумму натуральных чисел
def sum_numbers():
    # просим ввести два любых числа
    print('----------------------')
    first_number = type_number()
    print('----------------------')
    second_number = type_number()
    print('----------------------')
    # Делаем замену в случае если введенное пользователем второе число будет больше чем первое.
    if first_number > second_number:
        first_ = first_number
        first_new = second_number
        second_new = first_
    else:
        first_new = first_number
        second_new = second_number

    if first_new <= 1:
        first_new = 1

    # Приводим левую сторону к целому числу если остаток 0 то преобразовываем в integer
    first_normalize = first_new % 1
    if first_normalize == 0:
        first_normalize = int(first_new)
    else:
        first_normalize = int(first_new + 1)

    # Приводим правую сторону к нулю
    second_normalize = second_new % 1
    second_normalize = int(second_new - second_normalize)

    # Высчитываем сумму всего диапазона от начала до конца
    result_sum = 0
    while first_normalize <= second_normalize:
        result_sum += first_normalize
        first_normalize += 1
    print("Sum of all natural numbers is [{},{}] and even {}"
          .format(first_number, second_number, result_sum))
    print('---------------------------------------------------')


sum_numbers()
