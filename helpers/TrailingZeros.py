def trailing_zeroes(s):
    if s == 0:
        return 32
    count = 0
    while (s >> count) & 1 == 0:
        count += 1
    return count