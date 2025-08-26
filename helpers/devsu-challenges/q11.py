def get_position_at(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        steps = [0, 1]  # Initial steps for stage 0 and 1
        for i in range(2, n + 1):
            next_step = steps[i - 1] - steps[i - 2]
            steps.append(next_step)
        return steps[-1]

print(get_position_at(3))
