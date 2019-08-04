def round_to_nearest(num, divisor, round_up_on_tie=True):
    """
    Rounds number $num to nearest multiply of $divisor.

    :param num: number we need to round
    :param divisor: round to nearest multiply of this number
    :param round_up_on_tie: True / False. Applies only if there is tie  = same distance for up/down roundng)
    :return: rounded number

    :Example:

    >>> round_to_nearest(62.4, 5)
    60
    >>> round_to_nearest(62.5, 5, round_up_on_tie=True)
    65
    >>> round_to_nearest(62.5, 5, round_up_on_tie=False)
    60
    """
    # Speedup
    if num % divisor == 0:
        return num

    low_value = num // divisor * divisor
    high_value = ((num // divisor) + 1) * divisor

    low_distance = (num - low_value)
    high_distance = (high_value - num)

    if abs(low_distance - high_distance) < 1e-10:
        return high_value if round_up_on_tie else low_value
    elif low_distance < high_distance:
        return low_value
    else:
        return high_value


def round_down_to_nearest(num, divisor):
    """
    Rounds-down number $num to nearest multiply of $divisor.

    :param num: number we need to round
    :param divisor: round to nearest multiply of this number
    :return: rounded number

    :Example:

    >>> round_down_to_nearest(62.5, 5)
    60
    """
    return num // divisor * divisor


def round_up_to_nearest(num, divisor):
    """
    Rounds-up number $num to nearest multiply of $divisor.

    :param num: number we need to round
    :param divisor: round to nearest multiply of this number
    :return: rounded number

    :Example:

    >>> round_down_to_nearest(62.5, 5)
    65
    """
    return ((num // divisor) + 1) * divisor
