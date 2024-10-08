#Method 1
def linearSearch(lst, target):
    for element in lst:
        if element == target:
            return lst.index(target)
    return -1    

#Method 2
def linearSearch2(lst, target):
    size = len(lst)
    for index in range(0, size):
        if lst[index] == target:
            return index
    return -1
    

my_list = [11, 20, 17, 35, 28]
target = 35

result = linearSearch(my_list, target)
print(result)

result1 = linearSearch2(my_list, target)
print(result)