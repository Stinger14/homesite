def compute_join_point(s1: int, s2: int) -> int:
    """
    :type s1: int
    :type s2: int
    :rtype: int
    """
    
    # Generate sequences and check for join point
    while True:
        tmp1 = sum(int(num) for num in str(s1))
        tmp2 = sum(int(num) for num in str(s2))
        if s1 == s2:
            return s1
        s1 += tmp1
        s2 += tmp2

print(compute_join_point(471, 480))