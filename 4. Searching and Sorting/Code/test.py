def binarySearch(sorted_array, target):
    start = 0
    end = len(sorted_array) - 1
    while(start<=end):
        mid = (start+end)//2
        if sorted_array[mid] == target:
            return mid
        elif sorted_array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1
    
arr = [1, 2, 3, 4, 5, 6, 6, 17]
a = binarySearch(arr, 6)
print(a)