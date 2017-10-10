import jhashcode
import mmh3
from cityhash import CityHash32
from spooky import hash32
import numpy as np
import random
import matplotlib.pyplot as plt
import hashlib

random.seed(17)


def trailing_zeroes(s):
    if s == 0:
        return 32
    count = 0
    while (s >> count) & 1 == 0:
        count += 1
    return count


def first_zero(array):
    for i in range(len(array)):
        if array[i] == 0:
            return i


def probabilistic_counting(n, m):
    count = [0] * m
    bitmap = np.zeros((m, 32))
    for value in n:
        # k = CityHash32(value)
        k = hash(value)
        num = random.randint(0, m - 1)
        bitmap[num][trailing_zeroes(k)] = 1
    for j in range(0, m):
        count[j] = first_zero(bitmap[j])
    # print(count)
    return 2 ** (np.mean(count)) * (m / 0.77351)


def estimate_cardinality(n, k):
    """
    Estimate numbre of distinct elements in the input. 
    :param n: Hashed elements
    :param k: 
    :return:
    """
    num_buckets = 2 ** k
    max_zeros = [0] * num_buckets

    for value in n:
        h = hash(value)
        bucket = h & (num_buckets - 1)
        bucket_hash = h >> k
        max_zeros[bucket] = max(max_zeros[bucket], trailing_zeroes(bucket_hash))
        
    return 2 ** (float(sum(max_zeros)) / num_buckets) * num_buckets * 0.79402  # 2^x * number of buckets where x is the mean of all buckets
    



if __name__ == '__main__':
    errors = [0] * 120
    m = [0] * 120

    for i in range(len(errors)):
        m[i] = 100 + 5 * i
        avg_error = [0] * 5
        for r in range(len(avg_error)):
            avg_error[r] = np.abs(
                500000 - probabilistic_counting([random.random() for j in range(500000)], m[i])) / 500000
        errors[i] = np.mean(avg_error)
    print(errors)
    plt.plot(m, errors)
    plt.ylabel("Error rate")
    plt.xlabel('m')
    plt.show()
