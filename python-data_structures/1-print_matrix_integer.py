def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print("{:2} {:2} {:2}".format(*row))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)