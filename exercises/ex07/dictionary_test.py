"""Here is where the unit tests for my dictionary functions will live."""

__author__ = "730551195"

from dictionary import invert, favorite_color, count
import pytest


def test_invert1() -> None:
    """Test for an empty dictionary."""
    empty_dict: dict[str, str] = {}
    assert invert(empty_dict) == {}


def test_invert2() -> None:
    """Test for a dictionary with normal use cases."""
    regular_dict: dict[str, str] = {'a': 'y', 'b': 'x', 'c': 'w', 'd': 'z'}
    assert invert(regular_dict) == {'y': 'a', 'x': 'b', 'w': 'c', 'z': 'd'}


def test_invert3() -> None:
    """Test for a dictionary with repeated value in origional."""
    with pytest.raises(KeyError):
        my_dictionary = {'one': 'banana', 'two': 'banana', 'three': 'blueberry', 'four': 'strawberry'}
        invert(my_dictionary)

    
def test_favorite_color1() -> None:
    """Test the case if input_colors is an empty dictionary."""
    empty_dict: dict[str, str] = {}
    assert favorite_color(empty_dict) == ""


def test_favorite_color2() -> None:
    """Test for a regular use case."""
    empty_dict: dict[str, str] = {"Chris": "blue", "Jake": "green", "Kush": "green"}
    assert favorite_color(empty_dict) == "green"


def test_favorite_color3() -> None:
    """Test for a use case when two colors tie for most often."""
    empty_dict: dict[str, str] = {"Noora": "green", "Gryffin": "green", "Harrold": "blue", "Chris": "blue"}
    assert favorite_color(empty_dict) == "green"


def test_count1() -> None:
    """Test for a use case when the input list is empty."""
    empty_list: list[str] = []
    assert count(empty_list) == {}


def test_count2() -> None:
    """Test for a regular use case."""
    input_list: list[str] = ["blue", "red", "green", "blue", "blue", "green"]
    assert count(input_list) == {'blue': 3, 'red': 1, 'green': 2}


def test_count3() -> None:
    """Test for a use case with quirky lil words."""
    input_list: list[str] = ["supercalifragilisticexpialidocious", "neuropsychopharmacology", "deoxyribonucleic_acid", "neuropsychopharmacology", "hi"]
    assert count(input_list) == {'supercalifragilisticexpialidocious': 1, 'neuropsychopharmacology': 2, 'deoxyribonucleic_acid': 1, 'hi': 1}