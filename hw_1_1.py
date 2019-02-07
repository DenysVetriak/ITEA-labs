# # 1. Запросить у пользователя имя и фамилию.
print('---------') # Обычный прочерк для удобства, тоже самое далее по коду.
name_user = input('Write your first name: ')
print(type(name_user))
print('---------')
wait = input('Press Enter to continue')
print('---------')
second_name = input('Write your second name: ')
print(type(second_name))
#
# # 2. Поприветсвовать пользователя с использованием его имени и фамилии.
print('---------')
print("Hello: " + name_user + second_name)

# 3. Запросить День даты рождения (цело число).
# 4. Запросить Месяц даты рождения (цело число).
# 5. Запросить Год даты рождения (цело число).
a = start_year = 2019
b = start_month = 1
c = start_date = 31
print("Please enter a date by the requested order :")
y = year = input("Please Enter the Year: ")
m = month = input("Please Enter the Month: ")
d = day = input("Please Enter the Day: ")
st_date = [str(y+"." +m+"."+d)]
print("Your Date is: " + str(st_date))
# 6. Вывести количество прожитых лет (цело число).
# 7. Вывести количество прожитых месяцев (цело число).
# 8. Вывести количество прожитых дней, месяцев, лет до даты начала курса 31.01.2019 \
# без учёта високосных лет и считая, что среднее количество дней в месяце = 30.
print('--------------------------------------------')
# Расчет количества дней прожитых от дня рождения до даты производился по формуле: \
# N=360*G+30(M-1)+D, где G, M, D, год, месяц, день.  Дальше результаты вычетаются, \
# получаем общее количество прожитых дней.
how_days_lived_person = int(a)*360+30*int(b)-1+int(c)
how_days_lived_person2 = int(y)*360+30*int(m)-1+int(d)
# Присваеваем переменную что бы было дальше удобнее работать
how_days_lived = how_days_lived_person - how_days_lived_person2
# Для уверенности выдаем результат
print(int(how_days_lived))
# Узнаем количество полных прожитых лет от дня рождения
full_years = how_days_lived // 360
# Выводим результат
print("You lived " + str(full_years) + " full years")
# Узнаем общее количество прожитых месяцев от дня рождения, при учете что в месяце 30 дней.
month_lived = int(how_days_lived) // 30
# Выводим
print("You lived full " + str(month_lived) + " month ")
# Далее выводим дни и месяцы в соотношении пройденного времени от дня рождения до назначенной даты
how_days_left = how_days_lived - month_lived * 30
how_month_left = (how_days_lived - (full_years * 360)) // 30
# Выводим результат и на конец добавляем форматирование для красоты.
print("Before course started you lived {}-years {}-month {}-days"  .format(full_years, how_month_left, how_days_left))




