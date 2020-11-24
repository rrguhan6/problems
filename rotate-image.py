# https://leetcode.com/problems/rotate-image/


def print_mat(matrix):
    for i in matrix:
        for j in i:
            print(j, end="\t")
        print()
    print()


def rotate(matrix):
    row = len(matrix)

    print_mat(matrix)
    # transpose
    for i in range(0, row):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    print_mat(matrix)

    for i in range(0, row):
        matrix[i] = matrix[i][::-1]

    print_mat(matrix)


# rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
