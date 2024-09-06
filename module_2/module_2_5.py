def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[-1].append(value)


    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

# Ваша функция get_matrix имеет правильную структуру и логику создания матрицы. 
# Однако, требуется небольшая оптимизация: 
# - вместо создания дополнительной переменной add для каждой строки матрицы, можно просто добавлять пустой список
# напрямую в matrix (в соответствии с кол-вом строк). Также, важно помнить, что в Python списки передаются по ссылке,
# поэтому добавление одного и того же списка несколько раз в matrix приведет к тому, что все строки матрицы будут
# ссылаться на один и тот же список. Это может вызвать проблемы при изменении значений в матрице. 
# Поэтому рекомендую создавать новый пустой список для каждой строки матрицы.
# А далее уже добавлять в этот список value (в соответствии с количеством столбцов).
#
# Прошу доработать и направить решение повторно.


# def get_matrix(n, m, value):
#     matrix = []
#     for i in range(n):
#         add = []
#         matrix.append(add)
#         for j in range(m):
#             add.append(value)
#     return matrix
#
# result1 = get_matrix(2, 2, 10)
# result2 = get_matrix(3, 5, 42)
# result3 = get_matrix(4, 2, 13)
# print(result1)
# print(result2)
# print(result3)

# matrix = k for x in matrix if matrix != []
# for k in matrix:
#     if k == 0:
#         matrix.pop(k)
#         return matrix
# matrix.remove(None)
# col_ = []
# add.append(col_)
