def generate_fibonacci(elements):
    # Generate Fibonacci sequence to a number of elements
    if elements == 1:
        seq = [1]
        return seq
    elif elements == 2:
        seq = [1, 2]
        return seq
    else:
        seq = [1, 2]
        for x in range(elements - 2):
            next = calc_next_element(seq)
            seq.append(next)
        return seq


def calc_next_element(sequence):
    # Calculates next element to fibonacci sequence
    size = len(sequence)
    element = sum([sequence[size - 2], sequence[size - 1]])
    return element


def calc_fibonacci_to(number):
    a = 1
    i = 0
    while i <= number:
        arr = generate_fibonacci(a)
        i = max(arr)
        a += 1
        arr.pop()
    return arr


def get_even_subset(arr):
    even = []
    for x in arr:
        if x % 2 == 0:
            even.append(x)
        else:
            pass
    return even


print(sum(get_even_subset(calc_fibonacci_to(4000000))))
