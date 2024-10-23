def find_unique_in_a_unique_in_b(A, B):
    unique_in_A = set([x for x in A if A.count(x) == 1])
    unique_in_B = set([x for x in B if B.count(x) == 1])
    result = list(unique_in_A ^ unique_in_B)
    return result


# Пример массивов A и B
A = [1, 2, 3, 4, 5, 6, 2, 5, 7]
B = [2, 2, 3, 3, 7, 8, 9, 3]

menu = '''Выберите действие(ввести цифру):
1 Выполнить программу с собственными данными
2 Выполнить программу с данными-примерами
3 Вывести меню
0 Остановить программу'''
print(menu)
while True:
    ind = input()
    match ind:
        case '1':
            A1 = list(input('Введите массив А через пробел\n').split())
            B1 = list(input('Введите массив B через пробел\n').split())
            print(f'Результат в введёнными данными:\n{find_unique_in_a_unique_in_b(A1, B1)}')
        case '2':
            print(f'Результат с примерными данными:\n{find_unique_in_a_unique_in_b(A, B)}')
        case '3':
            print(menu)
        case '0':
            break
        case _:
            print('Пожалуйста следуйте инструкции')