data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

# Шаг 1: создаём пустые списки
letters = []
numbers = []

# Шаг 2: разделяем элементы по типу
for i in data_tuple:
    if isinstance(i, str):
        letters.append(i)
    else:
        numbers.append(i)

# Шаг 3: удаляем 6.13, переносим True в letters
numbers.remove(6.13)
numbers.remove(True) # True == 1, чтобы не мешал
letters.append(True)

# Вставим 2 между 3 и 1
numbers.insert(1,2)

# Шаг 4: сортируем numbers, реверсируем letters, меняем буквы
numbers.sort()
letters.reverse()

# Заменим 'g' на 'G', 'C' на 'c'
letters[1] = 'G'
letters[7] = 'c'

# Шаг 5: возводим числа в квадрат
for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2

# Шаг 6: преобразуем в кортежи
letters = tuple(letters)
numbers = tuple(numbers)

print(letters)
print(numbers)