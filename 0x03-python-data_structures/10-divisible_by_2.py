#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    reeses_list = list(my_list)
    for i in my_list:
        if (i % 2 == 0):
            reeses_list[i] = True
        else:
            reeses_list[i] = False
    return reeses_list
