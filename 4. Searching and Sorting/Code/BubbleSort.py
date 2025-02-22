def BubbleSort(lst):
    n = len(lst)
    for passes in range(n-1):               # we require n-1 passes because as we put n-1 elements at right positions last one will get automatically at right position.
        for i in range(n-1-passes):        #As last element is sorted in each pass we are not comparing it.
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]

    return lst

unsorted_lst = [999, 389, 100, 26, 4, 1]
result = BubbleSort(unsorted_lst)
print(result)