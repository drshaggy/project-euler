from helpers import Timer


# ---------------------------------------------------------
# Helper Methods
# ---------------------------------------------------------
def load_number_dict(file_name):
    dict_ = {}
    with open(file_name) as file:
        for line in file:
            num, word = line.split(' ')
            dict_[num] = word[:-1]
    return dict_


def number_letter_counts(n, dict_):
    total = 0
    list_ = []
    for num in range(1, n + 1):
        word = get_number_word(num, dict_)
        list_.append(word)
        total += len(word)
    return total


def get_number_word(num, dict_):
    word = ''
    if num <= 20:
        word += dict_[str(num)]
    elif len(str(num)) == 2:
        try:
            word += dict_[str(num)[0] + '0']
            if str(num)[1] != '0':
                word += dict_[str(num)[1]]
        except KeyError:
            print("Error on {}".format(num))
    elif len(str(num)) == 3:
        try:
            word += dict_[str(num)[0]]
            word += 'hundred'
            if num != 100 * int(str(num)[0]) and num < 111 + ((int(str(num)[0]) - 1) * 100):
                word += 'and'
                if str(num)[1] != '0':
                    word += dict_[str(num)[1] + '0']
                if str(num)[2] != '0':
                    word += dict_[str(num)[2]]
            if 111 + ((int(str(num)[0]) - 1) * 100) <= num < 120 + ((int(str(num)[0]) - 1) * 100):
                word += 'and'
                word += dict_[str(num)[1:]]
            elif num >= 120 + ((int(str(num)[0]) - 1) * 100):
                if str(num)[1] != '0':
                    word += 'and'
                    word += dict_[str(num)[1] + '0']
                if str(num)[2] != '0':
                    word += dict_[str(num)[2]]
        except KeyError:
            print("Error on {}".format(num))
    elif len(str(num)) == 4:
        try:
            word += dict_[str(num)[0]]
            word += 'thousand'
            if str(num)[2] != '0':
                word += dict_[str(num)[1]]
                word += 'hundred'
            if str(num)[2] != '0':
                word += dict_[str(num)[2] + '0']
            if str(num)[3] != '0':
                word += 'and'
                word += dict_[str(num)[3]]
        except KeyError:
            print("Error on {}".format(num))
    return word


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    num_words = load_number_dict('data/problem17.txt')
    print(number_letter_counts(1000, num_words))
    timer.stop()
