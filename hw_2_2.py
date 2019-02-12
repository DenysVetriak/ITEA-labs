# 1. Пользователь вводит порядковый номер Числа Фибоначчи - n
# 2.Программа вычисляет этот элемент ряда Фибоначчи и выводит его на экран (с вразумительным сообщением).

# Пример работы программы:
# Введите порядковый номер: 6
# Элемент [6] ряда Чисел Фибоначчи = 8

def fibonacci_number():
    # Запросим у пользователя натуральное число.
    fib_number = input("Введите номер элемента ряда Фибоначчи, больше 0: ")
    # Убедимся что число целое и натуральное.
    check_fibonacci = fib_number.isdigit()
    if check_fibonacci:
        fib_number = int(fib_number)
        return fib_number
    else:
        print("Номер ряда должен быть целым числом")


def fib_math():
    fibo_number = fibonacci_number()
    while fibo_number:
        if fibo_number > 0:
            break
        else:
            print("Ваше число должно быть больше ноля: ")
    else:
        exit("Перезапустите программу и введите число правильно")

    fib_number1 = 1
    fib_number2 = 1
    iterator = 0
    while iterator < (fibo_number - 2):
        fibo_sum = fib_number1 + fib_number2
        fib_number1 = fib_number2
        fib_number2 = fibo_sum
        iterator += 1
    print("Элемент [{}] ряда Числа Фибоначчи = {}".format(fibo_number, fib_number2))


fib_math()
