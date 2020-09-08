def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return (my_list)
    reeses_list = my_list
    reeses_list = list(reeses_list)
    reeses_list[idx] = element
    return (reeses_list)
