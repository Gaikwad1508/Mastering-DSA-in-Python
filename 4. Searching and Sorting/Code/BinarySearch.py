def BinarySearch(sorted_list, target):
    start = 0
    end = len(sorted_list)-1

    while(start <= end):
        mid = (start + end)//2

        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            start = mid + 1
        elif sorted_list[mid] > target:
            end = mid - 1
            
    return -1

sorted_list = [1, 40, 65, 72, 84, 90, 299]
target = 84
result = BinarySearch(sorted_list, target)
print(result)