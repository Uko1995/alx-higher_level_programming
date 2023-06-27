#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    final_list = []

    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            result = 0
            print("{}".format("division by 0"))
        except (ValueError, TypeError):
            result = 0
            print("{}".format("wrong type"))
        except IndexError:
            result = 0
            print("{}".format("out of range"))
        finally:
            final_list.append(result)
    return final_list
