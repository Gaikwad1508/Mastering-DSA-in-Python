l1 = []

l1.append(1)
l1.append(1.5)
l1.append('python')

print(l1[0])


import array

arr = array.array('i',[1,2,3,4,5])
print(arr)
arr[0] = 10
print(arr)


import sys
l2 = []
print(sys.getsizeof(l2))

for i in range(17):
    l2.append(i)
    print(f"Length : {len(l2)} , Size : {sys.getsizeof(l2)}")