import numpy as np
import random
import matplotlib.pyplot as plt
import helpers.TrailingZeros as trailing_zeroes


random.seed(12)


def first_zero(array):
    for i in range(len(array)):
        if array[i] == 0:
            return i


def probabilistic_counting(values, m):
    count = [0] * m
    bitmap = np.zeros((m, 32))

    for value in values:
        k = value
        # k = hash(value)
        num = random.randint(0, m - 1)
        bitmap[num][trailing_zeroes.trailing_zeroes(k)] = 1
    for i in range(0, m):
        count[i] = first_zero(bitmap[i])
    # Below is causing to run somehow slower
    # for i in range(len(bitmap)):
    #     if bitmap.any():
    #         for j in range(0, m):
    #             # count[j] = first_zero(bitmap[j])
    #             count[j] = bitmap[i]
    # print(count)
    return 2 ** (np.mean(count)) * (m / 0.77351)


if __name__ == '__main__':
    errors = [0] * 120
    m = [0] * 120

    for i in range(len(errors)):
        m[i] = 100 + 5 * i
        avg_error = [0] * 5
        for r in range(len(avg_error)):
            avg_error[r] = np.abs(100000 - probabilistic_counting([random.randint(0, 2 ** 32) for i in range(100000)], m[i])) / 100000
            # avg_error[r] = np.abs(100000 - probabilistic_counting([np.random.randint(0,2,100000,37)], m[i])) / 100000
        errors[i] = np.mean(avg_error)
    print(errors)
    print(m)
    plt.plot(m, errors)
    plt.ylabel("Error rate")
    plt.xlabel('m')
    plt.show()
