"""EX06 - Dictonary Functions."""
__author__ = "730460523"


def invert(orig_dic: dict[str, str]) -> dict[str, str]:
    """Switches the keys and values of a dictionary."""
    new_dic: dict[str, str] = dict()
    # Loops through every key in the given dictionary
    for key in orig_dic:
        # Decides if the value of the key is in the new dictionary being created to raise a KeyError
        if orig_dic[key] in new_dic:
            raise KeyError("There are two of the same values in your dictionary. Cannot generate unique keys.")
        # Sets the new dictionary's key to the value of the origional dictionary and the value to the key
        else:
            new_dic[orig_dic[key]] = key
    return new_dic


def count(lister: list[str]) -> dict[str, int]:
    """Creates a dictionary with the values of a list as the keys and the frequency of these values as the values."""
    counter_dictionary: dict[str, int] = dict()
    # Loops through every item in the list 
    for item in lister:
        # If the item is in the dictionary already, increase its value by 1
        if item in counter_dictionary:
            counter_dictionary[item] += 1
        # If not, add a new key with a value of 1
        else:
            counter_dictionary[item] = 1
    return counter_dictionary


def favorite_color(color_input: dict[str, str]) -> str:
    """Determines the most frequent str value in from a dictionary."""
    # Creates an empty list and empty dictionary.
    color_list: list[str] = list()
    color_dictionary: dict[str, int] = dict()
    # Generates lists of colors from the color_input dictionary
    for color in color_input:
        color_list.append(color_input[color])
    # Sets color_dictionary equal to a dictionary with keys as the colors in the list and values of said colors frequency within the list
    color_dictionary = count(color_list)
    # Checks every key in the color_dictionary to see if it occurs more than once
    max: int = 1
    fav_color: str = ""
    for color in color_dictionary:
        if color_dictionary[color] > max:
            fav_color = color
            max = color_dictionary[color]  
    return fav_color