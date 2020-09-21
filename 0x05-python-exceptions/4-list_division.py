#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    reeses_list = []
    for i in range(list_length):

        try:
            answer = my_list_1[i] / my_list_2[i]

        except (TypeError, ValueError):
            print("wrong type")
            answer = 0

        except ZeroDivisionError:
            print("division by 0")
            answer = 0

        except IndexError:
            print("out of range")
            answer = 0

        finally:
            reeses_list.append(answer)

    return reeses_list
