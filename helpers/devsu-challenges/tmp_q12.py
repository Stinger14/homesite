def foo(s1, s2):
    while True:
        tmp1 = sum(int(num) for num in str(s1))
        tmp2 = sum(int(num) for num in str(s2))
        if s1 == s2:
            return s1
        s1 += tmp1
        s2 += tmp2

print(foo(471, 480))