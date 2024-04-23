from math import factorial

# bracket combinations
def bracket_combinations(num):
    """
    Calculates the number of valid bracket combinations given a number of pairs.

    Args:
        num (int): The number of pairs of brackets.

    Returns:
        int: The number of valid bracket combinations.

    Raises:
        ValueError: If the input number is negative.

    Examples:
        >>> bracket_combinations(3)
        5
        >>> bracket_combinations(4)
        14
    """
    if num < 0:
        raise ValueError("Number of pairs cannot be negative.")

    return int(factorial(2 * num)/(factorial(num + 1) * (factorial(num))))

print(bracket_combinations(input()))