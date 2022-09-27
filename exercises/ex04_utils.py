"""Creating utility list functions 9/17/22."""


__author__ = "730551195"


def all(number_list: list[int], number: (int)) -> bool:
    """This function runs through a list and tests if each index is equal to an int and it returns True or False."""
    if len(number_list) == 0:
        return False
    i: int = 0
    list_length: int = len(number_list)
    while i < list_length:
        if number_list[i] == number:
            i += 1
        else:
            return False
    return True


def max(list_ints: list[int]) -> int:
    """This function uses a while loop to iterate through each index of a list and return the value of the index with the greatest value."""
    if len(list_ints) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    largest_value: int = list_ints[0]
    while i < len(list_ints):
        if list_ints[i] > largest_value:
            largest_value = list_ints[i]
            i += 1
        else:
            i += 1
    return largest_value


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Given two unique lists, if the first list contains the same lengths and values as the other, is_equal will return true."""
    if list1 == list2:
        is_equal = True
        return is_equal
    else:
        is_equal = False
        return is_equal