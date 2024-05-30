def get_matrix(n, m, value):
    matrix = []
    for _ in range(n):
        row = []  #
        for _ in range(m):
            row.append(value)
        matrix.append(row)
    return matrix

result1 = get_matrix(6, 9, 12)
result2 = get_matrix(5, 2, 48)
result3 = get_matrix(2, 12, 55)

print(result1)
print(result2)
print(result3)
