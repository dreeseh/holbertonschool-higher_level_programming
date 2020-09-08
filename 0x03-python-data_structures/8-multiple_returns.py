#!/usr/bin/python3
def multiple_returns(sentence):
    list = [0, 1]
    length = len(sentence)
    if length == 0:
        list[0] = len(sentence)
        list[1] = None
    else:
        list[0] = len(sentence)
        list[1] = sentence[0]
    ret_val = tuple(list)
    return (ret_val)
