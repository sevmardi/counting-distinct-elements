import numpy as np

def count_tailing_zeros(s):
	s = str(s)
	rev = s[::-1]
	count = 0
	for i in rev:
		if i is '0':
			count+=1
		else:
			break
	return count


def mmds_fm(values, k):
	num_buckets = 2 ** k
	parts = 10
	bucket_len = int(np.ceil(len(values) / parts))
	bucket =  0
	for i in np.arange(len(values) - 1):
		s = values[i]
		r = count_tailing_zeros(s)

		if i % bucket_len == 0:
			bucket+=1

	calculate_mean = np.array([2 ** np.mean(r[:,1] for i in np.arange(bucket_len))])

	return np.mean(calculate_mean)
