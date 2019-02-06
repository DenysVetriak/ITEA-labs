# 1. Запросить у пользователя целое число.
# 2. Вывести на экран число в представлении целого числа, вещественного числа, логического значения, строки.
# 3. Запросить у пользователя ещё одно целое число.
# 4. Выполнить операции + и * над всеми вариантами представления первого числа и второго числа, если они допустимы.
# 5. Результаты операций вывести на экран, сопровождая вразумительным текстом о то какая операция над какими типами
# операндов была выполнена.


request_some_number = int(input('Please write some number: '))
# Присваеваем переменные да бы было удобнее далее работать.
some_number = request_some_number
number1_float = float(some_number)
number1_bool = bool(some_number)
number1_str = str(some_number)
print("Наше целое число: ", request_some_number)
print("Наше вещественное число: ", number1_float)
print("Наше логическое значение: ", number1_bool)
print("Наша строка: ", number1_str)

# Тоже свмое делаем со вторым числом.
request_some_number2 = int(input('Please write second number: '))
some_number2 = request_some_number2
number2_float = float(some_number2)
number2_bool = bool(some_number2)
number2_str = str(some_number2)
print("------------------------------------------------")
print("Сейчас мы выполним операции со знаком + : ", "\n")
print("int + int = ", some_number + some_number2)
print("str + float = ", some_number + number2_float)
print("int + bool = ", some_number + number2_bool)
print("float + int = ", number1_float + some_number2)
print("float + float = ", number1_float + number2_float)
print("float + bool = ", number1_float + number2_bool)
print("bool + int = ", number1_bool + some_number2)
print("bool + float = ", number1_bool + number2_float)
print("bool + bool = ", number1_bool + number2_bool)
print("str + str = ", number1_str + number2_str)
print("------------------------------------------------")

print("Сейчас мы выполним операции со знаком * : ", "\n")
print("int * int = ", some_number * some_number2)
print("int * float = ", some_number * number2_float)
print("float * int = ", number1_float * some_number2)
print("int * bool = ", some_number * number2_bool)
print("bool * int = ", number1_bool * some_number)
print("float * bool = ", number1_float * number2_bool)
print("bool * float = ", number1_bool * number2_float)
print("int * str = ", some_number * number2_str)
print("str * int = ", number2_str * some_number)
print("str * bool = ", number1_str * number2_bool)
print("bool * str = ", number1_bool * number2_str)
print("bool * bool = ", number1_bool * number2_bool)
print("float * float = ", number1_float * number2_float)

