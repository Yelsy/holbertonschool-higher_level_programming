#!/usr/bin/python3
def max_integer(my_list=[]):
    count = len(my_list)
    if count == 0:
        return None
    max_list = my_list[0]
    for i in my_list:
        if i > max_list:
            max_list = i
    return max_list
