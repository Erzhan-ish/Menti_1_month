while True:
    vowels = ['a', 'e', 'i', 'o', 'y', 'u', 'A', 'E', 'I', 'O', 'Y', 'U'
        , 'я', 'Я', 'ю', 'Ю', 'ы', 'Ы', 'э', 'Э', 'ё', 'Ё', 'а', 'А', 'о', 'О', 'е', 'Е', 'у', 'У', 'и', 'И']

    word = input('Введите слово: ')
    if word == 'stop':
        break

    count_vowels = 0
    count_cons = 0
    counts_letters = 0

    for letter in word:
        if letter in vowels:
            count_vowels += 1
        else:
            count_cons += 1
        counts_letters += 1
    percent_vowels = round(count_vowels * 100 / counts_letters,2)
    percent_cons = round(count_cons * 100 / counts_letters,2)

    print(f'Слово: {word}')
    print(f'Количество букв: {counts_letters}')
    print(f'Гласные: {count_vowels}')
    print(f'Согласные: {count_cons}')
    print(f'гласные/согласные: {percent_vowels}% / {percent_cons}%')
