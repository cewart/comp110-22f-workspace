"""Creating utility list functions 9/17/22."""

__author__: "730551195"

def all(number_list: list[int], number: (int)) -> bool:
    """This function runs through a list and tests if each index is equal to an int and it returns True or False."""
    i: int = 0
    list_length: int = len(number_list)
    while i < list_length:
        if number_list[i] == number:
            i += 1
        else:
            all = False
            print(all)
            return
    all = True
    print(all)
    return


def max(list_ints: list[int]) -> int:
    if len(list_ints) == 0:
        raise ValueError("max() arg is an empty List")
    max_value = list_ints[0]
    for largest in list_ints:
        if largest > max_value:
            return largest

def is_equal(list1: list[int], list2: list[int]) -> bool:
    if list1 == list2:
        is_equal = True
        return is_equal
    else:
        is_equal = False
        return is_equal