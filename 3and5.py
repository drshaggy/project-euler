def multiple_of(multiple, max):
    # Find array of multiples up to a maximum limit
    arr = []
    for i in range(1, max):
        new = i * multiple
        if new < max:
            arr.append(new)
    return arr


def combine_array(arr1, arr2):
    # Combines arrays and remove duplicates and sorts
    for x in arr1:
        arr2.append(x)
    arr2.sort()
    new = list(set(arr2))
    return new


x = 1000
three = multiple_of(3, x)
five = multiple_of(5, x)
com = combine_array(three, five)
ans = sum(com)
print(ans)
