"""Dictionary related utility functions."""

__author__ = "730551195"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read rows of CSV into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table into a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(input_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """This function will create a column-based table with a specified number of roes of data for each column."""
    table: dict[str, list[str]] = {}
    for column in input_table:
        store_N_values: list[str] = []
        for item in input_table[column]:
            if rows > len(store_N_values):
                store_N_values.append(item)
        table[column] = store_N_values
    return table
        

def select(table: dict[str, list[str]], name: list[str]) -> dict[str, list[str]]:
    """This function will create a column-based table with a subset of origional, relevant columns."""
    column_table: dict[str, list[str]] = {}
    for column in name:
        column_table[column] = table[column]
    return column_table


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Will return a new column-based table that includes data from two tables."""
    combined_table: dict[str, list[str]] = {}
    for column in table1:
        combined_table[column] = table1[column]
    for column in table2:
        if column in combined_table:
            combined_table[column] += table2[column]
        else:
            combined_table[column] = table2[column]
    return combined_table


def count(to_count: list[str]) -> dict[str, int]:
    """Function that takes a list and returns a dictionary that counts the number of times a value appeared."""
    frequencies: dict[str, int] = {}
    for item in to_count:
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    return frequencies