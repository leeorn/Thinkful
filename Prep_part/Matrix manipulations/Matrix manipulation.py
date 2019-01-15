import numpy as np
import time
# checks if it's 2D array
# addition
# subtraction
# multiplication
# find inverse


def check2D(matrix1, matrix2):
    if np.shape(matrix1) != (2,2) or np.shape(matrix2) != (2,2):
           print("not legal")
    else:
        print("continue")

a = [[1, 2], [3, 4], [3, 4]]
b = [[5, 6], [7, 8], [1, 2]]


# Adding the 2 given matrices if possible
def addition(matrix1, matrix2):
    t_start = time.clock()
    if np.shape(matrix1) == np.shape(matrix2):          # check if they're the same size
        new_matrix = []                                 # create an empty list

        for row in range(len(matrix1)):                 # go through the row length
            new_matrix.append([])                       # create a new list, in side that position
            for col in range(len(matrix1[row])):        # go number by number and add them
                 new_matrix[row].append(matrix1[row][col] + matrix2[row][col])

    t_end = time.clock()
    t_total = (t_end - t_start) * (10 ** 6)
    print("This function took {} nano seconds".format(t_total))

    return new_matrix


# c = addition(a, b)
# print(c)


# Multiply the given matrix with a given scalar
def scalar_multi(matrix, num):
    if type(num) == int or type(num) == float:
        new_matrix = []
        for row in range(len(matrix)):
            new_matrix.append([])
            for col in range(len(matrix[row])):
                new_matrix[row].append(matrix[row][col] * num)

        return new_matrix
    else:
        return None


def matrix_multi(matrix1, matrix2):
    # checks the column length of the first matrix is the same as the rows in the second one
    if np.shape(matrix1)[1] != np.shape(matrix2)[0]:
        return None
    # initialize a new matrix size matrix1[0] x matrix2[1]
    new_matrix = []
    for row in range(len(matrix1)):
        new_matrix.append([])
        for col in range(len(matrix2[0])):
            new_matrix[row].append(0)

    # iterating rows of matrix 1
    for i in range(len(matrix1)):
        # iterating cols of matrix 2
        for j in range(len(matrix2[0])):
            # iterating rows of matrix 2
            for k in range(len(matrix2)):
                new_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return new_matrix

# x = [[12,7],
#      [4,5],
#      [7,8]]
#
# y = [[5,8,1,2],
#      [6,7,3,0],
#      [4,5,9,1]]
#
# t = matrix_multi(x,y)
# print(t)


# Subtract the second matrix from the first one
def subtraction(matrix1, matrix2):
    matrix2 = scalar_multi(matrix2, -1)

    new_matrix = addition(matrix1, matrix2)
    return new_matrix

# e = subtraction(a, b)
# print(e)

# finding the inverse of a 2x2 matrix
def inverse_2x2(matrix):
    if np.shape(matrix) != (2,2):
        return None

    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    matrix = [[d, -b], [-c, a]]
    determinant = 1 / ((a*d) - (b*c))

    new_matrix = scalar_multi(matrix, determinant)

    return new_matrix

f = [[3, 4], [1, 2], [5,6]]
# print(inverse_2x2(f))

def matrix_trans(matrix):
    # creating a new matrix and fill it with 0's
    new_matrix = []
    for row in range(len(matrix[0])):
        new_matrix.append([])
        for col in range(len(matrix)):
            new_matrix[row].append(0)

    # doing the transpose part (row to columns and vice versa)
    for i in range(len(new_matrix)):
        for k in range(len(new_matrix[0])):
            new_matrix[i][k] += matrix[k][i]

    return new_matrix




print((matrix_trans(a)))

