#checking if array is sorted or not using recursion at head (i.e. mentioned recusive call first) 
#But it has an cache. That we will cover to solve in later part.

def checkSorted(l1):
    if(len(l1)==0 or len(l1)==1):
        return True
    
    ans = checkSorted(l1[1:])

    if(l1[0] < l1[1]):
        return ans
    else:
        return False
    

# As we have mentioned above comment we are gonna correct that cache issue by using tail recursion.
# that cache is unnecessary increase in depth of recursion. in previous code.
# So we will check the first two elements and then call the function with rest of the list.
# This will reduce the depth of recursion and hence will be more efficient.
def checkSorted1(l1):
    if (len(l1) == 0 or len(l1) == 1):
        return True
    
    if (l1[0] <= l1[1]):
        return checkSorted1(l1[1:])
    else: 

        return False

# below code is more efficient than previous one.
# As we are checking the first two elements and then calling the function with rest of the list.
# This will reduce the depth of recursion and hence will be more efficient.
def checkSorted2(l1):
    if(len(l1)==0 or len(l1)==1):
        return True
    
    if(l1[0] >= l1[1]):
        return False
    
    return checkSorted2(l1[1:])


l3 = [i for i in range(10000,1,-1) ]
# print(l3)
print(checkSorted2(l3))