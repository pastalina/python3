# Задание 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними
# находится букв.

letter1 = input('Введите первую букву латинского алфавита: ')
letter2 = input('Введите вторую букву латинского алфавита: ')

loc1 = ord(letter1) - 96
loc2 = ord(letter2) - 96
dist = loc2 - loc1 - 1

print(f'Первая буква находится на {loc1} месте, вторая буква находится на {loc2} месте. Букв между первой и второй '
      f'буквами: {dist}')