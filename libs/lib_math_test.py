from lib_math import round_to_nearest, round_down_to_nearest, round_up_to_nearest


def test_round_to_nearest():
    test_cases = {(62.5, 1): 63,
                  (62.5, 2): 62,
                  (62.5, 5): 65,
                  (62.5, 10): 60,
                  (62.5, 100): 100,
                  (62.53, 0.1): 62.5,
                  (62.55, 0.1): 62.6,
                  (62.56, 0.1): 62.6
                  }

    # Iterate over all test-cases
    for params, expected_result in test_cases.items():
        num, divisor = params
        assert round_to_nearest(num, divisor) == expected_result


def test_round_down_to_nearest():
    test_cases = {(62.5, 1): 62,
                  (62.5, 2): 62,
                  (62.5, 5): 60,
                  (62.5, 10): 60,
                  (62.5, 100): 0,
                  (62.53, 0.1): 62.5,
                  (62.55, 0.1): 62.5,
                  (62.56, 0.1): 62.5
                  }

    # Iterate over all test-cases
    for params, expected_result in test_cases.items():
        num, divisor = params
        assert round_down_to_nearest(num, divisor) == expected_result


def test_round_up_to_nearest():
    test_cases = {(62.5, 1): 63,
                  (62.5, 2): 64,
                  (62.5, 5): 65,
                  (62.5, 10): 70,
                  (62.5, 100): 100,
                  (62.53, 0.1): 62.6,
                  (62.55, 0.1): 62.6,
                  (62.56, 0.1): 62.6
                  }

    # Iterate over all test-cases
    for params, expected_result in test_cases.items():
        num, divisor = params
        assert round_up_to_nearest(num, divisor) == expected_result
