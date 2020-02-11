#!/usr/bin/env python3
import time
from matplotlib import pyplot as plt
import numpy as np

start = time.time()


def sum_of_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


def number_of_matches(start, stop, step=1):
    m = 0
    for n in range(start, stop, step):
        if sum_of_digits(n) == sum_of_digits(n*137):
            m += 1
    return m


def array_of_matches(start, stop, step=1):
    arr = []
    for n in range(start, stop, step):
        if sum_of_digits(n) == sum_of_digits(n*137):
            arr.append(sum_of_digits(n))
    return arr


def array_of_matches_before_sum(start, stop, step=1):
    arr = []
    for n in range(start, stop, step):
        if sum_of_digits(n) == sum_of_digits(n*137):
            arr.append(n)
    return arr


def count_freq(arr):
    freqs = {}
    unique_arr = set(arr)
    for element in unique_arr:
        n = 0
        for i in arr:
            if i == element:
                n += 1
        freqs[element] = n
    return freqs

def find_diff_arr(arr):
    arr_diff = []
    for i, n in enumerate(arr):
        if i != 0:
            arr_diff.append(n - arr_n[i-1])
    return arr_diff


r_start = 0
r_stop = int(10e5)
step = 9
print(number_of_matches(r_start, r_stop, step))
arr_n = array_of_matches_before_sum(r_start, r_stop, step)
arr = array_of_matches(r_start, r_stop, step)
print(arr)
print(count_freq(arr))
print(arr_n)

arr_diff = find_diff_arr(arr_n)
print(arr_diff)
x = range(len(arr_n))
x = np.array(x)
arr_n = np.array(arr_n)

# ----------------------------------
# Line of best fit
# ----------------------------------
x = x
y = arr_n
denominator = x.dot(x) - x.mean() * x.sum()
m = (x.dot(y) - y.mean() * x.sum()) / denominator
b = (y.mean() * x.dot(x) - x.mean() * x.dot(y)) / denominator
y_pred = m*x + b
print('y = {}*x + {}'.format(m, b))


# ----------------------------------
# R^2
# ----------------------------------
res = y - y_pred
tot = y - y.mean()
R_squared = 1 - res.dot(res) / tot.dot(tot)
print(R_squared)

# ----------------------------------
# Plot
# ----------------------------------
plt.scatter(x, y)
plt.plot(x, y_pred, 'r')
plt.xlabel('x')
plt.ylabel('n where sum_digits(n) == sum_digits(137n)')
plt.title('R squared = %.3f' % R_squared)
plt.savefig('plot.png')



elapsed = time.time() - start
print("Execution took %.2f seconds" % elapsed)
