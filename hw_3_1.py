# 1. Пользователь вводит два любых числа a и b. Тип чисел может быть как int, так и float;
# 2. Выполняется вызов функции;
# 3. Результат выводится на экран с вразумительным пояснением.


def hello_msg():
    print("Здравствуйте если хотите продолжить работу нажмите GO, если же нет, введите EXIT")


def main():
    exit = 'EXIT'
    hello_msg()
    res = 0
    okay_msg = 'Вы вышли из программы...'
    while res == 0:
        go_msg = input('Пожалуйста сделайте Ваш выбор >>> ')
        if go_msg.upper() == 'GO':
            # Go to count!
            res = 1
            print('Дальше введите желаемые натуральные числа: ')

            while res == 1:
                num1 = input_num('first')
                if num1.upper() == exit:
                    print(okay_msg)
                    break
                elif check_num(num1):
                    res = 2
                    while res == 2:
                        num2 = input_num('second')
                        if num2.upper() == exit:
                            print(okay_msg)
                            break
                        elif check_num(num2):
                            res = 2
                            num1r = convert_min(num1, num2)
                            num2r = convert_max(num1, num2)

                            sum_nat = sum_natural_numbers(num1r, num2r)
                            if sum_nat == 0:
                                print(f'Между введенными числами нет натуральных чисел {num1} and {num2}')
                            else:
                                print(f'Сумма всех натуральных чисел между {num1} and {num2} равна {sum_nat}')
                            break

        elif go_msg.upper() == exit:
            print(okay_msg)
            break
        else:
            print('Попробуйте еще.')


def check_num(arg):
    # Проверяем аргумент числовой или нет
    if arg:
        arg = ((arg.replace('.', '', 1))[0].replace('-', '') + arg.replace('.', '', 1)[1:]).strip()
        return arg.isnumeric()


def convert_max(arg1, arg2):
    # Проверяем какой из аргументов больше, коневерируем во float и обратно присваеваем к инту.
    if float(arg1) >= float(arg2):
        return int(float(arg1))
    else:
        return int(float(arg2))


def convert_min(arg1, arg2):
    # Проверяем какой из аргументов меньше, коневерируем во float и обратно присваеваем к инту.
    ROUND_C = 0.4
    if float(arg1) <= float(arg2):
        return round(float(arg1) + ROUND_C)
    else:
        return round(float(arg2) + ROUND_C)


def sum_natural_numbers(arg1, arg2):
    # Вычисляем сумму натуральных чисел
    sum_nat = 0
    for i in range(arg1, arg2 + 1):
        if i >= 0:
            sum_nat += i
    return sum_nat


def input_num(nn):
    # Просим пользователя ввести число и возвращаем
    num = input(f'Put here your {nn} number >>> ')
    return num.strip()


main()   # Делаем вызов
