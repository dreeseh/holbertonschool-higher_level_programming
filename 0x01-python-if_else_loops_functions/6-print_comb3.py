#!/usr/bin/python3
for num_01 in range(0, 10):
    for num_02 in range(num_01 + 1, 10):
        if num_01 == 8 and num_02 == 9:
            print("{}{}".format(num_01, num_02))
        else:
            print("{}{}".format(num_01, num_02), end=", ")
