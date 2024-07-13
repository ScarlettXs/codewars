def smaller(arr):
    list = []
    for i in range(len(arr)):
        number = arr[i]
        smaller_count = 0
        for f in range(len(arr)):
            if arr[f] < number and i < f:
                smaller_count += 1
        list.append(smaller_count)
    return list