# Изменить программу из Задачи №1 так, чтобы вывод на экран статистики по словам и символам был упорядочен по алфавиту
# Внимание! Использование сторонних и стандартных модулей недопустимо!
# Например такое не приемлемо:
#
# from collections import OrderedDict


def input_text():
    some_text = []
    while True:
        text = input("Введите текст: ").lower()
        print("Для подсчета статистики после ввода текста нажите (Enter)")
        if text != "":
            some_text.append(text)
        else:
            return some_text


def count_numbers(one_symbol):
    count = 0
    for i in one_symbol:
        if i.isdigit() == True:
            count += 1
    print("Всего цифр = {}".format(count))



def count_symbols(one_symbol):
    chars_stat = {}
    for unique_symbols in one_symbol:
        if unique_symbols in chars_stat:
            chars_stat[unique_symbols] += 1
        else:
            chars_stat[unique_symbols] = 1
    key_list = list(chars_stat.keys())
    key_list.sort()
    print("<--- Сортировка Статистика символов ---")
    for _key in key_list:
        print("{} = {}".format(repr(_key), chars_stat[_key]))
    print("--- Сортировка Статистика символов --->")


def count_word(text):
    words_stat = {}
    aggregate_list = []
    for _value in text:
        _new_value = str(_value).split()
        aggregate_list = aggregate_list + _new_value
    for unique_words in aggregate_list:
        if unique_words in words_stat:
            words_stat[unique_words] += 1
        else:
            words_stat[unique_words] = 1

    key_list = list(words_stat.keys())
    key_list.sort()
    print("<--- Сортировка Статистики Слов ---")
    for _key in key_list:
        print("{} = {}".format(repr(_key), words_stat[_key]))
    print("--- Сортировка Статистики Слов --->")


def text_stat(text):

    one_symbol = list(''.join(text))
    print("Всего строк = {}".format(len(text)))
    count_numbers(one_symbol)
    count_symbols(one_symbol)
    count_word(text)


text = input_text()
text_stat(text)
