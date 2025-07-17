data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for i in data_tuple:
    if isinstance(i, str):
        letters.append(i)
    if isinstance(i, (int, float)):
        numbers.append(i)
numbers.pop(0)
numbers.pop(0)
letters.append(True)
numbers.insert(1,2)
numbers.sort()
letters.reverse()
letters[1] = 'G'
letters[7] = 'c'
for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2

letters = tuple(letters)
numbers = tuple(numbers)

print(letters)
print(numbers)