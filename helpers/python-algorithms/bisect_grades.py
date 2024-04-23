import bisect

import bisect

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    """
    Assigns a grade based on the given score.

    Args:
        score (int): The score to be graded.
        breakpoints (list, optional): List of breakpoints for grade boundaries. Defaults to [60, 70, 80, 90].
        grades (str, optional): String of grades corresponding to each breakpoint. Defaults to 'FDCBA'.

    Returns:
        str: The grade corresponding to the given score.
    """
    i = bisect.bisect(breakpoints, score)
    return grades[i]

# Example input
print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])
