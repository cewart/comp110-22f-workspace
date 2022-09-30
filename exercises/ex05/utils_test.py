"""Function uinit testing 9/26/22- function test location."""

__author__ = "730551195"


from utils import only_evens, concat, sub


def test_only_evens() -> None:
    """Test for empty list."""
    input_list: list[int] = []
    assert only_evens(input_list) == []


def test_only_evens2() -> None:
    """Test for more normal use."""
    input_list: list[int] = [2, 4, 6, 8, 10]
    assert only_evens(input_list) == [2, 4, 6, 8, 10]


def test_only_evens3() -> None:
    """Test for normal use."""
    input_list: list[int] = [-2, -1, -18, -17, 2]
    assert only_evens(input_list) == [-2, -18, 2]


def test_concat() -> None:
    """Test for empty list."""
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []
    

def test_concat2() -> None:
    """Test for negatives."""
    list_1: list[int] = [-6]
    list_2: list[int] = [-3]
    assert concat(list_1, list_2) == [-6, -3]


def test_concat3() -> None:
    """Test for regular use."""
    list_1: list[int] = [1, 2, 3, 4]
    list_2: list[int] = [5, 6, 7, 8]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_sub() -> None:
    """Test for empty string."""
    input_list: list[int] = []
    start_index: int = 3
    end_index: int = 5
    assert sub(input_list, start_index, end_index) == []


def test_sub2() -> None:
    """Test for normal input."""
    input_list: list[int] = [1, 2, 3, 4, 5, 6]
    start_index: int = 3
    end_index: int = 5
    assert sub(input_list, start_index, end_index) == [4, 5]


def test_sub3() -> None:
    """Test for bounds."""
    input_list: list[int] = [3, 1, 4, 1, 5, 9, 2]
    start_index: int = -19
    end_index: int = 197490
    assert sub(input_list, start_index, end_index) == [3, 1, 4, 1, 5, 9, 2]