import helpers.TrailingZeros as trailing_zeroes
import matplotlib.pyplot as plt
import numpy as np
import random


def loglog_counting(values, k):
    """
    Estimate numbre of distinct elements in the input. 
    :param values: Hashed elements
    :param k: 
    :return:
    """
    num_buckets = 2 ** k
    max_zeros = [0] * num_buckets

    for value in values:
        # h = hash(value)
        h = value
        bucket = h & (num_buckets - 1)
        bucket_hash = h >> k
        max_zeros[bucket] = max(max_zeros[bucket], trailing_zeroes.trailing_zeroes(bucket_hash))

    return 2 ** (float(sum(max_zeros)) / num_buckets) * num_buckets * 0.79402  # 2^x * number of buckets where x is the mean of all buckets

if __name__ == '__main__':
    errors = [0] * 15
    m = [0] * 15
    
    for i in range(len(errors)):
        m[i] = 3 + i
        avg_error = [0] * 20
        true_count = 500000
        for j in range(len(avg_error)):
            avg_error[j] = np.abs(true_count - loglog_counting([random.randint(0, 2 ** 32) for i in range(true_count)], m[i])) / true_count
            # avg_error[r] = np.abs(100000 - loglog_counting([random.random() for j in range(100000)], m[i]))/(100000)
            # avg_error[r] = np.abs(100000 - loglog_counting([np.random.randint(0, 2 ** 32) for i in range(100000)], m[i])) / 100000
        errors[i] = np.mean(avg_error)
    print(errors)
    print(m)
    plt.plot(m, errors)
    plt.ylabel("Error rate")
    plt.xlabel("m")
    plt.show()

