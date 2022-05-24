#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    c = 0

    try:
        for i in my_list:
            if c < x:
            print ('{}'.format(my_list[element]) , end= '')
            c += 1

        print()
    except TypeError:
        pass
    finally:
        return element
