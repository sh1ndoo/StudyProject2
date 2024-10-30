def find_unique_in_a_multiple_in_b(A, B):
    unique_in_A = [x for x in A if A.count(x) == 1]
    multiple_in_B = {x for x in B if B.count(x) > 1}
    result = [x for x in unique_in_A if x in multiple_in_B]
    return result
def find_multiple_in_a_multiple_in_b(A, B):
    multiple_in_A = {x for x in A if A.count(x) > 1}
    multiple_in_B = {x for x in B if B.count(x) > 1}
    result = [x for x in multiple_in_A if x in multiple_in_B]
    return result
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
            ch = input('Введите номер программы для выполнения (1, 2, 3)\n')
            if ch not in ('1', '2', '3'):
                print('Вводите цифру от 1 до 3')
                print(menu)
                continue
            A1 = list(input('Введите массив А через пробел\n').split())
            B1 = list(input('Введите массив B через пробел\n').split())
            match ch:
                case '1':
                    print(f'Результат в введёнными данными:\n{find_unique_in_a_multiple_in_b(A1, B1)}')
                case '2':
                    print(f'Результат в введёнными данными:\n{find_multiple_in_a_multiple_in_b(A1, B1)}')
                case '3':
                    print(f'Результат в введёнными данными:\n{find_unique_in_a_unique_in_b(A1, B1)}')
        case '2':
            ch = input('Введите номер программы для выполнения (1, 2, 3)\n')
            if ch not in ('1', '2', '3'):
                print('Вводите цифру от 1 до 3')
                print(menu)
                continue
            match ch:
                case '1':
                    print(f'Результат с примерными данными:\n{find_unique_in_a_multiple_in_b(A, B)}')
                case '2':
                    print(f'Результат с примерными данными:\n{find_multiple_in_a_multiple_in_b(A, B)}')
                case '3':
                    print(f'Результат с примерными данными:\n{find_unique_in_a_unique_in_b(A, B)}')
        case '3':
            print(menu)
        case '0':
            break
        case _:
            print('Пожалуйста следуйте инструкции')