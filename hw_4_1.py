# Задача №1 (Статистика слов)

# 1. В основной части программы:
# 2. Пользователь вводит с клавиатуры строки.
# 3. Пустая строка означает прекратить ввод.
# 4. Строки сохраняются в список. Далее этот список будем называть "Текст"
# 5. Программа вызывает функцию text_stat в которую передаёт Текст (см. описание функции ниже).
# 6. Программа выводит на экран статистику, которую вернула функция text_stat:
# для статистики слов - таблица, в которой
# первый столбец - слово
# второй столбец - количество повторений слова
# для статистики символов - таблица в которой
# первый столбец - символ, если не печатный, то его печатное представление, например для символа табуляции - это "\t"
# второй столбец - количество повторений символа
# для цифр - количество цифр в Тексте
# для строк - количество строк


# Ввод текста с клавиатруры
def input_text():
    some_list = []
    while True:
        text = input("Введите текст: ").lower()
        print("Для подсчета статистики после ввода текста нажите (Enter)")
        if text != "":
            some_list.append(text)
        else:
            return some_list


# Подсчета цифер в программе
def count_numbers(one_symbol):
    count = 0
    for i in one_symbol:
        if i.isdigit():
            count += 1
    print("Всего цифр = {}".format(count))


# Вычисление количетва символов в пользовательском вводе
def count_symbols(one_symbol):
    chars = {}
    # Запускаем цикл по списку который состоит из одиночных символов
    # и складываю его в словарь
    for unique_symbols in one_symbol:
        # Если символ уже есть в словаре то к его количеству добавляем один
        # Если нет то ставим единицу
        if unique_symbols in chars:
            chars[unique_symbols] += 1
        else:
            chars[unique_symbols] = 1
    print("<--- Статистика символов ---")
    for key, value in chars.items():
        print("{} = {}".format(repr(key), value))
    print("--- Статистика символов --->")


# Подсчет уникальных слов
def count_word(text):
    words_stat = {}
    separate_list = []
    # Преобразовывваем начальный ввод пользователя в удобный для нас список с которым дальше будем работать
    for _value in text:
        _new_value = str(_value).split()
        separate_list = separate_list + _new_value
    for unique_words in separate_list:
        if unique_words in words_stat:
            words_stat[unique_words] += 1
        else:
            words_stat[unique_words] = 1
    # Делаем вывод
    print("<--- Статистика слов ---")
    for key, value in words_stat.items():
        print("{} = {}".format(repr(key), value))
    print("--- Статистика слов --->")


def text_stat(text):
    one_symbol = list(''.join(text))
    print("Всего строк = {}".format(len(text)))
    count_numbers(one_symbol)
    count_symbols(one_symbol)
    count_word(text)


text = input_text()
text_stat(text)
