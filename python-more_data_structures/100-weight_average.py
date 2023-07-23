#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        mul = 0
        suma = 0
        for i in my_list:
            mul += i[0] * i[1]
        for i in my_list:
            suma += i[1]
        return mul/suma
