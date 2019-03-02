# Отвчает за ввод текста с клавиатуры
def input_text():
    some_list = []
    while True:
        text = input("Введите текст: ").lower()
        print("Для подсчета статистики после ввода текста нажите (Enter)")
        if text != "":
            some_list.append(text)
        else:
            return some_list


# Делаем подсчет цифр
def count_numbers(one_symbol, exclude):
    count = 0
    for i in one_symbol:
        if i in exclude:
            continue
        elif i.isdigit():
            count += 1
    print("Всего цифр = {}".format(count))


# Подсчет количества символов в строке которую ввел пользователь
def count_symbols(one_symbol, exclude):
    chars_stat = {}
    for unique_symbols in one_symbol:
        if unique_symbols in exclude:
            continue
        elif unique_symbols in chars_stat:
            chars_stat[unique_symbols] += 1
        else:
            chars_stat[unique_symbols] = 1
    print("<--- Статистика символов ---")
    for key, value in chars_stat.items():
        print("{} = {}".format(repr(key), value))
    print("--- Статистика символов --->")


# Просчет уникальнх символов в том что ввел пользователь
def count_word(text, exclude):
    words_stat = {}
    aggregate_list = []
    # Преобразовывваем начальный ввод пользователя в удобный для нас список с которым дальше будем работать
    for _value in text:
        _new_value = str(_value).split()
        aggregate_list = aggregate_list + _new_value
    for unique_words in aggregate_list:
        if unique_words in exclude:
            continue
        elif unique_words in words_stat:
            words_stat[unique_words] += 1
        else:
            words_stat[unique_words] = 1
    print("<--- Статистика слов ---")
    for key, value in words_stat.items():
        print("{} = {}".format(repr(key), value))
    print("--- Статистика слов --->")


# Функция преобразования *args в список для того что бы на выходе получить список из элементов
def check_exclude(__exclude_list):
    exclude_list = []
    # запускаем цикл по списку *args если элемент равен списку то дописываем в новый список
    # если нет то просто добавляем в конец списка
    for element in __exclude_list:
        if type(element) == list:
            exclude_list.extend(element)
        else:
            exclude_list.append(element)
    return exclude_list


def text_stat(text, *args):
    exclude_list = check_exclude(list(args))
    one_symbol = list(''.join(text))
    print("Всего строк = {}".format(len(text)))
    count_numbers(one_symbol, exclude_list)
    count_symbols(one_symbol, exclude_list)
    count_word(text, exclude_list)


text = input_text()
text_stat(text)
