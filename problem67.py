from helpers import Timer
import numpy as np
import copy


# ---------------------------------------------------------
# Helper Methods
# ---------------------------------------------------------
def import_triangle_from_file(file_name):
    triangle = []
    with open(file_name) as file:
        for line in file:
            list_ = line.split(' ')
            int_list = []
            for i in list_:
                int_list.append(int(i))
            triangle.append(int_list)
    return triangle


def triangle_to_array(triangle):
    size = len(triangle)
    matrix = np.zeros(shape=(size, size))
    for i, row in enumerate(triangle):
        for j, element in enumerate(row):
            matrix[i][j] = element
    return matrix


# Finds max cost path when assessing the two adjacent values directly below
def max_cost_path(matrix):
    previous_index = None
    for i, row in enumerate(matrix):
        print(i)
        if i == 0:
            old_matrix = copy.deepcopy(matrix)
            matrix[i][0] = row[0]
            index = [0]
        else:
            new_index = set()
            for j in index:
                matrix[i][j] = max(matrix[i][j], matrix[i - 1][j] + old_matrix[i][j])
                new_index.add(j)
                matrix[i][j + 1] = max(matrix[i][j + 1], matrix[i - 1][j] + old_matrix[i][j + 1])
                new_index.add(j + 1)
            index = new_index
            print(index)
    print(matrix)
    return int(max(matrix[-1]))


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    tri = import_triangle_from_file('data/problem67.txt')
    timer.elapsed()
    mat = triangle_to_array(tri)
    timer.elapsed()
    cost_path = max_cost_path(mat)
    print(cost_path)
    timer.stop()