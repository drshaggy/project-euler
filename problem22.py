from helpers import Timer


# ---------------------------------------------------------
# Helper Methods
# ---------------------------------------------------------
char_worth = {'A': 1,
              'B': 2,
              'C': 3,
              'D': 4,
              'E': 5,
              'F': 6,
              'G': 7,
              'H': 8,
              'I': 9,
              'J': 10,
              'K': 11,
              'L': 12,
              'M': 13,
              'N': 14,
              'O': 15,
              'P': 16,
              'Q': 17,
              'R': 18,
              'S': 19,
              'T': 20,
              'U': 21,
              'V': 22,
              'W': 23,
              'X': 24,
              'Y': 25,
              'Z': 26}


def import_names_to_list(file_path):
    names = []
    with open(file_path) as file:
        for line in file:
            list_ = line.split(',')
            for item in list_:
                names.append(item[1:-1])
    return names

def get_worth(string):
    sum_ = 0
    for char in string:
        sum_ += char_worth[char]
    return sum_


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    names_ = import_names_to_list('data/problem22.txt')
    names_.sort()
    sum_ = 0
    for i, name in enumerate(names_):
        sum_ += (get_worth(name) * (i + 1))
    print(sum_)
    timer.stop()