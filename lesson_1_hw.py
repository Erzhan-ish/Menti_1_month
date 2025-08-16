monday = float(input('введите расход за понедельник '))
tuesday = float(input('введите расход за вторник '))
wednesday = float(input('введите расход за среду '))
thursday = float(input('введите расход за четверг '))
friday = float(input('введите расход за пятницу '))
saturday = float(input('введите расход за субботу '))
sunday = float(input('введите расход за воскресенье '))

summ_expense = monday + tuesday + wednesday + thursday + friday + saturday + sunday
print(f'общая сумма {summ_expense} ')

average_expense = round((summ_expense / 7), 1)
print(f'средний расход {average_expense} ')
