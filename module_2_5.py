def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix

#тест функции
result1 = get_matrix(4, 6, 13)
result2 = get_matrix(2, 7, 9)
result3 = get_matrix(4, 4, 36)
print(result1)
print(result2)
print(result3)