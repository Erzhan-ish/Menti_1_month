numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # возвращает True, если x чётное.
print(even_numbers)  # [2, 4, 6] filter

squares = list(map(lambda x: x**2, numbers)) # возводит x в квадрат
print(squares)  # [1, 4, 9, 16, 25, 36] map



def nearest_number(sequence, target):
    sorted_sequence = sorted(sequence, key=lambda x: abs(x - target)) # Сортируем элементы по абсолютной разнице
    return target, sorted_sequence
print(nearest_number([312, 996, 31, 1991], 1000))



def get_element_by_index(data=[1, 2, 3, 4, 5]):
    while True:
        try: # открываем блок try чтобы ловить ошибки без краша программы
            user_input = input(f"Введите индекс элемента от 0 до {len(data) - 1} (или 'exit' для выхода): ")
            if user_input.lower() == 'exit':
                print("Выход из программы.")
                break
            index = int(user_input) # Преобразуем в целое число
            print(f"Элемент по индексу {index}: {data[index]}") # выводим элемент по индексу
        except ValueError:
            print("Пожалуйста, введите числовой индекс или 'exit'.") # если ввели не число и не exit сообщаем об этом
        except IndexError:
            print(f"Индекс вне диапазона! Введите число от 0 до {len(data) - 1}.") # сообщаем правильный диапазон индекса

get_element_by_index()  # По умолчанию [1, 2, 3, 4, 5]
get_element_by_index("Hello!")  # Можно также передать строку или список