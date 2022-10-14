"""Dictionary Functions and Unit Tests - Function Skeleton section 10/9/22."""

__author__ = "730551195"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """This inverts the keys and values, so keys of input become the values of output and vice versa."""
    new_dict: dict[str, str] = {}
    for value in input_dict:
        if input_dict[value] in new_dict:
            raise KeyError("Cannot invert because one or more input values match, which are not allowed to match when they become the key value.")
        new_dict[input_dict[value]] = value
    return new_dict


def favorite_color(input_colors: dict[str, str]) -> str:
    """This one returns the most common favorite color, and returns the color of first appearance if there is a tie."""
    count_dict: dict[str, int] = {}
    common_color: str = ""
    greatest_value: int = 0
    for value in input_colors:
        if input_colors[value] in count_dict:
            count_dict[input_colors[value]] += 1
        else: 
            count_dict[input_colors[value]] = 1
    for largest in count_dict:
        if count_dict[largest] > greatest_value:
            greatest_value = count_dict[largest]
            common_color = largest
    return common_color
        
    
def count(input_list: list[str]) -> dict[str, int]:
    """Creates a dictionary where the key is a value from the list and each value is the count of the times of appearance."""
    new_dict: dict[str, int] = {}
    for value in input_list:
        if value in new_dict:
            new_dict[value] += 1
        else:
            new_dict[value] = 1
    return new_dict