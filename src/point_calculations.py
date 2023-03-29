def calculate_base_point(target: int, calculated: int) -> int:
    """Calculates the base point.

    For more information, you can look up to project's
    README.md file.

    Parameters
    ----------
    target : int
        The target number with 3 digits
    calculated : int
        The number that has been calculated by player

    Returns
    -------
    int
        The base point
    """

    # Do a int conversion, in case of the calculated number's type is float
    calculated = int(calculated)

    return max(0, target - calculated)


def calculate_multiplier(step_target: int, step_calculated: int) -> int:
    """Calculates the multiplier.

    Multiplier system awards the player if the target number has been
    calculated more quickier. For more information, you can look up
    to project's README.md file.

    Parameters
    ----------
    step_target : int
        Number of steps that has been used for generating the target number
    step_calculated : int
        Number of steps that has been used by player for calculating
        the target number

    Returns
    -------
    int
        The multiplier
    """

    return max(0, step_target - step_calculated + 3)


def calculate_final_point(base_point: int, multiplier: int) -> int:
    """Calculates the final point.

    For more information, you can look up to project's README.md file.

    Parameters
    ----------
    base_point : int
        The base point
    multiplier : int
        The multiplier

    Returns
    -------
    int
        The final point
    """

    return base_point + 2 * multiplier
