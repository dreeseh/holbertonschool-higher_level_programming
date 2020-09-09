#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    reeses_list = my_list.copy()
    for i in my_list:
        if i % 2 == 0:
            reeses_list[i] = True
        else:
            reeses_list[i] = False
    return reeses_list
