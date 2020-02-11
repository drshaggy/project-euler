import numpy as np
from helpers import *


# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------
def import_array_from_file(file_name):
    with open(file_name) as file:
        list_ = []
        for line in file:
            elements = line.split(' ')
            for i, element in enumerate(elements):
                elements[i] = int(element)
            list_.append(elements)
    return np.array(list_)


def calculate_max_adjacent_product(array, x, y):
    prod_x = 1
    prod_y = 1
    prod_pos_xy = 1
    prod_neg_xy = 1
    list_ = []
    for n in range(4):
        if y < 0 or x + n < 0 or y > 19 or x + n > 19:
            prod_x *= 0
        else:
            prod_x *= arr[y][x + n]
            list_.append(prod_x)
        if y + n < 0 or x < 0 or y + n > 19 or x > 19:
            prod_y = 0
        else:
            prod_y *= arr[y + n][x]
            list_.append(prod_y)
        if y + n < 0 or x + n < 0 or y + n > 19 or x + n > 19:
            prod_neg_xy = 0
        else:
            prod_neg_xy *= arr[y + n][x + n]
            list_.append(prod_neg_xy)
        if y - n < 0 or x + n < 0 or y - n > 19 or x + n > 19:
            prod_pos_xy = 0
        else:
            prod_pos_xy *= arr[y - n][x + n]
            list_.append(prod_pos_xy)
    return max(list_)


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    arr = import_array_from_file('data/problem11.txt')
    list_of_max_per_element = []
    for x in range(20):
        for y in range(20):
            list_of_max_per_element.append(calculate_max_adjacent_product(arr, x, y))
    print(len(list_of_max_per_element))
    print(max(list_of_max_per_element))
    timer.stop()



