#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    tem_list = list(my_list)
    tem_list[idx] = element
    return tem_list
