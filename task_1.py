# Напишите функцию для транспонирования матрицы.
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]


def transpose_matrix(user_matrix) -> list:
    """ Функция меняет местами строки и колонки матрицы """
    rows = len(user_matrix)
    columns = len(user_matrix[0])

    transposed = [[0 for _ in range(rows)] for _ in range(columns)]

    for i in range(rows):
        for j in range(columns):
            transposed[j][i] = user_matrix[i][j]

    return transposed


my_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose_matrix(my_matrix)
print(transposed_matrix)