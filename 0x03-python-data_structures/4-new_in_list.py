def new_in_list(my_list, idx, element):
    reeses_list = []
    reeses_list = list(my_list)
    if idx < 0 or idx >= len(reeses_list):
        return (reeses_list)
    reeses_list[idx] = element
    return (reeses_list)
