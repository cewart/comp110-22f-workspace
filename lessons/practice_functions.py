"""Hand-written code from prac quix 10/17/22."""


def odd_and_even(input_list: list[int]) -> list[int]:
    """given a list, should return a list with odd elements and even index"""
    new_list: list[int] = []
    i: int = 0
    while i < len(input_list):
        if i % 2 == 0 and input_list[i] % 2 != 0:
            new_list.append(input_list[i])
        i += 1
    print(new_list)
    return new_list

input_str: str = "comp110"
new_str: str = ""
vowels: list[str] = ["a", "e", "i", "o", "u"]
i: int = 0
while i < len(input_str):
    if input_str[i] in vowels and i % 3 != 0:
        new_str += input_str[i]
    if i % 3 == 0 and input_str[i] not in vowels:
        new_str += input_str[i]
    i += 1
print(new_str)