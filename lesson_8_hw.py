low = 0 # отмечаем минимальное значение
max = 101 # отмечаем максимальное значение

attemts = 0 # счетчик, будем считать кол-во попыток
list_1 = [] # список сюда сохраним все попытки

quess = int(input('Загадайте число от 1 до 100: '))
attemts += 1
while True:
    mid = (low + max) // 2 # получаем середину
    print(f'ваше число {mid}?')
    is_true = input('Больше/Меньше, да: ').title()
    if is_true == 'Больше':
        low = mid # если число больше середины то приравниваем min к середине
        attemts += 1 # прибавляем плюс 1 к количеству попыток
        list_1.append(mid) # добавляем попытку в список
    elif is_true == 'Меньше':
        max = mid # если меньше то max приравниваем к середине
        attemts += 1
        list_1.append(mid)
    elif is_true == 'Да':
        attemts += 1
        list_1.append(mid)
        with open('results.txt', 'w') as file: # сохраняем все в файл
            file.write(f'количество попыток: {attemts}\nзагаданное число: {quess}\nсписок попыток: {list_1}')
        break
    else:
        print('Вводите только больше/меньше, да.')