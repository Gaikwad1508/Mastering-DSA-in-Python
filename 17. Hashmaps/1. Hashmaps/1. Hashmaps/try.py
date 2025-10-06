class Hashmaps:
    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = [None] * capacity
        self.values = [None] * capacity
        self.size = 0

    #Function to hash the keys
    def hashFunction(self, key):
        return abs(hash(key)) % self.capacity
    
    def rehash(self, oldHashedKey):
        return (oldHashedKey + 1) % self.capacity

    def insert(self, key, value):
        hashedKey = self.hashFunction(key)

        if self.slots[hashedKey] is None:       #Key not present
            self.slots[hashedKey] = key
            self.values[hashedKey] = value
            self.size += 1
            return

        else:
            #Key already present, so update value only
            if self.slots[hashedKey] == key:
                self.values[hashedKey] = value
                return
            
            else:
                #check for collison condition
                newHashedKey = self.rehash(hashedKey)
                while self.slots[newHashedKey] is not None and self.slots[newHashedKey] != key:
                    newHashedKey = self.rehash(newHashedKey)

                #found empty slot
                if self.slots[newHashedKey] is None:
                    self.slots[newHashedKey] = key
                    self.values[newHashedKey] = value
                    self.size += 1
                    return
                
                else:   #found key already present, so update the value
                    self.values[newHashedKey] = value
                    return
                
    def get(self, key):
        initialHashedKey = self.hashFunction(key)
        currentHashedKey = initialHashedKey

        while self.slots[currentHashedKey] is not None:
            if self.slots[currentHashedKey] == key:
                return self.values[currentHashedKey]
            
            currentHashedKey = self.rehash(currentHashedKey)
            if currentHashedKey == initialHashedKey:
                return "key not found, traversal completed"
        return "key not found"    
    
    def delete(self, key):
        initialIndex = self.hashFunction(key)
        currentHashIndex = initialIndex

        while self.slots[currentHashIndex] is not None:
            #key found, delete it
            if self.slots[currentHashIndex] == key:
                self.slots[currentHashIndex] = None
                self.values[currentHashIndex] = None
                print(f"{key} deleted successfully")
                return
            
            currentHashIndex = self.rehash(currentHashIndex)
            if currentHashIndex == initialIndex:
                break
        print(f"{key} not found")
        return
    
    def __setitem__(self, key, value):
        return self.insert(key, value)
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __str__(self):
        result = []
        for i in range(self.capacity):
            if self.slots[i] is not None:
                result.append(f"{self.slots[i]} : {self.values[i]}")

        return "\n".join(result)
def countFrequency(words):
    hashmap = {}
    for word in words:
        if word in hashmap:
            hashmap[word] += 1
        else:
            hashmap[word] = 1
    return hashmap

def groupAnagrams(words):       #anagrams are the words having same letters with different order
    hashmap = {}
    for word in words:
        sortedWord = ''.join(sorted(word))
        if sortedWord in hashmap:
            hashmap[sortedWord].append(word)
        else:
            hashmap[sortedWord] = [word]
    return hashmap


class LLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, key, value):
        newNode = LLNode(key, value)
        newNode.next = self.head
        self.head = newNode

    def search(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None
    
    def delete(self, key):
        current = self.head
        prev = None

        while current:
            if current.key == key:
                #current is head
                if prev == None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False
    
    def traverse(self):
        current = self.head
        while current:
            print(f"{current.key} : {current.value} --> ", end = " ")
            current = current.next
        print("None")

class HashMapUsingChaining:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = self.__createBuckets(capacity)

    def __createBuckets(self, capacity):
        buckets = [LinkedList() for i in range(capacity)]
        return buckets
    
    def hashFunction(self, key):
        return abs(hash(key)) % self.capacity
    
    def rehash(self):
        print("Rehashing....")
        oldBuckets = self.buckets
        self.capacity = 2*self.capacity
        self.buckets = self.__createBuckets(self.capacity)
        self.size = 0

        for eachLLHead in oldBuckets:
            current = eachLLHead.head
            while current:
                self.insert(current.key, current.value)
                current = current.next


    
    def insert(self, key, value):
        bucketIndex = self.hashFunction(key)
        bucket = self.buckets[bucketIndex]

        node = bucket.search(key)

        if node is None:
            bucket.add(key, value)
            self.size += 1
        #key already present, so update the value
        else:
            node.value = value  

        loadFactor = self.size / self.capacity 
        if loadFactor > 0.75:
            self.rehash()

    def get(self, key):
        bucketIndex = self.hashFunction(key)
        bucket = self.buckets[bucketIndex]

        node = bucket.search(key)

        if node is None:
            return "key is not found"
        else:
            return node.value
        
    def remove(self, key):
        bucketIndex = self.hashFunction(key)
        bucket = self.buckets[bucketIndex]

        removed = bucket.delete(key)

        if removed:
            self.size -= 1
            return f"key {key} is removed from hashmap"
        
        else:
            return f"key {key} not found in hashmap"
        
    def __len__(self):
        return self.size
    
    def __str__(self):
        for i in range(self.capacity):
            if self.buckets[i] != None:
                self.buckets[i].traverse()

        return ""
    
    def __setitem__(self, key, value):
        return self.insert(key, value)
    
    def __getitem__(self, key):
        return self.get(key)



# words = ['eat','tea','tan','ate','nat','bat']
# dict1 = groupAnagrams(words)    
# print(dict1)

hash_map = HashMapUsingChaining(3)
# print((hash_map))
hash_map.insert("Apple",100)
hash_map.insert("Orange",105)
hash_map.insert("banana",200)
hash_map.insert("banana2",500) # 0.8
hash_map.insert("banana3",200)

# print((hash_map))
print(hash_map.get("Apple")) # Key should be case sensitive
print(hash_map.get("Orange"))
print(hash_map.get("banana"))

hash_map.remove("Apple")
print(hash_map.get("Apple")) 
print(len(hash_map))
print(hash_map)

print(hash_map["banana2"])
