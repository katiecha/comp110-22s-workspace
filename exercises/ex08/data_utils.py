"""Dictionary related utility functions."""

__author__ = "730460523"

from csv import DictReader


# Define your functions below
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reads an entire CSV of data into a list of rows, each row represented as dict[str, str]."""
    # Establishes empty list of dictionaries to store CSV data.
    result: list[dict[str, str]] = []
    # Opens a handle to the data file.
    file_handle = open(filename, "r", encoding="utf8")
    # Prepares to read that file as a CSV rather than just strings.
    csv_reader = DictReader(file_handle)
    # Reads each row of the CSV line-by-line.
    for row in csv_reader:
        result.append(row)
    # Closes the file when we're done to free the resources.
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produces a list[str] of all values in a single column whose name is the second parameter."""
    # Establishes empty list to store column values.
    result: list[str] = []
    # Loops through the rows of 'table'.
    for row in table:
        # Sets 'item' equal to the 'column' key of rows.
        item: str = row[column]
        # Appends item to result.
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a table represented as a list of rows into one represented as a dictionary of columns."""
    # Establishes empty dictionary.
    result: dict[str, list[str]] = {}
    # Sets 'first_row' equal to a dictionary with the values of row index 0 of the 'row_table' list.
    first_row: dict[str, str] = row_table[0]
    # Loops through every column name of first_row.
    for column in first_row:
        # Sets the key 'column' to a list of its values using column_values function.
        result[column] = column_values(row_table, column)
    return result


def head(col_table: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Produce a column-based table with only the first N rows of data."""
    # Establishes empty dictionary
    result: dict[str, list[str]] = {}
    # Loops through every column in the first row of 'col_table'.
    for key in col_table:
        # Checks if the N value is greater than the length of the dictionary list.
        if num_rows >= len(col_table[key]):
            # Sets the key of the result dictionary to the entire origional dictionary list if true.
            result[key] = col_table[key]
        else:  
            result_list: list[str] = []
            i: int = 0
            # Loops from 0 to N or num_rows.
            while i < num_rows:
                # Appends the dictionary key's ith list value.
                result_list.append(col_table[key][i])
                i += 1
            # Sets the key of the result to list created above.
            result[key] = result_list
    return result


def select(col_table: dict[str, list[str]], name_list: list[str]) -> dict[str, list[str]]:
    """Establishes a column-based table with specific columns specified by a list parameter."""
    # Establishes an empty dictionary.
    result: dict[str, list[str]] = {}
    # Loops through every value in the 'name_list'
    for name in name_list:
        # Sets the key of the resulting dictionary to the name and the value to the value associated with the key from the origional dictionary.
        result[name] = col_table[name]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two column-based tables into one."""
    result: dict[str, list[str]] = {}
    # Loops through the keys of the first table.
    for col in table_1:
        result[col] = table_1[col]
    # Loops through the keys of the second table.
    for col in table_2:
        # Checks to see if the key is already in the dictionary.
        if col in result:
            result[col] += table_2[col]
        else: 
            result[col] = table_2[col]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Counts the frequencies of a specified list of values."""
    result: dict[str, int] = {}
    # Loops through every item in the list of specified values.
    for item in values:
        # If the item is in the resulting dictionary, increments it by one.
        if item in result:
            result[item] += 1
        # Adds the key to the dictionary with a value of one if not.
        else:
            result[item] = 1
    return result


def equal_to_exp(prior_exp_col: list[str], exp_level: str) -> list[bool]:
    """Creates a list of bools, True if the column name matches the given string, False if not,"""
    result: list[bool] = []
    for item in prior_exp_col:
        result.append(item == exp_level)
    return result


def masked(und_col: list[str], mask: list[bool]) -> list[int]:
    """Takes two lists of strings and bools and returns a single list of every string value where the correlating bool was True."""
    result: list[int] = []
    for i in range(len(mask)):
        if mask[i]:
            result.append(int(und_col[i]))
    return result


def combine(table: dict[str, list[str]]) -> dict[str, list[int]]:
    """Returns a dictionary with keys denoted by 'prior_exp levels' and list values with the correlating 'understanding levels'."""
    result: dict[str, list[int]] = {}
    for item in table["prior_exp"]:
        experiences: list[bool] = equal_to_exp(table["prior_exp"], item)
        result[item] = masked(table["understanding"], experiences)
    return result


def average(table: dict[str, list[int]], col: str) -> float:
    """Takes the average value of a list of ints for a certain string."""
    result: float = 0 
    for item in table[col]:
        result += item
    result /= len(table[col])
    return result