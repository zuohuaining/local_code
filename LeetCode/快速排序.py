
def quick_sort(data, key=None, reverse=False):
    if len(data) <= 1:
        return data
    else:
        if not key:
            pivot = data[0]
            data_l = [i for i in data[1:] if i < pivot]
            data_r = [i for i in data[1:] if i > pivot]
        else:
            pivot = data[0]
            data_l = [i for i in data[1:] if key(i) < key(pivot)]
            data_r = [i for i in data[1:] if key(i) > key(pivot)]

        if reverse:
            data_l, data_r = data_r, data_l
        return quick_sort(data_l, key, reverse) + [pivot] + quick_sort(data_r, key, reverse)

data = [3,2,1,5,0]
print(quick_sort(data, key=lambda x: x*-1, reverse=True))