def get_larger_numbers(a, b):
    arr3 = []
    for i in range(len(a)):
        arr3.append(max(a[i],b[i]))
    return arr3