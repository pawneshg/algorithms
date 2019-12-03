arr = [64, 25, 12, 22, 11]

for arr_ind in range(len(arr)):
    min_ = arr[arr_ind]
    min_ind = arr_ind
    for ind in range(arr_ind, len(arr)):
        if arr[ind] < min_:
            min_ = arr[ind]
            min_ind = ind
    arr[arr_ind], arr[min_ind] = min_, arr[arr_ind]
print(arr)
