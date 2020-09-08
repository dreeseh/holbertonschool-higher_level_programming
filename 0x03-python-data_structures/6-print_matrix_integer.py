#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        print(i)
        for j in i:
            print("{:d}".format(j), end=" ")
        print("")
