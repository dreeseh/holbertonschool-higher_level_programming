#!/usr/bin/python3
def remove_char_at(str, n):
    if n < len(str) and n >= 0:
        removed = str.replace(str[n], "")
        return(removed)
    else:
        return(str)
