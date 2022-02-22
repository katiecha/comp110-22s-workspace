"""An example of a function that searches through a list."""

# Defines a function named contains/
# Two parameters
# 1. needle - the string we're searching for
# 2. haystack - the list we're searching through
# Algorithm:
#   For each itme in the haystack
#       Test if it is equal to the needle
#           If so, return True
# After testing all items, return False, because not found
# Returns true if needle in haystack, false otherwise


def main() -> None:
    print(contains("Kevin Bacon", ["Kanye West", "Pete Davidson"]))


# Contains function using for...in loop.
def contains(needle: str, haystack: list[str]) -> bool:
    # Checks every item in the list.
    for item in haystack:
        if item == needle:
            return True
    return False


# Allows program to run as a program in a module, can also import singular functions from it in the Globals frame
if __name__ == "__main__":
    main()
else:
    print(__name__)  # __name__ is the name of the module

# # Contains function using while loop.
# def contains2(needle: str, haystack: list[str]) -> bool:
#     i: int = 0
#     list_len: int = len(haystack)
#     while i < list_len:
#         if haystack[i] == needle:
#             return True
#         i += 1
#     return False
