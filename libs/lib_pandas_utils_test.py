from lib_pandas_utils import is_empty_value
import pandas as pd
import numpy as np
import datetime as dt


def test_is_empty_value():
    # Test cases dictionary: key = tested input, value = correct result
    test_cases = {'abcd': False,        # case: has common chars
                  'abcd \n ': False,    # case: has common chars + invisible chars
                  '': True,             # case: is empty string
                  '   ': True,          # case: contains only spaces
                  '\t': True,           # case: contains tab
                  ' \t ': True,         # case: contains tab + spaces
                  '\n': True,           # case: contains newline
                  ' \n \t ': True,      # case: contains newline + tab + spaces
                  None: True,           # case: common null value
                  np.nan: True,         # case: common null value
                  pd.NaT: True,         # case: common null value
                  dt.date(2019, 12, 31): False  # case: date object
                  }

    # Iterate over all test-cases
    for param, expected_result in test_cases.items():
        assert is_empty_value(param) == expected_result
