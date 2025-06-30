def SelectionSort(lst):
    n = len(lst)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

unsorted_lst = [-8, 6, 41, 34, 52, 1]
result = SelectionSort(unsorted_lst)
print(result)