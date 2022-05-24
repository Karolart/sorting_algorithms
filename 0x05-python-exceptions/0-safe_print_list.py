#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    element = 0

    if element < x:
    try:
        for i in my_list:
            print ('{}'.format(my_list[element]) , end= '')
            element = element + 1


        print(none)
    except TypeError:
        pass
    finally:
        return element
