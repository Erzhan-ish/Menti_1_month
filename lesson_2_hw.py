date = int(input('Введите день рождения: '))
month = int(input('Введите месяц рождения: '))
if (21 <= date <= 31 and month == 3) or (month == 4 and 1 <= date <= 20):
    print("Овен")
elif (21 <= date <= 31 and month == 4) or (month == 5 and 1 <= date <= 21):
    print("Телец")
elif (22 <= date <= 31 and month == 5) or (month == 6 and 1 <= date <= 21):
    print("Близнецы")
elif (22 <= date <= 31 and month == 6) or (month == 7 and 1 <= date <= 22):
    print("Рак")
elif (23 <= date <= 31 and month == 7) or (month == 8 and 1 <= date <= 21):
    print("Лев")
elif (22 <= date <= 31 and month == 8) or (month == 9 and 1 <= date <= 23):
    print("Дева")
elif (24 <= date <= 31 and month == 9) or (month == 10 and 1 <= date <= 23):
    print("Весы")
elif (24 <= date <= 31 and month == 10) or (month == 11 and 1 <= date <= 22):
    print("Скорпион")
elif (23 <= date <= 31 and month == 11) or (month == 12 and 1 <= date <= 22):
    print("Стрелец")
elif (23 <= date <= 31 and month == 12) or (month == 1 and 1 <= date <= 20):
    print("Козерог")
elif (21 <= date <= 31 and month == 1) or (month == 2 and 1 <= date <= 19):
    print("Водолей")
elif (20 <= date <= 31 and month == 2) or (month == 3 and 1 <= date <= 20):
    print("Рыбы")
else:
    print("Ошибка: Дата введена неправильно!")
