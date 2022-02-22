"""EX05 - 'list' Utility Functions."""
__author__ = "730460523"


def only_evens(gen_list: list[int]) -> list[int]:
    """Returns only the even values in the list."""
    even_list: list[int] = list()
    for item in gen_list:
        if item % 2 == 0:
            even_list.append(item)
    return(even_list)


def sub(starting_list: list[int], min: int, max: int) -> list[int]:
    """Returns only the given subset of values from the list."""
    i: int = 0
    list_len: int = len(starting_list)
    sub_list: list[int] = list()
    while i < list_len:
        if i >= min and i < max:
            sub_list.append(starting_list[i])
        i += 1
    return sub_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Returns the concatenation of the first and second list."""
    result_list: list[int] = list()
    for item in list_one:
        result_list.append(item)
    for element in list_two:
        result_list.append(element)
    return result_list