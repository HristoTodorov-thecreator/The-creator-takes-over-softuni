def rotate_matrix(matrix):
    matrix_length = len(matrix)


    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()


mtrx = []

class MatrixContentError(Exception):

    pass

class MatrixSizeError(Exception):
    pass

def check(line):
    return all(s.isdigit() for s in line)

while True:
    line = input().split()

    if not line:
        break
    mtrx.append(line)

    if not check(line):
        raise MatrixContentError('The matrix must consist of only integers')


for m in mtrx:
    if len(m) != len(mtrx):
        raise MatrixSizeError('The size of the matrix is not a perfect square')

rotate_matrix(mtrx)


for row in mtrx:
    print(*row, sep=' ')