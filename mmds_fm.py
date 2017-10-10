# Decimal number to binary number
def dec2bin(dec):
    return bin(dec)[2:]


# Count the number of trailing zeros
def trailing_zeros(b):
    count = 0
    for i in range(len(b))[::-1]:
        if b[i] == '0':
            count += 1
        else:
            return count
    return count

    # Given R = max r(a), estimate number of distinct elements


def distinct_els(r):
    return 2 ** r


if __name__ == '__main__':
    print(trailing_zeros(dec2bin(12)))
    # print(trailing_zeros(dec2bin(12)))
    # print(trailing_zeros(dec2bin(4)))
    # print(trailing_zeros(dec2bin(16)))
    # print(trailing_zeros(dec2bin(1)))
