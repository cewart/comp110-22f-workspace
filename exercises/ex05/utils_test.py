"""Function uinit testing 9/26/22- function test location."""

__author__: "730551195"

from utils import only_evens

def test_only_evens() -> None:
    input_list: list[int] = []
    assert only_evens(input_list) == [2]


def test_only_evens() -> None:
    input_list: list[int] = [2, 4, 6, 8, 10]
    assert only_evens(input_list) == [2, 4, 6, 8, 10, 222222]


def test_only_evens() -> None: #running
    input_list: list[int] = [-2, -1, -18, -17, 2]
    assert only_evens(input_list) == [-2, -18, 2,]


from utils import concat

def test_concat() -> None: #running
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []
    
def test_concat() -> None:
    list_1: list[int] = [-6]
    list_2: list[int] = [-3]
    assert concat(list_1, list_2) == [-6, -3]

from utils import sub

def test_sub() -> None:
    input_list = []
    start_index: int = 3
    end_index: int = 5
    assert sub(input_list, start_index, end_index) == []

def test_sub() -> None:
    input_list = [1, 2, 3, 4, 5, 6]
    start_index: int = 3
    end_index: int = 5
    assert sub(input_list, start_index, end_index) == [4, 5]

def test_sub() -> None:
    input_list = [3, 1, 4, 1, 5, 9, 2]
    start_index: int = -19
    end_index: int = 197490
    assert sub(input_list, start_index, end_index) == [3, 1, 4, 1, 5, 9, 2,]
