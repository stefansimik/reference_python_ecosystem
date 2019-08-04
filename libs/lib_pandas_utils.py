import pandas as pd


def is_empty_value(input):
    """Checks if input is logically empty.

    * None
    * NaN, NaT = pandas / numpy missing values
    * empty / invisible strings
      * '' = empty string
      * ' \n  ' = string, that containing only invisible characters (spaces, tabs, newline, ...)

    :return: True if input-value is empty, otherwise False
    :rtype: bool

    >>> input = '    '
    >>> is_empty_value(input)
    True
    """
    return pd.isnull(input) or (type(input) == str and len(input.strip()) == 0)
