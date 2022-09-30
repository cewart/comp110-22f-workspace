"""Exercise 5: function unit testing- function location 9/26/22."""

__author__ = "730551195"


def only_evens(input_list: list[int]) -> list[int]:
    """For a list of integers, this function will return a list of even integers from the origional list."""
    i: int = 0
    evens_from_input: list[int] = list()
    while i < len(input_list):
        if len(input_list) == 0:
            return []
        if input_list[i] % 2 == 0:
            evens_from_input.append(input_list[i])
        i += 1
    return evens_from_input


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Given two lists, this function will create a new list that is all elements of first list followed by all elements of the second one."""
    both_lists: list[int] = list()
    i: int = 0
    while i < len(list_1):
        both_lists.append(list_1[i])
        i += 1
    i = 0
    while i < len(list_2):
        both_lists.append(list_2[i])
        i += 1
    return both_lists


def sub(input_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Given a list, a start index, and an end index, this funtion will create a new list of ints between and including the start and end index."""
    bounded_list: list[int] = list()
    if start_index < 0:
        start_index = 0
    if end_index > len(input_list):
        end_index = len(input_list)
    if len(input_list) == 0 or start_index > len(input_list) or end_index <= 0:
        return bounded_list
    i: int = 0
    while i < start_index:
        i += 1
    while start_index <= i and end_index > i:
        bounded_list.append(input_list[i])
        i += 1
    return bounded_list