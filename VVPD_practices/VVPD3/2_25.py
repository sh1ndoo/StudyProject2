def find_multiple_in_a_multiple_in_b(A, B):
    multiple_in_A = {x for x in A if A.count(x) > 1}
    multiple_in_B = {x for x in B if B.count(x) > 1}
    result = [x for x in multiple_in_A if x in multiple_in_B]
    return result


# Пример массивов A и B
A = [1, 2, 3, 4, 5, 6, 2, 5, 7]
B = [2, 2, 3, 3, 7, 8, 9, 3]

A1 = list(input('Введите массив А через пробел\n').split())
B1 = list(input('Введите массив B через пробел\n').split())

print(f'Результат с примерными данными:\n{find_multiple_in_a_multiple_in_b(A, B)}\nРезультат в введёнными данными:\n{find_multiple_in_a_multiple_in_b(A1, B1)}')