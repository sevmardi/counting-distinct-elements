


# Count the number of trailing zeros
def trailing_zeros(b):
    count = 0
    for i in range(len(b))[::-1]:
        if b[i] == '0':
            count += 1
        else:
            return count
    return count

def mmds_fm(a, m):
    """
    a: Stream of eleemnts
    m: Distant eles 
    """
    



if __name__ == '__main__':
