def InsertionSort(lst):
    n = len(lst)
    for current in range(1, n):
        correctCard = lst[current]
        currentPosition = current - 1     #It will go from i-1 to 0

        while currentPosition >= 0:
            if correctCard > lst[currentPosition]:
                break
            else:
                lst[currentPosition + 1] = lst[currentPosition]
                currentPosition -= 1
        lst[currentPosition + 1] = correctCard 
    return lst

unsorted_lst = [34, 32, 99929, 2388, 32, 00, 124]
result = InsertionSort(unsorted_lst)
print(result)