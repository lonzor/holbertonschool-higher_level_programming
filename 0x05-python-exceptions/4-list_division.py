#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list3 = []

    for i in range(list_length):
        divide = 0
        try:
            divide = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            list3.append(divide)
    return list3
