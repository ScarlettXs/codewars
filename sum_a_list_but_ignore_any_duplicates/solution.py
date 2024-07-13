def sum_no_duplicates(l):
    l.sort()
    reduce_list = []
    final_list = []
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            reduce_list.append(l[i])
    for item in l:
        if item not in reduce_list:
            final_list.append(item)
    result = sum(final_list)
    return result

