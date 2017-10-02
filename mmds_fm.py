
# Decimal number to binary number
def dec2bin(dec):
    return bin(dec)[2:]

# Count the number of trailing zeros
def counttrailingzero(b):
    cnt = 0
    for i in range(len(b))[::-1]:
        if b[i] == '0':
            cnt += 1
        else:
            return cnt
    return cnt


 # Given R = max r(a), estimate number of distinct elements
def distinct_els(r):
    return 2 ** r


if __name__ == '__main__':
    # print(counttrailingzero(dec2bin(10)))
    # print(counttrailingzero(dec2bin(12)))
    # print(counttrailingzero(dec2bin(4)))
    print(counttrailingzero(dec2bin(16)))
    # print(counttrailingzero(dec2bin(1)))
