from bitarray import bitarray
from cityhash import CityHash32
from spooky import hash32
import statistics
import jhashcode
import mmh3
import math


def count_trailing_zeros(s):
    s = str(s)
    rev = s[::-1]
    count = 0
    for i in rev:
        if i == '0':
            count += 1
        else:
            break
    return count


file_names = ['quotes_2008-08.txt',
              'quotes_2008-09.txt',
              'quotes_2008-10.txt',
              'quotes_2008-11.txt',
              'quotes_2008-12.txt',
              'quotes_2009-01.txt',
              'quotes_2009-02.txt',
              'quotes_2009-03.txt',
              'quotes_2009-04.txt']

hash_function_1_tail_length = []
hash_function_2_tail_length = []
hash_function_3_tail_length = []
hash_function_4_tail_length = []

for i in file_names:
    fp = open(i, 'r')
    for line in fp:
        temp = line.split('\t')
        if temp[0] is 'Q':
            # hashing
            hash_value_1 = abs(CityHash32(temp[1]))
            hash_value_2 = abs(hash32(temp[1]))
            hash_value_3 = abs(jhashcode.hashcode(temp[1]))
            hash_value_4 = abs(mmh3.hash(temp[1]))

            # binray rep
            binary_1 = format(hash_value_1, '032b')  # represent in 32 bits
            binary_2 = format(hash_value_2, '032b')  # represent in 32 bits
            binary_3 = format(hash_value_3, '032b')  # represent in 32 bits
            binary_4 = format(hash_value_4, '032b')  # represent in 32 bits

            # trailing zeros
            hash_function_1_tail_length.append(count_trailing_zeros(binary_1))
            hash_function_2_tail_length.append(count_trailing_zeros(binary_2))
            hash_function_3_tail_length.append(count_trailing_zeros(binary_3))
            hash_function_4_tail_length.append(count_trailing_zeros(binary_4))
    fp.close()

avg_hash12 = (2 ** (max(hash_function_1_tail_length)) + 2 ** (max(hash_function_2_tail_length))) / float(2)
avg_hash34 = (2 ** (max(hash_function_3_tail_length)) + 2 ** (max(hash_function_4_tail_length))) / float(2)

print(math.ceil(statistics.median([avg_hash12, avg_hash34])))
