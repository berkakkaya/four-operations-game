from random import randint, choice


def generate_nums() -> tuple[int, int, int, int, int, int]:
    """Generates a number list.

    Returns
    -------
    tuple[int, int, int, int, int, int]
        The number list
    """

    # Create a empty number list
    nums = list()

    # Generate 5 single digit number
    while len(nums) != 5:
        generated = randint(0, 9)

        if not generated in nums:
            nums.append(generated)
    
    # Generate a two digit number and add it to the list
    nums.append(choice([10, 20, 30, 40, 50, 60, 70, 80, 90]))
    
    return tuple(nums)


def generate_target_number(nums: tuple) -> int:
    """Generate a target number, based on the number list

    Parameters
    ----------
    nums : tuple
        The number list

    Returns
    -------
    int
        The target number
    """

    # Sort the list in descending order
    nums = sorted(nums, reverse=True)
    max_limit = 1
    
    # Pick the biggest 4 numbers and multiply them to get the max limit
    for num in nums[:4]:
        max_limit = max_limit * num
    
    # Regularize the max limit if it's out of range
    if max_limit < 100:
        max_limit = max_limit * 2
    
    if max_limit >= 1000:
        max_limit = 999
    
    return randint(100, max_limit)


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
