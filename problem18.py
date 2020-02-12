from helpers import Timer


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


def triangle_sums(triangle):
    new_tri = []
    for i, line in enumerate(triangle):
        if i == 0:
            pass
        else:
            new_line = []
            for i, element in enumerate(line[:-1]):
                new_line.append(line[i] + line[i + 1])
            new_tri.append(new_line)
    return new_tri


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    tri = import_triangle_from_file('data/problem18.txt')
    print(triangle_sums(tri))
    timer.stop()