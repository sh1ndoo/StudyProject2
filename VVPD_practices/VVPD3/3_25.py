def find_multiple_in_a_multiple_in_b(A, B):
    unique_in_A = set([x for x in A if A.count(x) == 1])
    unique_in_B = set([x for x in B if B.count(x) == 1])
    result = unique_in_A ^ unique_in_B
    return result


# Пример массивов A и B
A = [1, 2, 3, 4, 5, 6, 2, 5, 7]
B = [2, 2, 3, 3, 7, 8, 9, 3]

print(find_multiple_in_a_multiple_in_b(A, B))