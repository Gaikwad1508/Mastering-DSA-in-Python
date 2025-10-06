
## 1. Intersection Of Two Arrays
def intersection_of_arrays(arr1, arr2):
    hashmap = {}
    intersectionLst = []
    for num1 in arr1:
        if num1 in hashmap:
            hashmap[num1] += 1
        else:
            hashmap[num1] = 1

    for num2 in arr2:
        if num2 in hashmap and hashmap[num2] > 0:  # Check if num2 is in hashmap and count is positive
            intersectionLst.append(num2)           # Add num2 to intersection list
            hashmap[num2] -= 1                     # Decrement count in hashmap(very important step)
    return intersectionLst



# Example Usage:
arr1 = [1, 2, 2, 1]
arr2 = [2, 2, 2]
print(intersection_of_arrays(arr1, arr2))


# 2. Check for Duplicates

def contains_duplicates(nums): 
    hashmap = {}
    for num in nums:
        if num in hashmap:
            return True
        hashmap[num] = 1
    return False

# Example Usage:
nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
print(contains_duplicates(nums1))  # Output: True
print(contains_duplicates(nums2))  # Output: False


# 3. First Non Repeating Character in a string

def first_non_repeating_char(s):
    if not s:
        return "string is empty"
    hashmap = {}
    for char in s:
        if char in hashmap:
            hashmap[char] += 1
        else:
            hashmap[char] = 1

    for char in hashmap:
        if hashmap[char] == 1:
            return char
    return "non repeating character not present"
    

# Example Usage:
s = "swiss"
print(first_non_repeating_char(s)) # 'w'


