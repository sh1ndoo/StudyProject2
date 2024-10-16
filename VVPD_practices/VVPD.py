"""
Вычисление значения функции с переданным через командную строку аргументом
"""
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-x', help="Введите x для вычисления значения функции")

x = parser.parse_args().x
# Проверяем переданное значение, чтобы избежать нежелательных ошибок
if x is None:
    print('Введите число')
    quit()
else:
    for i in x:
        if i not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-'):
            print('Только числа')
            quit()
        elif x == '-1':
            print('Деление на 0')
            quit()
x = float(x)
y = 7 * (x ** 2) + (2 / ((1 + x) ** 0.5))
print(y)
