import random

def shuffle(values):
    """
    Shuffles the elements in the given list randomly.

    Args:
        values (list): The list of values to be shuffled.

    Returns:
        None. The function shuffles the list in-place.

    Example:
        >>> values = [1, 2, 3, 4, 5]
        >>> shuffle(values)
        >>> print(values)
        [4, 2, 1, 5, 3]
    """
    for i in range(len(values)):
        swapIndex = random.randint(0, len(values) - 1)
        values[i], values[swapIndex] = values[swapIndex], values[i]
